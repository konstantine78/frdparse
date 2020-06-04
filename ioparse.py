import re
import userdefined
DataTypesDict = {'F':'float','B':'bool','I':'int', 'OM':'OperatingMode', 'UI':'unsigned int'}
DataSyntaxDict = {'I':'Input', 'Inter':'Intermediate', 'O':'Output', 'AC':'AlignConst', 'DC':'DesignConst', 'LV':'LocalVar', 'F':'Fault'}
ID_PREFIX = ''

class Data:
    def __init__(self, sectionID, objectID, name, vi_name, datatype, datatype_abbreviated):
        self.sectionID = sectionID
        self.objectID = objectID
        self.name = name
        self.vi_name = vi_name
        self.datatype = datatype
        self.datatype_abbreviated = datatype_abbreviated
    
    def getName(self):
        return '{}'.format(self.name)

    def getVIName(self):
        return '{}'.format(self.vi_name)

    def getDataType(self, abbreviated=False):
        if abbreviated == True:
            return '{}'.format(self.datatype_abbreviated)
        else:
            return '{}'.format(self.datatype)

    def getSectionID(self):
        return '{}'.format(self.sectionID)

    def getObjectID(self):
        return '{}'.format(self.objectID)

    def getDataTypeAbbreviated(self):
        return '{}'.format(self.datatype_abbreviated)

    @classmethod
    def ConvertStringToData(cls, fullstring, majorID, minorID):
        ''' 
        class Data - ConvertStringToData:
        The ConvertStringToData is a classmethod for class Data.  It will return a 'Data' class with member
        variables populated with real data after having parsed through the string argument to this method.
        It has four arguments, one of which is the class Data itself, since it is a classmethod.  The other three
        arguments are as follows: 
        1. 

        This class method performs the following:
        1. The section ID will be equal the majorID argument.
        2. The object ID will be equal to the minorID argument to this method.
        3. The full string is updated to remove all spaces.
        4. Regular expression patterns are defined to determine the name, data type, and abbreviated data type.
        5. String searches with the regular expression patterns are performed to determine member values.
        
        '''
        sectionID = majorID
        objectID = minorID

        # Delete spaces.
        fullstring = fullstring.replace(" ", "")

        # Define the regular expressions to use for pattern recognition.
        name_pattern = re.compile(r':(.*)\(.\)')
        datatype_abbreviated_pattern = re.compile(r'\(([A-Z]*)\)')
        #source_pattern = re.compile(r'\(Source:(.*)\)' )

        # Name
        matched_string = name_pattern.search(fullstring)
        if matched_string: 
            name = matched_string[1]
        else:
            name = 'FAILED'
        
        vi_name = sectionID + '_' + name

        # Data type and abbreviation
        matched_string = datatype_abbreviated_pattern.search(fullstring)
        if matched_string: 
            datatype_abbreviated = matched_string[1]
            datatype = DataTypesDict[datatype_abbreviated]
        else:
            datatype_abbreviated = 'Could not determine abbreviated data type.'
            datatype = 'Could not determine data type.'
          
        return cls(sectionID, objectID, name, vi_name, datatype, datatype_abbreviated)
        
class Input(Data):
    def __init__(self, sectionID, objectID, name, vi_name, datatype, datatype_abbreviated, source, intermediate):
        super().__init__(sectionID, objectID, name, vi_name, datatype, datatype_abbreviated)
        self.source = source
        self.intermediate = intermediate
    
    def getSource(self):
        return '{}'.format(self.source)

    def isIntermediate(self):
        if self.intermediate == True:
            return True
        return False

    @classmethod
    def ConvertStringToData(cls, fullstring, majorID, minorID):
        ''' 
        class Input - ConvertStringToData:
        Parses through the fullstring and uses ID arguments to return a class instance of Input.
        
        '''
        sectionID = majorID
        objectID = minorID

        # Delete spaces.
        fullstring = fullstring.replace(" ", "")

        # Define the regular expressions to use for pattern recognition.
        name_pattern = re.compile(r':(.*)\(.\)')
        datatype_abbreviated_pattern = re.compile(r'\(([A-Z]*)\)')
        source_pattern = re.compile(r'\(Source:(.*)\)' )

        # Name
        matched_string = name_pattern.search(fullstring)
        if matched_string: 
            name = matched_string[1]
        else:
            name = 'Could not determine Name of data.'
        
        vi_name = sectionID + '_' + name
        
        # Data type and abbreviation
        matched_string = datatype_abbreviated_pattern.search(fullstring)
        if matched_string: 
            datatype_abbreviated = matched_string[1]
            datatype = DataTypesDict[datatype_abbreviated]
        else:
            datatype_abbreviated = 'Could not determine abbreviated data type.'
            datatype = 'Could not determine data type.'
        
        # Determine input signal 'Source'.
        matched_string = source_pattern.search(fullstring)
        source = matched_string[1] 
        if ID_PREFIX in source:
            intermediate = True
        else:
            intermediate = False

        return cls(sectionID, objectID, name, vi_name, datatype, datatype_abbreviated, source, intermediate)
        
class Output(Data):
    def __init__(self, sectionID, objectID, name, vi_name, datatype, datatype_abbreviated, destination):
        super().__init__(sectionID, objectID, name, vi_name, datatype, datatype_abbreviated)
        self.destination = destination

    def getDestination(self):
        return '{}'.format(self.destination)

    
    @classmethod
    def ConvertStringToData(cls, fullstring, majorID, minorID):
        ''' 
        class Output - ConvertStringToData:
        Parses through the fullstring and uses ID arguments to return a class instance of Output.
        
        '''
        sectionID = majorID
        objectID = minorID

        # Delete spaces.
        fullstring = fullstring.replace(" ", "")

        # Define the regular expressions to use for pattern recognition.
        name_pattern = re.compile(r':(.*)\(.\)')
        datatype_abbreviated_pattern = re.compile(r'\(([A-Z]*)\)')
        destination_pattern = re.compile(r'\(Destination:(.*)\)' )

        # Name
        matched_string = name_pattern.search(fullstring)
        if matched_string: 
            name = matched_string[1]
        else:
            name = 'Could not determine Name of data.'

        vi_name = sectionID + '_' + name

        # Data type and abbreviation
        matched_string = datatype_abbreviated_pattern.search(fullstring)
        if matched_string: 
            datatype_abbreviated = matched_string[1]
            datatype = DataTypesDict[datatype_abbreviated]
        else:
            datatype_abbreviated = 'Could not determine abbreviated data type.'
            datatype = 'Could not determine data type.'
        
        # Determine 'Destination'.
        if 'Destination:' in fullstring:
            matched_string = destination_pattern.search(fullstring)
            destination = matched_string[1]
        else:
            destination = 'NA'

        return cls(sectionID, objectID, name, vi_name, datatype, datatype_abbreviated, destination) 

class Constant(Data):
    def __init__(self, sectionID, objectID, name, vi_name, datatype, datatype_abbreviated, const_type, units, defaultvalue, minvalue, maxvalue):
        super().__init__(sectionID, objectID, name, vi_name, datatype, datatype_abbreviated)
        self.const_type = const_type
        self.units = units
        self.defaultvalue = defaultvalue
        self.minvalue = minvalue
        self.maxvalue = maxvalue

    def getDefaultValue(self, numeric=False):
        if numeric == True:
            if userdefined.is_int(self.defaultvalue):
                return int(self.defaultvalue)            
            elif userdefined.is_float(self.defaultvalue):
                return float(self.defaultvalue)
        else:
            return '{}'.format(self.defaultvalue)    
    
    def getUnits(self):
        return '{}'.format(self.units)    
    
    def getConstType(self):
        return '{}'.format(self.const_type)    
    
    def getMinValue(self, numeric=False):        
        if numeric == True:
            if userdefined.is_int(self.minvalue):
                return int(self.minvalue)
            elif userdefined.is_float(self.minvalue):
                return float(self.minvalue)
        else:
            return '{}'.format(self.minvalue)     
    
    def getMaxValue(self, numeric=False):        
        if numeric == True:
            if userdefined.is_int(self.maxvalue):
                return int(self.maxvalue)
            elif userdefined.is_float(self.maxvalue):
                return float(self.maxvalue)
        else:
            return '{}'.format(self.maxvalue)     
    
    @classmethod
    def ConvertStringToData(cls, fullstring, majorID, minorID):
        ''' 
        class Constant - ConvertStringToData:
        Parses through the fullstring and uses ID arguments to return a class instance of Constant.
        
        '''
        sectionID = majorID
        objectID = minorID

        # Delete spaces.
        fullstring = fullstring.replace(" ", "")

        # Define the regular expressions to use for pattern recognition.
        name_pattern = re.compile(r':(.*)\(.\)')
        datatype_abbreviated_pattern = re.compile(r'\(([A-Z]*)\)')

        # Name
        matched_string = name_pattern.search(fullstring)
        if matched_string: 
            name = matched_string[1]
        else:
            name = 'Could not determine Name of data.'

        vi_name = sectionID + '_' + name

        # Data type and abbreviation
        matched_string = datatype_abbreviated_pattern.search(fullstring)
        if matched_string: 
            datatype_abbreviated = matched_string[1]
            datatype = DataTypesDict[datatype_abbreviated]
        else:
            datatype_abbreviated = 'Could not determine abbreviated data type.'
            datatype = 'Could not determine data type.'

        # Determine the type of constant (Align or Design)
        if fullstring.startswith('AC'):
            const_type = 'AC'
        else:
            const_type = 'DC'

        # Determine the units for this constant.
        units = 'tbd'

        # Determine the default value for this constant.
        defaultvalue = 'tbd'

        # Determine the minimum and maximum values for this constant.
        minvalue = 'tbd'
        maxvalue = 'tbd'
          
        return cls(sectionID, objectID, name, vi_name, datatype, datatype_abbreviated, const_type, units, defaultvalue, minvalue, maxvalue)

class LocalVariable(Data):
    def __init__(self, sectionID, objectID, name, vi_name, datatype, datatype_abbreviated):
        super().__init__(sectionID, objectID, name, vi_name, datatype, datatype_abbreviated)

class Fault:
    def __init__(self, sectionID, objectID, faultname, vi_name, faultcode, faultdescr, faultcumlimit, faultconlimit):
        self.sectionID = sectionID
        self.objectID = objectID
        self.faultname = faultname
        self.vi_name = vi_name
        self.faultcode = faultcode
        self.faultdescr = faultdescr
        self.faultcumlimit = faultcumlimit
        self.faultconlimit = faultconlimit
    
    @classmethod
    def ConvertStringToFault(cls, fullstring, majorID, minorID):
        ''' 
        class Fault - ConvertStringToFault:
        Parses through the fullstring and uses ID arguments to return a class instance of Fault.
        
        '''
        
        # Define the Object ID
        sectionID = majorID
        objectID = minorID

        # Define the regular expressions to use for pattern recognition.
        faultname_pattern = re.compile(r':(.*)\(')
        faultcode_pattern = re.compile(r'\b0[xX][a-f0-9A-F]+\b')

        string_no_spaces = fullstring.replace(' ', '')

        # Name
        matched_string = faultname_pattern.search(string_no_spaces)
        if matched_string: 
            faultname = matched_string[1]
            vi_name = sectionID + '_' + faultname
        else:
            faultname = 'UNKNOWN FAULT NAME'
            vi_name = 'UNKNOWN VI_NAME'

        # Code
        matched_string = faultcode_pattern.search(string_no_spaces)
        if matched_string: 
            faultcode = matched_string[0]
        else:
            faultcode = '0xDEADBEEF'

        # Description
        faultdescr = fullstring.split('\"')[1]

        # Cumulative Limit
        faultcumlimit = string_no_spaces.split('\"')[2].split(',')[1].strip()

        # Consecutive Limit
        faultconlimit = string_no_spaces.split('\"')[2].split(',')[2].split(')')[0].strip()

        return cls(sectionID, objectID, faultname, vi_name, faultcode, faultdescr, faultcumlimit, faultconlimit)

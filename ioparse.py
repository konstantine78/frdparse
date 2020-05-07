import re
import csv
import os

DataTypesDict = {'F':'float','B':'bool','I':'int', 'OM':'OperatingMode', 'UI':'unsigned int'}
DataSyntaxDict = {'I':'Input', 'O':'Output', 'AC':'AlignConst', 'DC':'DesignConst', 'LV':'LocalVar', 'F':'Fault'}

def syntaxKey(line):
    if line.startswith('I:'):
        return DataSyntaxDict.get('I')
    if line.startswith('O:'):
        return DataSyntaxDict.get('O')
    if line.startswith('AC:'):
        return DataSyntaxDict.get('AC')
    if line.startswith('DC:'):
        return DataSyntaxDict.get('DC')
    if line.startswith('LV:'):
        return DataSyntaxDict.get('LV')
    if line.startswith('F:'):
        return DataSyntaxDict.get('F')

def isConstant(mystring):
    pattern = re.compile(r'AC:{1}|DC:{1}').search(mystring)
    if pattern:
        return True
    else:
        return False

def isConditional(mystring):
    pattern = re.compile(r'C:').search(mystring)
    if pattern:
        return True
    else: 
        return False

def is_float(value):
  try:
    float(value)
    return True
  except:
    return False
    
def is_int(value):
  try:
    int(value)
    return True
  except:
    return False
 
def write_data_to_csv_output(theList, csvwriter):
    for i in range (len(theList)):
        csvwriter.writerow(
            [
                theList[i].name,
                theList[i].datatype,
                theList[i].datatype_abbreviated,
                theList[i].objectID,
                theList[i].source,
                theList[i].destination,
                theList[i].units,
                theList[i].defaultvalue,
                theList[i].minvalue,
                theList[i].maxvalue,
                ]
            )

def write_faults_to_csv_output(theList, csvwriter):
    for i in range (len(theList)):
        csvwriter.writerow(
            [
                theList[i].objectID,
                theList[i].faultname,
                theList[i].faultcode,
                theList[i].faultdescr,
                theList[i].faultcumlimit,
                theList[i].faultconlimit,
                ]
            )

def csv_file_cleanup(path, infile, outfile, delete=False):
    with open(path + infile, 'r') as input:
        with open(path + outfile, 'w') as output:
            non_blank_lines = (line for line in input if line.strip())
            output.writelines(non_blank_lines)
    if delete == True:
        delete_file(path, infile)    

def delete_file(path, file):
    os.chdir(path)
    os.remove(file)
    print(path+file+' has been deleted.')

class Data:
    def __init__(self, name, datatype, datatype_abbreviated, objectID, source, destination, units, defaultvalue, minvalue, maxvalue):
        self.name = name
        self.datatype = datatype
        self.datatype_abbreviated = datatype_abbreviated
        self.objectID = objectID
        self.source = source
        self.destination = destination
        self.units = units
        self.defaultvalue = defaultvalue
        self.minvalue = minvalue
        self.maxvalue = maxvalue
    
    def getName(self):
        return '{}'.format(self.name)

    def getDataType(self, abbreviated=False):
        if abbreviated == True:
            return '{}'.format(self.datatype_abbreviated)
        else:
            return '{}'.format(self.datatype)

    def getObjectID(self):
        return '{}'.format(self.objectID)

    def getSource(self):
        return '{}'.format(self.source)

    def getDefaultValue(self, numeric=False):
        if numeric == True:
            if is_float(self.defaultvalue):
                return float(self.defaultvalue)
            elif is_int(self.defaultvalue):
                return int(self.defaultvalue)
        else:
            return '{}'.format(self.defaultvalue)

    @classmethod
    def ConvertStringToData(cls, fullstring, keyword, ID):
        ''' 
        ---------------------------------------------------------------------------------------------------------
        ConvertStringToData:
        The ConvertStringToData is a classmethod for class Data.  It will return a 'Data' class with member
        variables populated with real data after having parsed through the string argument to this method.
        It has four arguments, one of which is the class Data itself, since it is a classmethod.  The other three
        arguments are as follows: 
        1. fullstring - this is the line feed from the exported text input file.
        2. keyword - this is the first part of the full string that provides the data syntax for defining what
        type of data it is.
        3. ID - This is the object identifier for the line.

        This class method performs the following:
        1. The object ID will be equal to the ID argument to this method.
        2. The full string is updated to remove all spaces.
        3. Regular expression patterns are defined to determine the name, data type, and source (for inputs).  
        4. String searches with the regular expression patterns are performed to determine member values.
        4. The keyword is used to determine various class members' values.
        ---------------------------------------------------------------------------------------------------------
        '''
        objectID = ID

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

        # Data type and abbreviation
        matched_string = datatype_abbreviated_pattern.search(fullstring)
        if matched_string: 
            datatype_abbreviated = matched_string[1]
            datatype = DataTypesDict[datatype_abbreviated]
        else:
            datatype_abbreviated = 'Could not determine abbreviated data type.'
            datatype = 'Could not determine data type.'
        
        # Determine input signal 'Source'.  All others are N/A.
        matched_string = source_pattern.search(fullstring)
        if keyword == 'Input' and matched_string:
            source = matched_string[1]
        else: 
            source = 'N/A'

        # Determine Destination.  This only applies to Output and Local Variable Data.
        if keyword == 'Output' or keyword == 'LocalVar':
            destination = 'tbd'
        else:
            destination = 'N/A'
        
        # Determine Units.  Everyone has units but Local Variables.
        if keyword != 'LocalVar':
            units = 'tbd'
        else: 
            units = 'N/A'

        # Determine the default value.
        defaultvalue = 'N/A'

        # Determine the minimum and maximum values.  This applies to alignment constants only.
        if keyword == 'AlignConst':
            minvalue = 'tbd'
            maxvalue = 'tbd'
        else:
            minvalue = 'N/A'
            maxvalue = 'N/A'

        return cls(name, datatype, datatype_abbreviated, objectID, source, destination, units, defaultvalue, minvalue, maxvalue)
        
class Input(Data):
    def __init__(self, name, datatype, datatype_abbreviated, objectID, source, destination, units, defaultvalue, minvalue, maxvalue):
        super().__init__(name, datatype, datatype_abbreviated, objectID, source, destination, units, defaultvalue, minvalue, maxvalue)
    
class Output(Data):
    def __init__(self, name, datatype, datatype_abbreviated, objectID, source, destination, units, defaultvalue, minvalue, maxvalue):
        super().__init__(name, datatype, datatype_abbreviated, objectID, source, destination, units, defaultvalue, minvalue, maxvalue)

class AlignConst(Data):
    def __init__(self, name, datatype, datatype_abbreviated, objectID, source, destination, units, defaultvalue, minvalue, maxvalue):
        super().__init__(name, datatype, datatype_abbreviated, objectID, source, destination, units, defaultvalue, minvalue, maxvalue)
        
class DesignConst(Data):
    def __init__(self, name, datatype, datatype_abbreviated, objectID, source, destination, units, defaultvalue, minvalue, maxvalue):
        super().__init__(name, datatype, datatype_abbreviated, objectID, source, destination, units, defaultvalue, minvalue, maxvalue)
        
class LocalVariable(Data):
    def __init__(self, name, datatype, datatype_abbreviated, objectID, source, destination, units, defaultvalue, minvalue, maxvalue):
        super().__init__(name, datatype, datatype_abbreviated, objectID, source, destination, units, defaultvalue, minvalue, maxvalue)

class Fault:
    def __init__(self, objectID, faultname, faultcode, faultdescr, faultcumlimit, faultconlimit):
        self.objectID = objectID
        self.faultname = faultname
        self.faultcode = faultcode
        self.faultdescr = faultdescr
        self.faultcumlimit = faultcumlimit
        self.faultconlimit = faultconlimit
    
    @classmethod
    def ConvertStringToFault(cls, fullstring, ID):
        
        # Define the Object ID
        objectID = ID

        # Define the regular expressions to use for pattern recognition.
        faultname_pattern = re.compile(r':(.*)\(')
        faultcode_pattern = re.compile(r'\b0[xX][a-f0-9A-F]+\b')

        string_no_spaces = fullstring.replace(' ', '')

        # Name
        matched_string = faultname_pattern.search(string_no_spaces)
        if matched_string: 
            faultname = matched_string[1]
        else:
            faultname = 'UNKNOWN'

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

        return cls(objectID, faultname, faultcode, faultdescr, faultcumlimit, faultconlimit)

import re

DataTypes = {'F':'float','B':'bool','I':'int', 'OM':'OperatingMode', 'UI':'unsigned int'}
SignalTypes = {'I':'Input', 'O':'Output', 'A':'AlignmentConstant', 'D':'DesignConstant'}

# Determine if the string is an input or output definition.  The first two characters must be an 'I:' or 'O:'
def isIO(mystring):
    pattern = re.compile(r'I:|O:').search(mystring)
    if pattern:
        return True
    else: 
        return False

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

# This function will perform a dictionary lookup to determine what the data type is based
# on the abbreviated version of the data type.
def getDataType(abbreviation):
    return DataTypes[abbreviation]
 
def write_to_csv_output(theList, csvwriter):
    for i in range (len(theList)):
        csvwriter.writerow(
            [
                theList[i].signal_type,
                theList[i].datatype_abbreviated,
                theList[i].datatype,
                theList[i].signal_name,
                theList[i].reference_id,
                theList[i].input_source
                ]
            )

class Signal:
    def __init__(self, signal_type, datatype_abbreviated, datatype, signal_name, reference_id, input_source):
        # initialize  here.
        self.signal_type = signal_type
        self.datatype_abbreviated = datatype_abbreviated
        self.datatype = datatype
        self.signal_name = signal_name
        self.reference_id = reference_id
        self.input_source = input_source

    # Returns the signal's name.
    def getDataType(self):
        return '{}'.format(self.datatype)

    @classmethod
    # This class method will return an instance of Class Signal.
    def stringToIOConvert(cls, s, theID):
        # Takes the full string of either an input 'I:' or output 'O:' and returns
        # the I/O data type, signal name, and signal type.  This function will strip all
        # spaces, then split the string into smaller chunks via referencing ':', '(', and ')'
        # This functions assumes string is of the following:
        #           I: InputVariable1(F)(Source: GSCC2_3)

        s = s.replace(" ", "")
        # Define the regular expressions to use for pattern recognition and pulling appropriate text out downstream.
        signal_name_pattern = re.compile(r':(.*)\(.\)')
        input_source_pattern = re.compile(r'\(Source:(.*)\)' )
        signal_type_pattern = re.compile(r'I:{1}|O:{1}|DC:{1}|AC:{1}')
        datatype_abbreviated_pattern = re.compile(r'\(([A-Z]*)\)')

        # Signal name
        matched_string = signal_name_pattern.search(s)
        if matched_string: 
            signal_name = matched_string[1]

        # Signal type; is it an input, output, or constant?
        matched_string = signal_type_pattern.search(s)
        signal_type = str(matched_string[0])[0]

        if matched_string:
            signal_type = SignalTypes[signal_type]

        # Input source outputs get text string that makes it obvious there's no input source.
        matched_string = input_source_pattern.search(s)

        if matched_string and signal_type != 'Output':
            input_source = matched_string[1]
        else: 
            input_source = 'N/A'

        # Data type
        matched_string = datatype_abbreviated_pattern.search(s)
        if matched_string: 
            datatype_abbreviated = matched_string[1]
            datatype = DataTypes[datatype_abbreviated]
        
        reference_id = theID
        return cls(signal_type, datatype_abbreviated, datatype, signal_name, reference_id, input_source)

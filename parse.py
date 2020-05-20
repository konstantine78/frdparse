import re
import csv
import userdefined
import ioparse
from ioparse import Input as i_data
from ioparse import Output as o_data
from ioparse import Constant as c_data
from ioparse import Fault as fault_data

def parse_export_file(path, id_prefix):
    '''
    ----------------------------------------------------------------------------------------------------------------------------
    The parse_export_file function takes two arguments, path and id prefix.  This is used downstream to aid in 
    parsing through a text file located in 'path' and searching for the id prefix.  Steps in this function are:
    1. Open the exported text file.  Note, all opening of files is performed with context managers.
    2. Remove empty lines and copy the conntents into a temporary file, 'output.txt'.
    3. Open 'output.txt' and declare local lists that will retain class instances of Class Signal from ioparse.py.
    4. Loop through the text file using the object identifier as a point of reference.  The assumption is that the object id
    is at the beginning of the "section of text" in question, whether it be Data definition or conditional statements.  We want
    to loop through, identify those objects that represent Data and then further loop through statements to create
    our lists of Data (or sub-classes to Data) and Fault class instances.  
    5. Parsing is performed mostly via regular expression matched strings and general string manipulation.  At the heart of 
    the parsing are the classmethods that are called from module ioparse.  These methods are custom classmethods
    and will return the class, Data (or Fault), from ioparse and allow for instantiation local to parse.py.  
    6. Once the lists are updated, and parsing has ceased, the lists are then written out to a *.csv file for archiving/use.
    7. Temporary files are then deleted and the lists are returned once the method has completed running.
    ----------------------------------------------------------------------------------------------------------------------------
    '''
    path = path+'/'
    ioparse.ID_PREFIX = id_prefix
    with open(path + 'exportedfile.txt', 'r') as infile:
        with open(path + 'output.txt', 'w') as outfile:
            for line in infile:
                if not line.strip(): continue  # skip the empty line
                outfile.write(line)  # non-empty line. Write it to output

    with open(path + 'output.txt', 'r') as f:
        file_contents = f.readlines()

    objectID = ''
    sectionID = ''
    inputs = list()
    outputs = list()
    constants = list()
    local_variables = list()
    faults = list()

    # Parsing starts now.
    for line in file_contents:
        line.strip() 

        # At EOF; therefore, we're done.
        if line.startswith('#ENDOFFILE'):
            pass
        
        # Record the Object ID , as it is used in all instances of class below.  Everything has an Object ID.
        if line.startswith('Object Identifier: ' + id_prefix):
            objectID = re.compile(r'\w+[0-9]').search(line)[0]

        if line.startswith('Type:') and ('Section' in line):
            sectionID = objectID

        # Check beginning of each line for Data-specific syntax.
        if line.startswith('I:'):
            inputs.append(i_data.ConvertStringToData(line, sectionID, objectID))
        if line.startswith('O:'):
            outputs.append(o_data.ConvertStringToData(line, sectionID, objectID))
        if line.startswith('AC:') or line.startswith('DC'):
            constants.append(c_data.ConvertStringToData(line, sectionID, objectID))
        if line.startswith('LV:'):
            local_variables.append('PLACEHOLDER')
            pass# This is a PLACEHOLDER
        if line.startswith('F:'):
            faults.append(fault_data.ConvertStringToFault(line, sectionID, objectID))
            pass# This is a PLACEHOLDER
        else:
            pass# This is a PLACEHOLDER

    # Write all data to csv files and perform cleanup.
    userdefined.update_output_data_files(path, inputs, outputs, constants, faults)

    # Return the lists for use downstream in creation of mysql database.
    return inputs, outputs, constants, faults

# This is used to run the file on its own without GUI.
#path = 'C:/Users/kostas/Documents/GitHub/frdparse/exporttextfiles/'
#parse_export_file(path, 'APPSW')
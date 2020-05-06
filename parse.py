import re
import csv
import os
import ioparse
from ioparse import Data as data

def parse_export_file(path, id_prefix):
    '''
    ----------------------------------------------------------------------------------------------------------------------------
    The parse_export_file function takes two arguments, path and id prefix.  This is used downstream to aid in 
    parsing through a text file located in 'path' and searching for the id prefix.  Steps in this function are:
    1. Open the exported text file.  Note, all opening of files is performed with context managers.
    2. Remove empty lines and copy the conntents into a temporary file, 'output.txt'.
    3. Open 'output.txt' and declare local lists that will retain class instances of Class Signal from ioparse.py.
    4. Loop through the text file using the object identifier as a point of reference.  The assumption is that the object id
    is at the beginning of the "section of text" in question, whether it be I/O definition or conditional statements.  We want
    to loop through, identify those objects that represent I/O signals and then further loop through I/O statements to create
    our lists of Signal class instances.  
    5. Parsing is performed mostly via regular expression matched strings and general string manipulation.  At the heart of 
    the parsing is the 'stringToIOConvert' method that is called from module ioparse.  This method is a classmethod
    and will return the class, Signal, from ioparse and allow for instantiation local to parse.py.  
    6. Once the lists are updated, and parsing has ceased, the lists are then written out to a *.csv file for archiving/use.
    7. Temporary files are then deleted and the lists are returned once the method has completed running.
    ----------------------------------------------------------------------------------------------------------------------------
    '''
    path = path+'/'
    with open(path + 'exportedfile.txt') as infile, open(path + 'output.txt', 'x') as outfile:
        for line in infile:
            if not line.strip(): continue  # skip the empty line
            outfile.write(line)  # non-empty line. Write it to output

    with open(path + 'output.txt', 'r') as f:
        file_contents = f.readlines()

    input_signals = list()
    output_signals = list()
    align_constants = list()
    design_constants = list()
    theKey = 'UNKNOWN'

    # Parsing starts now.
    for line in file_contents:
        line.strip() 

        # At EOF; therefore, we're done.
        if line.startswith('#ENDOFFILE'):
            pass
        
        # Record the Object ID to theID, as it is used in all instances of class Signal below.  Everything has an Object ID.
        if line.startswith('Obect Identifier: ' + id_prefix):
            theID = re.compile(r'\w+[0-9]').search(line)[0]

        # Check beginning of each line for Data-specific syntax.
        if line.startswith('I:'):
            input_signals.append(data.ConvertStringToData(line, ioparse.DataSyntaxDict.get('I'), theID))
        if line.startswith('O:'):
            output_signals.append(data.ConvertStringToData(line, ioparse.DataSyntaxDict.get('O'), theID))
        if line.startswith('AC:'):
            align_constants.append(data.ConvertStringToData(line, ioparse.DataSyntaxDict.get('AC'), theID))
        if line.startswith('DC:'):
            design_constants.append(data.ConvertStringToData(line, ioparse.DataSyntaxDict.get('DC'), theID))
        if line.startswith('LV:'):
            pass# This is a PLACEHOLDER
        if line.startswith('F:'):
            pass# This is a PLACEHOLDER
        else:
            pass# This is a PLACEHOLDER

    # Write to a temporary *.csv file.
    with open(path + 'temp.csv', 'w') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter='\t')

        #Write the top header fields for columns
        csv_writer.writerow(
            ['Name', 'Data Type', 'Data Type Abbrev.', 'Object ID', 
            'Source', 'Destination', 'Units', 'Default Value', 'Minimum Value', 'Maximum Value']
            )

        ioparse.write_to_csv_output(input_signals, csv_writer)
        ioparse.write_to_csv_output(output_signals, csv_writer)    
        ioparse.write_to_csv_output(align_constants, csv_writer)    
        ioparse.write_to_csv_output(design_constants, csv_writer)

    # Get rid of blank lines in the csv and output the final *.csv file.
    with open(path + 'temp.csv', 'r') as input:
        with open(path + 'MyIOSignals.csv', 'w') as output:
            non_blank_lines = (line for line in input if line.strip())
            output.writelines(non_blank_lines)

    #Clean up.  Delete temporary/intermediate files.
    os.chdir(path)
    os.remove('temp.csv')
    os.remove('output.txt')

    # Return the lists for use downstream in creation of mysql database.
    return input_signals, output_signals, align_constants, design_constants
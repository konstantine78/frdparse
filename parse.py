import re
import csv
import os
import ioparse
from ioparse import Signal as io

# Define the object ID prefix and the object ID pattern (i.e., Prefix*, where * is any number of integer digits)
id_prefix = "APPSW"
end_of_file = '#ENDOFFILE'

# Open the file with a context manager.  It will automatically handle the opening and closing of the file.
# Open the initial export file and loop through each line to remove any blank lines.  Write all "actual" lines
# to the cleaned up version of the FRD export file, and read in its contents once again.
with open('/Users/kostas/MyPythonProjects/frdparse/exporttextfiles/exportedfile.txt') as infile, open('/Users/kostas/MyPythonProjects/frdparse/exporttextfiles/output.txt', 'x') as outfile:
    for line in infile:
        if not line.strip(): continue  # skip the empty line
        outfile.write(line)  # non-empty line. Write it to output

with open('/Users/kostas/MyPythonProjects/frdparse/exporttextfiles/output.txt', 'r') as f:
    file_contents = f.readlines()

input_signals = list()
output_signals = list()
align_constants = list()
design_constants = list()

# Loop through the text file using the object identifier as a point of reference.  The assumption is that the object id
# is at the beginning of the "section of text" in question, whether it be I/O definition or conditional statements.  We want
# to loop through, identify those objects that represent I/O signals and then further loop through I/O statements to create
# our lists of Signal class instances.  
for line in file_contents:
    # Strip the whitespace at beginning and end of the line.
    line.strip() 

    # If we're at the last line (i.e., the end) break out of this.
    if line.startswith(end_of_file):
        pass
    
    # If the line is an object identifier object, record the object ID, which will have the pattern of 'id_prefix' followed by numbers.
    if line.startswith('Obect Identifier: ' + id_prefix):
        theID = re.compile(r'\w+[0-9]').search(line)[0]
        #print('The Object identifier (ID) has been updated to: ' + theID)

    # Check if text is defining I/O signals.
    if ioparse.isIO(line) == True:
        if line.startswith('I:'):
            input_signals.append(io.stringToIOConvert(line, theID))
        else:            
            output_signals.append(io.stringToIOConvert(line, theID))
    elif ioparse.isConstant(line) == True:
        if line.startswith('AC:'):
            align_constants.append(io.stringToIOConvert(line, theID))        
        else:            
            design_constants.append(io.stringToIOConvert(line, theID))
    elif ioparse.isConditional(line) == True:
        pass# This is a PLACEHOLDER for conditional statements.
    else:
        pass# This is a PLACEHOLDER for any non-IO or non-Conditional statements.
    
with open('/Users/kostas/MyPythonProjects/frdparse/exporttextfiles/MyIOSignals.txt', 'w') as io_f:
    io_f.write('***********************INPUT SIGNALS*******************************\n')
    ioparse.write_to_txt_output(input_signals, io_f)
    io_f.write('**********************OUTPUT SIGNALS*******************************\n')
    ioparse.write_to_txt_output(output_signals, io_f)
    io_f.write('**********************ALIGN CONSTANTS******************************\n')
    ioparse.write_to_txt_output(align_constants, io_f)  
    io_f.write('**********************DESIGN CONSTANTS*****************************\n') 
    ioparse.write_to_txt_output(design_constants, io_f)
    io_f.write('********************END OF SIGNALS LIST****************************\n')

with open('/Users/kostas/MyPythonProjects/frdparse/exporttextfiles/temp.csv', 'w') as csv_file:
    csv_writer = csv.writer(csv_file, delimiter='\t')

    #Write the top header fields for columns
    csv_writer.writerow(['Signal Type', 'Data Type Abbrev.', 'Data Type', 'Signal Name', 'ID', 'Source ID'])
    
    ioparse.write_to_csv_output(input_signals, csv_writer)
    ioparse.write_to_csv_output(output_signals, csv_writer)    
    ioparse.write_to_csv_output(align_constants, csv_writer)    
    ioparse.write_to_csv_output(design_constants, csv_writer)

# Get rid of blank lines in the csv.
with open('/Users/kostas/MyPythonProjects/frdparse/exporttextfiles/temp.csv', 'r') as input:
    with open('/Users/kostas/MyPythonProjects/frdparse/exporttextfiles/MyIOSignals.csv', 'w') as output:
        non_blank_lines = (line for line in input if line.strip())
        output.writelines(non_blank_lines)

os.chdir('/Users/kostas/MyPythonProjects/frdparse/exporttextfiles/')
os.remove('temp.csv')
os.remove('output.txt')

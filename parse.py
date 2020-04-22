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
with open('/Users/kostas/MyPythonProjects/frdexports/exporttextfiles/exportedfile.txt') as infile, open('/Users/kostas/MyPythonProjects/frdexports/exporttextfiles/output.txt', 'x') as outfile:
    for line in infile:
        if not line.strip(): continue  # skip the empty line
        outfile.write(line)  # non-empty line. Write it to output

with open('/Users/kostas/MyPythonProjects/frdexports/exporttextfiles/output.txt', 'r') as f:
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
        print('The Object identifier (ID) has been updated to: ' + theID)

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
    
with open('/Users/kostas/MyPythonProjects/frdexports/exporttextfiles/MyIOSignals.txt', 'w') as io_f:
    io_f.write('*******************************************************************\n')
    io_f.write('***********************INPUT SIGNALS*******************************\n')
    io_f.write('*******************************************************************\n')

    for i in range (len(input_signals)):
        io_f.write('Signal Type: ' + input_signals[i].signal_type +'\n')
        io_f.write('Abbreviated Data Type: ' + input_signals[i].datatype_abbreviated +'\n')
        io_f.write('Data Type: ' + input_signals[i].datatype +'\n')
        io_f.write('Signal Name: ' + input_signals[i].signal_name +'\n')
        io_f.write('Reference ID: ' + input_signals[i].reference_id +'\n')
        io_f.write('Input Source (if applicable): ' + input_signals[i].input_source +'\n')
        io_f.write('-------------------------\n')
    io_f.write('*******************************************************************\n')
    io_f.write('**********************OUTPUT SIGNALS*******************************\n')
    io_f.write('*******************************************************************\n')
    for i in range (len(output_signals)):
        io_f.write('Signal Type: ' + output_signals[i].signal_type +'\n')
        io_f.write('Abbreviated Data Type: ' + output_signals[i].datatype_abbreviated +'\n')
        io_f.write('Data Type: ' + output_signals[i].datatype +'\n')
        io_f.write('Signal Name: ' + output_signals[i].signal_name +'\n')
        io_f.write('Reference ID: ' + output_signals[i].reference_id +'\n')
        io_f.write('-------------------------\n')
    io_f.write('*******************************************************************\n')
    io_f.write('**********************ALIGN CONSTANTS******************************\n')
    io_f.write('*******************************************************************\n')    
    for i in range (len(align_constants)):
        io_f.write('Signal Type: ' + align_constants[i].signal_type +'\n')
        io_f.write('Abbreviated Data Type: ' + align_constants[i].datatype_abbreviated +'\n')
        io_f.write('Data Type: ' + align_constants[i].datatype +'\n')
        io_f.write('Signal Name: ' + align_constants[i].signal_name +'\n')
        io_f.write('Reference ID: ' + align_constants[i].reference_id +'\n')
        io_f.write('Input Source (if applicable): ' + align_constants[i].input_source +'\n')
        io_f.write('-------------------------\n')
    io_f.write('*******************************************************************\n')
    io_f.write('**********************DESIGN CONSTANTS*****************************\n')
    io_f.write('*******************************************************************\n')    
    for i in range (len(design_constants)):
        io_f.write('Signal Type: ' + design_constants[i].signal_type +'\n')
        io_f.write('Abbreviated Data Type: ' + design_constants[i].datatype_abbreviated +'\n')
        io_f.write('Data Type: ' + design_constants[i].datatype +'\n')
        io_f.write('Signal Name: ' + design_constants[i].signal_name +'\n')
        io_f.write('Reference ID: ' + design_constants[i].reference_id +'\n')
        io_f.write('Input Source (if applicable): ' + design_constants[i].input_source +'\n')
        io_f.write('-------------------------\n')
    io_f.write('*******************************************************************\n')
    io_f.write('********************END OF SIGNALS LIST****************************\n')
    io_f.write('*******************************************************************\n')

with open('/Users/kostas/MyPythonProjects/frdexports/exporttextfiles/temp.csv', 'w') as csv_file:
    csv_writer = csv.writer(csv_file, delimiter='\t')

    #Write the top header fields for columns
    csv_writer.writerow(['Signal Type', 'Data Type Abbrev.', 'Data Type', 'Signal Name', 'ID', 'Source ID'])
    for i in range (len(input_signals)):
        csv_writer.writerow(
            [
                input_signals[i].signal_type,
                input_signals[i].datatype_abbreviated,
                input_signals[i].datatype,
                input_signals[i].signal_name,
                input_signals[i].reference_id,
                input_signals[i].input_source
                ]
            )
    for i in range (len(output_signals)):
        csv_writer.writerow(
            [
                output_signals[i].signal_type,
                output_signals[i].datatype_abbreviated,
                output_signals[i].datatype,
                output_signals[i].signal_name,
                output_signals[i].reference_id,
                output_signals[i].input_source
                ]
            )
    for i in range (len(align_constants)):
        csv_writer.writerow(
            [
                align_constants[i].signal_type,
                align_constants[i].datatype_abbreviated,
                align_constants[i].datatype,
                align_constants[i].signal_name,
                align_constants[i].reference_id,
                align_constants[i].input_source
                ]
            )
    for i in range (len(design_constants)):
        csv_writer.writerow(
            [
                design_constants[i].signal_type,
                design_constants[i].datatype_abbreviated,
                design_constants[i].datatype,
                design_constants[i].signal_name,
                design_constants[i].reference_id,
                design_constants[i].input_source
                ]
            )

with open('/Users/kostas/MyPythonProjects/frdexports/exporttextfiles/temp.csv', 'r') as input:
    with open('/Users/kostas/MyPythonProjects/frdexports/exporttextfiles/MyIOSignals.csv', 'w') as output:
        non_blank_lines = (line for line in input if line.strip())
        output.writelines(non_blank_lines)

os.chdir('/Users/kostas/MyPythonProjects/frdexports/exporttextfiles/')
os.remove('temp.csv')
os.remove('output.txt')

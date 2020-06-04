import csv
import os

inputsheader = ['Section ID', 'Object ID', 'Name', 'VI Name', 'Data Type', 'Data Type Abbrev.', 'Source', 'Intermediate']
outputsheader = ['SectionID', 'Object ID', 'Name', 'VI Name', 'Data Type', 'Data Type Abbrev.', 'Destination']
constantsheader = ['SectionID', 'Object ID', 'Name', 'VI Name', 'Data Type', 'Data Type Abbrev.', 'Type', 'Units', 'Default Value', 'Min', 'Max']
faultsheader = ['SectionID', 'Object ID', 'Faultname', 'VI Name', 'Faultcode', 'Description', 'Cumulative Limit', 'Consecutive Limit']

def update_output_data_files(path, inputs, outputs, constants, faults):
    with open(path + 'temp1.csv', 'w') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter='\t')
        csv_writer.writerow(inputsheader)
        write_inputs_to_csv(inputs, csv_writer)
    with open(path + 'temp2.csv', 'w') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter='\t')
        csv_writer.writerow(outputsheader)
        write_outputs_to_csv(outputs, csv_writer)
    with open(path + 'temp3.csv', 'w') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter='\t')
        csv_writer.writerow(constantsheader)
        write_constants_to_csv(constants, csv_writer)
    with open(path + 'temp4.csv', 'w') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter='\t')
        csv_writer.writerow(faultsheader)
        write_faults_to_csv(faults, csv_writer)
                        
    #Clean up.
    csv_file_cleanup(path, 'temp1.csv', '_Inputs.csv', True)
    csv_file_cleanup(path, 'temp2.csv', '_Outputs.csv', True)
    csv_file_cleanup(path, 'temp3.csv', '_Constants.csv', True)
    csv_file_cleanup(path, 'temp4.csv', '_Faults.csv', True)
    delete_file(path, 'output.txt')

def write_inputs_to_csv(theList, csvwriter):
    for i in range (len(theList)):
        csvwriter.writerow(
            [
                theList[i].sectionID,
                theList[i].objectID,
                theList[i].name,
                theList[i].vi_name,
                theList[i].datatype,
                theList[i].datatype_abbreviated,
                theList[i].source,
                theList[i].intermediate,
                ]
            )

def write_outputs_to_csv(theList, csvwriter):
    for i in range (len(theList)):
        csvwriter.writerow(
            [
                theList[i].sectionID,
                theList[i].objectID,
                theList[i].name,
                theList[i].vi_name,
                theList[i].datatype,
                theList[i].datatype_abbreviated,
                theList[i].destination,
                ]
            )

def write_constants_to_csv(theList, csvwriter):
    for i in range (len(theList)):
        csvwriter.writerow(
            [
                theList[i].sectionID,
                theList[i].objectID,
                theList[i].name,
                theList[i].vi_name,
                theList[i].datatype,
                theList[i].datatype_abbreviated,
                theList[i].const_type,
                theList[i].units,
                theList[i].defaultvalue,
                theList[i].minvalue,
                theList[i].maxvalue,
                ]
            )

def write_faults_to_csv(theList, csvwriter):
    for i in range (len(theList)):
        csvwriter.writerow(
            [
                theList[i].sectionID,
                theList[i].objectID,
                theList[i].faultname,
                theList[i].vi_name,
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
            print('Created or updated csv archive file: '+ outfile)
    if delete == True:
        delete_file(path, infile)    

def delete_file(path, file):
    os.chdir(path)
    os.remove(file)
    print(path + file + ' has been deleted.')

def is_float(value):
  try:
    float(value)
    return True
  except:
    return False
    
def is_int(value):
    if '.' not in str(value):
        try:
            int(value)
            return True
        except:
            return False
    else:
        return False
 
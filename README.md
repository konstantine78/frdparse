# frdparse
This program parses through a text file that defines requirements for an application.  The goal is to output
a CSV file for archiving/use and a mysql database with tables that reflect all I/O, constants, faults, local variables, and 
data types for an application.

# Files
1. parse.py - This is the main file which parses through text file of requirements and I/O declarations.  It makes use of imported python modules (csv, os, re).  There is a custom module imported, ioparse, that defines a container for any signal (class Signal), as well as custom methods that are called in parse.
2. ioparse.py - Custom module that is imported into parse.py.  It defines class Signal as well as methods defined that are used within ioparse and parse.py.
3. mysql_lib.py - Library of mysql methods for use by theUI.py. 
4. user_defined.py - User defined functionality that is imported into other modules.
5. exportedfile.txt - Source text file of requirements that parse.py parses through.

# Outputs
1. MyIOSignals.csv - Tab-delimited csv archive of all signals, along with attributes/fields for each, organized in table format.
2. iodb - mysql database.

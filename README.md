# frdparse
This program parses through a text file that defines requirements for an application.  
The main file is parse.py which parses through a text file.  The text file identifies all inputs, outputs, constants, conditional statements and results.  

# Files
1. parse.py - This is the main file which parses through text file of requirements and I/O declarations.  It makes use of imported python modules (csv, os, re).  There is a custom module imported, ioparse, that defines a container for any signal (class Signal), as well as custom methods that are called in parse.
2. ioparse.py - Custom module that is imported into parse.py.  It defines class Signal as well as methods defined that are used within ioparse and parse.py.
3. IOExportFile.txt - Source text file of requirements that parse.py parses through.
4. IOExportFileCleanedUp.txt - File exists to store a cleaned up version of IOExportFile.txt, that has all blank lines removed.

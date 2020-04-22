# frdparse
This program parses through a text file that defines requirements for an application.  
The main file is parse.py which parses through a text file.  The text file identifies all inputs, outputs, constants, conditional statements and results.  

# Files
1. parse.py - This is the main file which parses through text file of requirements and I/O declarations.  It makes use of imported python modules (csv, os, re).  There is a custom module imported, ioparse, that defines a container for any signal (class Signal), as well as custom methods that are called in parse.
2. ioparse.py - Custom module that is imported into parse.py.  It defines class Signal as well as methods defined that are used within ioparse and parse.py.
3. exportedfile.txt - Source text file of requirements that parse.py parses through.

# Outputs
1. MyIOSignals.txt - Text-based archive of all signals in source document, along with attributes for each signal.
2. MyIOSignals.csv - Tab-delimited csv archive of all signals, along with attributes/fields for each, organized in table format.
3. output.txt - Temporary text file that is equivalent to exportedfile.txt, with all blank lines removed.  This temporary file is what the parse.py file will loop through for actual signal parsing.

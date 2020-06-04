# frdparse
This program parses through a text file that defines requirements for an application.  The goal is to output
a CSV file for archiving/use and a mysql database with tables that reflect all I/O, constants, faults, local variables, and 
data types for an application.

# Files
1. parse.py - This is the main file which parses through text file of requirements and I/O declarations.  
2. ioparse.py - Custom module that is imported into parse.py.  It's main purpose is to parse a line and return a class instance that is placed into list(s) in parse.
3. mysql_lib.py - Library of mysql methods for use. 
4. userdefined.py - User defined functionality that is imported into other modules.
4. gui_userdefined.py - User defined GUI functionality that is imported into GUI modules.
5. frdparseUI.py - The user-interface file (GUI).
6. exportedfile.txt - Source text file of requirements that parse.py parses through.
7. frdparse.ui - Qt Designer created user interface file that is run through pyuic5 to generate the Ui_MainWindow class, which is parent class to MainWindow.
8. sqlDialog.ui - Qt Designer created user interface file that is run through pyuic5 to generate the Ui_SQLDialog class, which is parent class to SQLDialog.
9. ui_mainwindow.py - Python file that represents the frdparse.ui (generated via pyuic5).  This file should not be altered after generation.
9. ui_mainwinui_sqldialog.py - Python file that represents the sqldialog.ui (generated via pyuic5).  This file should not be altered after generation.
# Outputs
1. _Inputs, _Outputs, _Constants, _Faults - Tab-delimited csv archive of all data, along with attributes/fields for each, organized in table format.
2. 'Database' - any mysql database.  The user interface supports updating the database settings, including the name of it.

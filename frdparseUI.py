from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import parse
import mysql_lib
from gui_userdefined import *
from ui_mainwindow import Ui_MainWindow
from ui_sqldialog import Ui_SQLDialog

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.export_dir.setText('C:/Users/kostas/Documents/GitHub/frdparse/exporttextfiles')
        self.obj_id_prefix.setText('APPSW')
        '''
         These list declarations are not part of the UI.  They are lists of raw data obtained
         from the exported text file.
         1. inputs
         2. ouputs
         3. alignconsts
         4. designconsts
         5. faults
         
         The following are widgets of the UI MainWindow:
         1. export_dir_pb - Pushbutton that opens QFileDialog for setting working directory.
         2. export_dir - Line edit that contains the working directory.
         3. output_terminal - An output terminal that prints all sys.stdout statements.
         4. run_parse_button - Pushbutton to trigger file parser.
         5. obj_id_prefix - Line edit that provides means to manually enter the object ID prefix (e.g., APPSW)
   
        '''        
        self.inputs = list()
        self.outputs = list()
        self.consts = list() 
        self.faults = list()
        '''
        EmittingStream:
        Install a custom output stream by connecting sys.stdout to instance of EmmittingStream.

        '''
        sys.stdout = EmittingStream(textWritten=self.output_terminal_written)
        '''
        Connectors/Signals:
        1. Clicking of export_dir_pb will trigger the exportFileDirButtonClicked method.
        2. Clicking of run_parse_button will trigger the runParseButtonClicked method.
        3. Triggering the Help action from menu will trigger the help_Ui method.
        4. Clicking the sqldb_action_pb will trigger the sqlDatabaseTakeAction method.

        '''
        self.export_dir_pb.clicked.connect(self.exportFileDirButtonClicked)
        self.run_parse_button.clicked.connect(self.runParseButtonClicked)
        self.actionHelp.triggered.connect(self.help_Ui)
        self.sqlDialog_Open_pb.clicked.connect(self.openSQLDialogClicked)
     
    def exportFileDirButtonClicked(self):
        '''
         Method 'exportFileDirButtonClicked':
         Creates a QFileDialog for setting the working directory.  The string for that directory is then
         stored in export_dir.
        
        '''
        directory = str(QtWidgets.QFileDialog.getExistingDirectory())
        self.export_dir.setText('{}'.format(directory))
        print("Source directory has been updated to: "+ directory)

    def runParseButtonClicked(self):
        '''
         Method 'runParseButtonClicked':
         Parses through the export text file.  The method will need to know the file's directory path
         and the object ID prefix within the document.  At the core of this method is the call to parse_export_file.  That
         method will return the various lists needed downstream to create tables in the mysql database.
        
        '''
        if str(self.export_dir.text()).strip() == '' or str(self.obj_id_prefix.text()).strip() == '':
            print('Your directory path and/or Object ID prefix are empty.')
        else:
            try:
                print('Function parse_export_file form parse.py is being run.')
                print('Executing parsing on text file in ' + self.export_dir.text() + '\nObject ID Prefix is: ' + self.obj_id_prefix.text())
                self.inputs, self.ouputs, self.consts, self.faults = parse.parse_export_file(self.export_dir.text(), self.obj_id_prefix.text())
            except ValueError:
                print('Check the export directory path and object ID prefix for an invalid/empty string.')

    def output_terminal_written(self, text):
        '''
         Method 'output_terminal_written':
         Output ANY console output (stdout) to the output terminal text edit widget.
         This method is connected to sys.stdout via custom class EmittingStream.

        '''
        cursor = self.output_terminal.textCursor()
        cursor.movePosition(QtGui.QTextCursor.End)
        cursor.insertText(text)
        self.output_terminal.setTextCursor(cursor)
        self.output_terminal.ensureCursorVisible()

    def openSQLDialogClicked(self):
        i = self.inputs
        o = self.outputs
        c = self.consts
        f = self.faults
        d = SQLDialog(i,o,c,f)
        d.exec_()

    def help_Ui(self):
        print(help(MainWindow.setupUi))
        print(help(MainWindow.exportFileDirButtonClicked))
        print(help(MainWindow.runParseButtonClicked))
        print(help(MainWindow.output_terminal_written))
        print(help(MainWindow.sqlDatabaseTakeAction))
        print(help(parse.parse_export_file))

class SQLDialog(QtWidgets.QDialog, Ui_SQLDialog):
    def __init__(self, inputs, outputs, constants, faults, parent = None):
        super(SQLDialog, self).__init__(parent)
        self.setupUi(self)
        self.inputs = inputs
        self.outputs = outputs
        self.constants = constants
        self.faults = faults
        self.sqlDialog_host.setText('localhost')
        self.sqlDialog_user.setText('root')
        self.sqlDialog_password.setText('password1234')
        self.sqlDialog_DB.setText('NULL')
        self.no_action_SQLdb_pb.setChecked(True)
        self.sql_action_pb.clicked.connect(self.sqlDatabaseTakeAction)

    def sqlDatabaseTakeAction(self):
        '''
         Method 'sqlDatabaseTakeAction':
         Can either create or delete a MySQL database, provided the database's settings are specified
         and the appropriate database action radio button is checked.  This method calls either
         create_database or delete_database, depending on the action.  Create database must check if the lists
         that runParseButtonClicked updated are not empty.
        
        '''
        if str(self.sqlDialog_DB.text()).strip() == '':
                print('The database name is blank.  Please edit.')
        elif self.create_SQLdb_pb.isChecked():
            mysql_lib.create_database(
                self.sqlDialog_host.text(), 
                self.sqlDialog_user.text(), 
                self.sqlDialog_password.text(), 
                self.sqlDialog_DB.text()
                )
            mysql_lib.create_tables(self.sqlDialog_DB.text())
#            mysql_lib.update_input_table(self.sqlDialog_DB.text(), self.inputs)
            self.no_action_SQLdb_pb.setChecked(True) # Prevent inadvertent action taken after creation.
        elif self.delete_SQLdb_pb.isChecked():
            mysql_lib.delete_database(self.sqlDialog_DB.text())
            self.no_action_SQLdb_pb.setChecked(True) # Prevent inadvertent action taken after deletion.
        else: # do nothing.
            self.no_action_SQLdb_pb.setChecked(True)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())

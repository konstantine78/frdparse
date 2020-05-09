from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import parse
import mysql_lib
from user_defined import *

####################### END OF PYUIC5 Generated Python Code#############################################
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(676, 600)
        MainWindow.setStatusTip("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.export_dir = QtWidgets.QLineEdit(self.centralwidget)
        self.export_dir.setGeometry(QtCore.QRect(10, 40, 591, 20))
        self.export_dir.setObjectName("export_dir")
        self.export_dir_pb = QtWidgets.QPushButton(self.centralwidget)
        self.export_dir_pb.setGeometry(QtCore.QRect(610, 40, 51, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.export_dir_pb.setFont(font)
        self.export_dir_pb.setObjectName("export_dir_pb")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(10, 210, 631, 341))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 629, 339))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.output_terminal = QtWidgets.QTextEdit(self.scrollAreaWidgetContents)
        self.output_terminal.setGeometry(QtCore.QRect(10, 10, 601, 321))
        self.output_terminal.setObjectName("output_terminal")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 211, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setUnderline(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 180, 211, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setUnderline(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.run_parse_button = QtWidgets.QPushButton(self.centralwidget)
        self.run_parse_button.setGeometry(QtCore.QRect(30, 130, 71, 31))
        self.run_parse_button.setDefault(False)
        self.run_parse_button.setFlat(False)
        self.run_parse_button.setObjectName("run_parse_button")
        self.obj_id_prefix = QtWidgets.QLineEdit(self.centralwidget)
        self.obj_id_prefix.setGeometry(QtCore.QRect(10, 100, 121, 20))
        self.obj_id_prefix.setObjectName("obj_id_prefix")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 70, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setUnderline(True)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.sqlDialog_Open_pb = QtWidgets.QPushButton(self.centralwidget)
        self.sqlDialog_Open_pb.setGeometry(QtCore.QRect(350, 110, 71, 31))
        self.sqlDialog_Open_pb.setObjectName("sqlDialog_Open_pb")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 676, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionHelp = QtWidgets.QAction(MainWindow)
        self.actionHelp.setObjectName("actionHelp")
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionHelp)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.export_dir_pb.setStatusTip(_translate("MainWindow", "Set the export source directory."))
        self.export_dir_pb.setText(_translate("MainWindow", "..."))
        self.label.setText(_translate("MainWindow", "Set export directory:"))
        self.label_2.setText(_translate("MainWindow", "Output Terminal:"))
        self.run_parse_button.setToolTip(_translate("MainWindow", "Run the Parser"))
        self.run_parse_button.setText(_translate("MainWindow", "PARSE FILE"))
        self.run_parse_button.setShortcut(_translate("MainWindow", "Ctrl+Alt+R"))
        self.label_3.setText(_translate("MainWindow", "Object ID Prefix:"))
        self.sqlDialog_Open_pb.setText(_translate("MainWindow", "SQL Dialog"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave.setStatusTip(_translate("MainWindow", "Save output file"))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionHelp.setText(_translate("MainWindow", "Help"))
        self.actionHelp.setStatusTip(_translate("MainWindow", "Run this for help on tool\'s functions."))
        self.actionHelp.setShortcut(_translate("MainWindow", "Ctrl+Shift+H"))

class Ui_SQLDialog(object):
    def setupUi(self, SQLDialog):
        SQLDialog.setObjectName("SQLDialog")
        SQLDialog.setWindowModality(QtCore.Qt.WindowModal)
        SQLDialog.resize(447, 170)
        self.buttonBox = QtWidgets.QDialogButtonBox(SQLDialog)
        self.buttonBox.setGeometry(QtCore.QRect(120, 130, 171, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.groupBox = QtWidgets.QGroupBox(SQLDialog)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 181, 111))
        self.groupBox.setObjectName("groupBox")
        self.sqlDialog_host = QtWidgets.QLineEdit(self.groupBox)
        self.sqlDialog_host.setGeometry(QtCore.QRect(50, 20, 121, 20))
        self.sqlDialog_host.setObjectName("sqlDialog_host")
        self.sqlDialog_user = QtWidgets.QLineEdit(self.groupBox)
        self.sqlDialog_user.setGeometry(QtCore.QRect(50, 40, 121, 20))
        self.sqlDialog_user.setObjectName("sqlDialog_user")
        self.sqlDialog_password = QtWidgets.QLineEdit(self.groupBox)
        self.sqlDialog_password.setGeometry(QtCore.QRect(50, 60, 121, 20))
        self.sqlDialog_password.setObjectName("sqlDialog_password")
        self.sqlDialog_DB = QtWidgets.QLineEdit(self.groupBox)
        self.sqlDialog_DB.setGeometry(QtCore.QRect(50, 80, 121, 20))
        self.sqlDialog_DB.setObjectName("sqlDialog_DB")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(0, 20, 47, 13))
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(0, 40, 47, 13))
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(0, 60, 51, 20))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(0, 80, 51, 20))
        self.label_4.setObjectName("label_4")
        self.groupBox_2 = QtWidgets.QGroupBox(SQLDialog)
        self.groupBox_2.setGeometry(QtCore.QRect(210, 10, 221, 111))
        self.groupBox_2.setObjectName("groupBox_2")
        self.create_SQLdb_pb = QtWidgets.QRadioButton(self.groupBox_2)
        self.create_SQLdb_pb.setGeometry(QtCore.QRect(10, 20, 111, 17))
        self.create_SQLdb_pb.setObjectName("create_SQLdb_pb")
        self.delete_SQLdb_pb = QtWidgets.QRadioButton(self.groupBox_2)
        self.delete_SQLdb_pb.setGeometry(QtCore.QRect(10, 50, 101, 17))
        self.delete_SQLdb_pb.setObjectName("delete_SQLdb_pb")
        self.no_action_SQLdb_pb = QtWidgets.QRadioButton(self.groupBox_2)
        self.no_action_SQLdb_pb.setGeometry(QtCore.QRect(10, 80, 82, 17))
        self.no_action_SQLdb_pb.setObjectName("no_action_SQLdb_pb")
        self.sql_action_pb = QtWidgets.QPushButton(self.groupBox_2)
        self.sql_action_pb.setGeometry(QtCore.QRect(120, 30, 75, 41))
        self.sql_action_pb.setObjectName("sql_action_pb")

        self.retranslateUi(SQLDialog)
        self.buttonBox.accepted.connect(SQLDialog.accept)
        self.buttonBox.rejected.connect(SQLDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(SQLDialog)

    def retranslateUi(self, SQLDialog):
        _translate = QtCore.QCoreApplication.translate
        SQLDialog.setWindowTitle(_translate("SQLDialog", "Dialog"))
        self.groupBox.setTitle(_translate("SQLDialog", "Database Settings"))
        self.label.setText(_translate("SQLDialog", "host:"))
        self.label_2.setText(_translate("SQLDialog", "user:"))
        self.label_3.setText(_translate("SQLDialog", "password:"))
        self.label_4.setText(_translate("SQLDialog", "database:"))
        self.groupBox_2.setTitle(_translate("SQLDialog", "Database Action"))
        self.create_SQLdb_pb.setText(_translate("SQLDialog", "Create Database"))
        self.delete_SQLdb_pb.setText(_translate("SQLDialog", "Delete Database"))
        self.no_action_SQLdb_pb.setText(_translate("SQLDialog", "No Action"))
        self.sql_action_pb.setText(_translate("SQLDialog", "Take Action"))
####################### END OF PYUIC5 Generated Python Code#############################################

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
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
        self.alignconsts = list() 
        self.designconsts = list() 
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
                self.inputs, self.ouputs, self.alignconsts, self.designconsts, self.faults = parse.parse_export_file(self.export_dir.text(), self.obj_id_prefix.text())
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
        d = SQLDialog(self)
        d.exec()

    def help_Ui(self):
        print(help(MainWindow.setupUi))
        print(help(MainWindow.exportFileDirButtonClicked))
        print(help(MainWindow.runParseButtonClicked))
        print(help(MainWindow.output_terminal_written))
        print(help(MainWindow.sqlDatabaseTakeAction))
        print(help(parse.parse_export_file))

class SQLDialog(QtWidgets.QDialog, Ui_SQLDialog):
    def __init__(self, parent = None):
        super(SQLDialog, self).__init__(parent)
        self.setupUi(self)

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
            mysql_lib.create_database(self.database_name.text())
            self.no_action_SQLdb_pb.setChecked(True) # Prevent inadvertent action taken after creation.
        elif self.delete_SQLdb_pb.isChecked():
            mysql_lib.delete_database(self.database_name.text())
            self.no_action_SQLdb_pb.setChecked(True) # Prevent inadvertent action taken after deletion.
        else: # do nothing.
            self.no_action_SQLdb_pb.setChecked(True)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())

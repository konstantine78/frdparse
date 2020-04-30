# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frdparse.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from user_defined import *
import sys
import parse


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        '''
        ----------------------------------
         These list declarations are not part of the UI.  They are lists of raw data obtained
         from the exported text file.
         1. inputs
         2. ouputs
         3. alignconsts
         4. designconsts
        ----------------------------------        
        '''
        self.inputs = list()
        self.outputs = list()
        self.alignconsts = list() 
        self.designconsts = list() 
        '''
        ----------------------------------
         The following are widgets of the UI MainWindow:
         1. export_dir_pb - Pushbutton that opens QFileDialog for setting working directory.
         2. export_dir - Line edit that contains the working directory.
         3. output_terminal - An output terminal that prints all sys.stdout statements.
         4. run_parse_button - Pushbutton to trigger file parser.
         5. obj_id_prefix - Line edit that provides means to manually enter the object ID prefix (e.g., APPSW)
        ----------------------------------
        '''
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
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 629, 379))
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
        self.run_parse_button.setIcon(QtGui.QIcon("play.png"))
        self.run_parse_button.setIconSize(QtCore.QSize(72,72))
        self.run_parse_button.setGeometry(QtCore.QRect(150, 90, 71, 61))
        self.run_parse_button.setText("")
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
        self.database_name = QtWidgets.QLineEdit(self.centralwidget)
        self.database_name.setGeometry(QtCore.QRect(510, 110, 141, 20))
        self.database_name.setObjectName("database_name")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(360, 80, 141, 91))
        self.groupBox.setObjectName("groupBox")
        self.no_action_SQLdb_pb = QtWidgets.QRadioButton(self.groupBox)
        self.no_action_SQLdb_pb.setGeometry(QtCore.QRect(10, 60, 111, 17))
        self.no_action_SQLdb_pb.setObjectName("no_action_SQLdb_pb")
        self.create_SQLdb_pb = QtWidgets.QRadioButton(self.groupBox)
        self.create_SQLdb_pb.setGeometry(QtCore.QRect(10, 20, 111, 17))
        self.create_SQLdb_pb.setObjectName("create_SQLdb_pb")
        self.delete_SQLdb_pb = QtWidgets.QRadioButton(self.groupBox)
        self.delete_SQLdb_pb.setGeometry(QtCore.QRect(10, 40, 111, 17))
        self.delete_SQLdb_pb.setObjectName("delete_SQLdb_pb")
        self.no_action_SQLdb_pb.setChecked(True)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(510, 90, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setUnderline(True)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
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
        self.menuFile.addAction(self.actionSave)
        self.menubar.addAction(self.menuFile.menuAction())

        # Install a custom output stream by connecting sys.stdout to instance of EmmittingStream.
        sys.stdout = EmittingStream(textWritten=self.output_terminal_written)
        
        # Create signal/connections for custom methods.
        '''
        ----------------------------------
        Connectors in the UI file:
        1. Clicking of export_dir_pb will trigger the exportFileDirButtonClicked method.
        2. Clicking of run_parse_button will trigger the runParseButtonClicked method.
        ----------------------------------
        '''
        self.export_dir_pb.clicked.connect(self.exportFileDirButtonClicked)
        self.run_parse_button.clicked.connect(self.runParseButtonClicked)

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
        self.run_parse_button.setShortcut(_translate("MainWindow", "Ctrl+Alt+R"))
        self.label_3.setText(_translate("MainWindow", "Object ID Prefix:"))
        self.groupBox.setTitle(_translate("MainWindow", "MYSQL Database Action"))
        self.no_action_SQLdb_pb.setText(_translate("MainWindow", "No Action"))
        self.create_SQLdb_pb.setText(_translate("MainWindow", "Create Database"))
        self.delete_SQLdb_pb.setText(_translate("MainWindow", "Delete Database"))
        self.label_4.setText(_translate("MainWindow", "Database Name:"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave.setStatusTip(_translate("MainWindow", "Save output file"))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S"))

    # Custom UI Methods
    def exportFileDirButtonClicked(self):
        '''
        ----------------------------------
         Method 'exportFileDirButtonClicked':
         Creates a QFileDialog for setting the working directory.  The string for that directory is then
         stored in export_dir.
        ----------------------------------
        '''
        directory = str(QtWidgets.QFileDialog.getExistingDirectory())
        self.export_dir.setText('{}'.format(directory))
        print("Source directory has been updated to: "+ directory)

    def runParseButtonClicked(self):
        '''
        ----------------------------------
         Method 'runParseButtonClicked':
         Parses through the export text file.  The function will need to know the file's directory path
         and the object ID prefix within the document.  It returns the various lists needed downstream to
         create tables in the mysql database.
        ----------------------------------
        '''
        if self.export_dir.text() == '' or self.obj_id_prefix.text() == '':
            print('Your directory path and/or Object ID prefix are empty.')
        else:
            try:
                self.inputs = parse.parse_export_file(self.export_dir.text(), self.obj_id_prefix.text())
                print('Function parse_export_file form parse.py is being run.')
                print('Executing parsing on text file in ' + self.export_dir.text() + '\nObject ID Prefix is: ' + self.obj_id_prefix.text())
            except ValueError:
                print('Check the export directory path and object ID prefix for an invalid/empty string.')

    def output_terminal_written(self, text):
        '''
        ----------------------------------
         Method 'output_terminal_written':
         Output ANY console output (stdout) to the output terminal text edit widget.
         This method is connected to sys.stdout via custom class EmittingStream.
        ----------------------------------
        '''
        cursor = self.output_terminal.textCursor()
        cursor.movePosition(QtGui.QTextCursor.End)
        cursor.insertText(text)
        self.output_terminal.setTextCursor(cursor)
        self.output_terminal.ensureCursorVisible()

    def help_Ui(self):
        print(help(Ui_MainWindow.setupUi))
        print(help(Ui_MainWindow.exportFileDirButtonClicked))
        print(help(Ui_MainWindow.runParseButtonClicked))
        print(help(Ui_MainWindow.output_terminal_written))
        print(help(parse.parse_export_file))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

from PyQt5 import QtCore, QtGui, QtWidgets

class EmittingStream(QtCore.QObject):
    '''
    Custom class that defines a stream and reports data written to it with a Qt signal.

    '''
    textWritten = QtCore.pyqtSignal(str)

    def write(self, text):
        self.textWritten.emit(str(text))

from PyQt5 import QtCore, QtGui, QtWidgets

# Custom class that defines a stream and reports data written to it with a Qt signal
class EmittingStream(QtCore.QObject):

    textWritten = QtCore.pyqtSignal(str)

    def write(self, text):
        self.textWritten.emit(str(text))

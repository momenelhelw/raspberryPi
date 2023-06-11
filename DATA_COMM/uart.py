from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from data import Ui_Form

app = QtWidgets.QApplication(sys.argv)
Form = QtWidgets.QWidget()
ui = Ui_Form()
ui.setupUi(Form)
Form.show()





sys.exit(app.exec_())


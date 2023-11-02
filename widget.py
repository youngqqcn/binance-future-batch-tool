# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout

from PySide6.QtGui import QIntValidator,QDoubleValidator

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_Widget


class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)


#        btnMakeLong = QPushButton("long", self)
#        layout = QHBoxLayout()
#        layout.addWidget(btnMakeLong)
#        self.setLayout(layout)

        self.setWindowTitle("合约一键下单工具")
        self.resize(800, 600)

        # multiple validator
        multipleVal = QIntValidator()
        multipleVal.setRange(1, 100)
        self.ui.leMultiples.setValidator(multipleVal)



        # stop loss validator
        stopLossVal = QDoubleValidator()
        stopLossVal.setRange(0, 99.0)
        stopLossVal.setTop(99.0)
        stopLossVal.setDecimals(1)
        self.ui.leStopLossRatio.setValidator(stopLossVal)

        # amount validator
        amountVal =  QDoubleValidator()
        amountVal.setRange(0.0001, 99999999999.9)
        amountVal.setDecimals(4)
        self.ui.leAmount.setValidator(amountVal)


        # make long
        self.ui.btnMakeLong.clicked.connect(lambda: self.makeLongClicked(1))

        # make short
        self.ui.btnMakeShort.clicked.connect(lambda: self.makeShortClicked(1))

        self.ui.btnAddToken.clicked.connect(lambda: self.addToken())

        self.ui.btnDeleteToken.clicked.connect(lambda: self.deleteToken())

        pass



    def makeLongClicked(self, n):
        print("btnMakeLong {0} is Clicked".format(n))

    def makeShortClicked(self, n):
        print("btnMakeShort {0} is Clicked".format(n))


    def addToken(self):
        print('add token')
        pass

    def deleteToken(self):
        print('delete token')
        pass



if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())

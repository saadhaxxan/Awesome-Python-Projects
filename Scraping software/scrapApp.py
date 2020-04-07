from PyQt5 import QtCore, QtGui, QtWidgets
from urllib.request import urlopen
from bs4 import BeautifulSoup

class Ui_Form(object):
    
    	
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(732, 589)
        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setGeometry(QtCore.QRect(30, 50, 671, 491))
        self.textBrowser.setStyleSheet("QTextBrowser{\n"
"\n"
"background:#ffffff\n"
"\n"
"}")
        self.textBrowser.setObjectName("textBrowser")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(174, 552, 411, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.clicked.connect(self.scrapWeb)
        self.pushButton.setStyleSheet("QPushButton{\n"
"\n"
"border: 1px solid gray;\n"
"border-radius : 15px;\n"
"background:qradialgradient(spread:repeat, cx:0.5, cy:0.5, radius:0.077, fx:0.5, fy:0.5, stop:0 rgba(0, 169, 255, 147), stop:0.497326 rgba(0, 0, 0, 147), stop:1 rgba(0, 169, 255, 147))\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"color:white;\n"
"background-color:blue;\n"
"border-radius:15px;\n"
"border-width:0px\n"
"}")
    	
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(30, 10, 671, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("QLineEdit{\n"
"\n"
"background: rgb(255, 255, 255);\n"
"\n"
"\n"
"\n"
"}")
        self.lineEdit.setObjectName("lineEdit")
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def scrapWeb(self):
    	line_edit = self.lineEdit.text()
    	html = urlopen(line_edit).read()
    	bs_obj = BeautifulSoup(html,'lxml')
    	self.textBrowser.append(str(bs_obj)) 

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "Scrap URL"))
        self.lineEdit.setText(_translate("Form", "ENTER URL TO SCRAP"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())


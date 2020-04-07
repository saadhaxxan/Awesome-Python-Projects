from PyQt5 import QtCore, QtGui, QtWidgets
from PIL import Image, ImageDraw, ImageFont
import random
import os
import datetime
import qrcode
import cv2
import sys 
class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(799, 594)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        Form.setFont(font)
        Form.setStyleSheet("QWidget{\n"
"background:rgb(85, 170, 255);\n"
"\n"
"}")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(460, 30, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.clicked.connect(self.capture)
        self.pushButton.setStyleSheet("QPushButton{\n"
"border:3px solid black;\n"
"border-radius:15px;\n"
"background:blue;\n"
"color:white;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border:1px solid gray;\n"
"border-radius:15px;\n"
"background:black;\n"
"color:white;\n"
"}")
        self.pushButton.setObjectName("pushButton")
        
        self.pushButton.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(190, 30, 251, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(70, 150, 201, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(70, 230, 181, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(70, 310, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(70, 390, 171, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(70, 490, 231, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(360, 140, 381, 31))
        self.lineEdit.setStyleSheet("QLineEdit{\n"
"\n"
"background:white;\n"
"}")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(360, 220, 381, 31))
        self.lineEdit_2.setStyleSheet("QLineEdit{\n"
"\n"
"background:white;\n"
"}")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(Form)
        self.lineEdit_3.setGeometry(QtCore.QRect(360, 300, 381, 31))
        self.lineEdit_3.setStyleSheet("QLineEdit{\n"
"\n"
"background:white;\n"
"}")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(Form)
        self.lineEdit_4.setGeometry(QtCore.QRect(360, 390, 381, 31))
        self.lineEdit_4.setStyleSheet("QLineEdit{\n"
"\n"
"background:white;\n"
"}")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(Form)
        self.lineEdit_5.setGeometry(QtCore.QRect(360, 480, 381, 31))
        self.lineEdit_5.setStyleSheet("QLineEdit{\n"
"\n"
"background:white;\n"
"}")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(260, 540, 271, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.clicked.connect(self.generate_idcard)
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"border:3px solid black;\n"
"border-radius:15px;\n"
"background:blue;\n"
"color:white;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border:1px solid gray;\n"
"border-radius:15px;\n"
"background:black;\n"
"color:white;\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def capture(self):

        camera = cv2.VideoCapture(0)
        while True:
            return_value,image = camera.read()
            image= cv2.flip(image,1)
    #gray = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
            cv2.imshow('image',image)
            if cv2.waitKey(1)==13:
                height , width = image.shape[:2]
                start_row,start_col = int(height*.25), int(width*.25)
                end_row,end_col = int(height*.80), int(width*.80)
                cropped_img = image[start_row:end_row,start_col:end_col]
                cv2.imwrite('person.jpg',cropped_img)
                break
        camera.release()
        cv2.destroyAllWindows()


    def generate_idcard(self):
        # Generating Blank White Image
        image = Image.new('RGB', (1000,900), (255, 255, 255))
        draw = ImageDraw.Draw(image)
        font = ImageFont.truetype('arial.ttf', size=45)


        date = datetime.datetime.now() #getting time and date at the runtime

        (x, y) = (50, 50)
        message = self.lineEdit.text()
        company=message
        color = 'rgb(0, 0, 0)'
        font = ImageFont.truetype('arial.ttf', size=80)
        draw.text((x, y), message, fill=color, font=font)



        #generating ID NO randomly You can also ask user to enter 
        (x, y) = (50, 350)
        id_no = random.randint(1000000,9000000)
        message = str('ID '+str(id_no))
        font = ImageFont.truetype('arial.ttf', size=60)
        color = 'rgb(255, 0, 0)' # color 
        draw.text((x,y),message ,fill=color,font=font)


        # Asking user Full name
        (x, y) = (50, 250)
        message = self.lineEdit_2.text()
        name=message
        color = 'rgb(0, 0, 0)' # black color
        font = ImageFont.truetype('arial.ttf', size=45)
        draw.text((x, y), message, fill=color, font=font)




        

        # Asking about user gender
        (x, y) = (50, 550)
        message = self.lineEdit_3.text()
        color = 'rgb(0, 0, 0)' # black color 
        draw.text((x, y), message, fill=color, font=font)


        # Asking User about his phone number
        (x, y) = (50, 650)
        message = self.lineEdit_5.text()
        temp=message
        color = 'rgb(0, 0, 0)' # black color 
        draw.text((x, y), message, fill=color, font=font)



        # Asking user about his Adress
        (x, y) = (50, 750)
        message = self.lineEdit_4.text()
        color = 'rgb(0, 0, 0)' # black color 
        draw.text((x, y), message, fill=color, font=font)




        # save the edited image
 
        image.save(str(name)+'.png')


        # pasting person image taken by camera on card image
        card_image=Image.open(name+'.png')
        person_image= Image.open('person.jpg','r')
        card_image.paste(person_image,(600,75))
        card_image.save("card.jpg")
        img = qrcode.make(str(company)+str(id_no))   # this info. is added in QR code, also add other things
        img.save(str(id_no)+'.bmp')

        til = Image.open('card.jpg')
        im = Image.open(str(id_no)+'.bmp') #25x25
        til.paste(im,(600,400))
        til.save(name+'.png')
        self.hide()



    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "Capture Image"))
        self.label.setText(_translate("Form", "Capture Your Image "))
        self.label_2.setText(_translate("Form", "Your Company Name"))
        self.label_3.setText(_translate("Form", "Your Full Name"))
        self.label_4.setText(_translate("Form", "Your Gender"))
        self.label_5.setText(_translate("Form", "Your Current Adress"))
        self.label_6.setText(_translate("Form", "Your Active Phone Number"))
        self.pushButton_2.setText(_translate("Form", "Generate Id Card"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

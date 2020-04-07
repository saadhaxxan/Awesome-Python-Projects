from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
import MySQLdb
from PyQt5.uic import loadUiType
import datetime
from xlrd import *
from xlsxwriter import *

ui,_ = loadUiType('library.ui')

class MainApp(QMainWindow , ui):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.Handel_UI_Changes()
        self.Handel_Buttons()
        self.Dark_Orange_Theme()

        self.Show_Author()
        self.Show_Category()
        self.Show_Publisher()


        self.Show_Category_Combobox()
        self.Show_Author_Combobox()
        self.Show_Publisher_Combobox()

        self.Show_All_Clients()
        self.Show_All_Books()

        self.Show_All_Operations()


    def Handel_UI_Changes(self):
        self.Hiding_Themes()
        self.tabWidget.tabBar().setVisible(False)


    def Handel_Buttons(self):
        self.pushButton_5.clicked.connect(self.Show_Themes)
        self.pushButton_17.clicked.connect(self.Hiding_Themes)

        self.pushButton.clicked.connect(self.Open_Day_To_Day_Tab)
        self.pushButton_2.clicked.connect(self.Open_Books_Tab)
        self.pushButton_26.clicked.connect(self.Open_CLients_Tab)
        self.pushButton_3.clicked.connect(self.Open_Users_Tab)
        self.pushButton_4.clicked.connect(self.Open_Settings_Tab)

        self.pushButton_7.clicked.connect(self.Add_New_Book)
        self.pushButton_9.clicked.connect(self.Search_Books)
        self.pushButton_8.clicked.connect(self.Edit_Books)
        self.pushButton_10.clicked.connect(self.Delete_Books)

        self.pushButton_14.clicked.connect(self.Add_Category)
        self.pushButton_15.clicked.connect(self.Add_Author)
        self.pushButton_16.clicked.connect(self.Add_Publisher)

        self.pushButton_11.clicked.connect(self.Add_New_User)
        self.pushButton_13.clicked.connect(self.Edit_User)

        self.pushButton_19.clicked.connect(self.Dark_Orange_Theme)
        self.pushButton_18.clicked.connect(self.Dark_Blue_Theme)
        self.pushButton_21.clicked.connect(self.Dark_Gray_Theme)
        self.pushButton_20.clicked.connect(self.QDark_Theme)

        self.pushButton_22.clicked.connect(self.Add_New_Client)
        self.pushButton_24.clicked.connect(self.Search_Client)
        self.pushButton_23.clicked.connect(self.Edit_Client)
        self.pushButton_25.clicked.connect(self.Delete_Client)

        self.pushButton_6.clicked.connect(self.Handel_Day_Operations)

        self.pushButton_29.clicked.connect(self.Export_Day_Operations)
        self.pushButton_27.clicked.connect(self.Export_Books)
        self.pushButton_28.clicked.connect(self.Export_Clients)



    def Show_Themes(self):
        self.groupBox_3.show()


    def Hiding_Themes(self):
        self.groupBox_3.hide()

    ########################################
    ######### opening tabs #################
    def Open_Day_To_Day_Tab(self):
        self.tabWidget.setCurrentIndex(0)

    def Open_Books_Tab(self):
        self.tabWidget.setCurrentIndex(1)

    def Open_CLients_Tab(self):
        self.tabWidget.setCurrentIndex(2)

    def Open_Users_Tab(self):
        self.tabWidget.setCurrentIndex(3)

    def Open_Settings_Tab(self):
        self.tabWidget.setCurrentIndex(4)


    ########################################
    ######### Day Operations #################
    def Handel_Day_Operations(self):
        book_title = self.lineEdit.text()
        client_name = self.lineEdit_29.text()
        type = self.comboBox.currentText()
        days_number = self.comboBox_2.currentIndex() + 1
        today_date = datetime.date.today()
        to_date = today_date + datetime.timedelta(days=days_number)

        print(today_date)
        print(to_date)

        self.db = MySQLdb.connect(host='localhost',port=8080,user='root',password='saadhaxxan',db='library')
        
        self.cur = self.db.cursor()

        self.cur.execute('''
            INSERT INTO dayoperations(book_name, client, type , days , date   )
            VALUES (%s , %s , %s, %s , %s , %s)
        ''' , (book_title ,client_name, type , days_number , today_date ))

        self.db.commit()
        self.statusBar().showMessage('New Operation Added')

        self.Show_All_Operations()



    def Show_All_Operations(self):
        self.db = MySQLdb.connect(host='localhost',port=8080,user='root',password='saadhaxxan',db='library')
        self.cur = self.db.cursor()

        self.cur.execute(''' SELECT book_name , client , type , date  FROM dayoperations''')

        data = self.cur.fetchall()

        print(data)

        self.tableWidget.setRowCount(0)
        self.tableWidget.insertRow(0)
        for row , form in enumerate(data):
            for column , item in enumerate(form):
                self.tableWidget.setItem(row , column , QTableWidgetItem(str(item)))
                column += 1

            row_position = self.tableWidget.rowCount()
            self.tableWidget.insertRow(row_position)



    ########################################
    ######### Books #################

    def Show_All_Books(self):
        self.db = MySQLdb.connect(host='localhost',port=8080,user='root',password='saadhaxxan',db='library')
        self.cur = self.db.cursor()

        self.cur.execute(''' SELECT book_code,book_name,book_description,book_category,book_author,book_publisher,book_price FROM book''')
        data = self.cur.fetchall()

        self.tableWidget_5.setRowCount(0)
        self.tableWidget_5.insertRow(0)

        for row, form in enumerate(data):
            for column, item in enumerate(form):
                self.tableWidget_5.setItem(row, column, QTableWidgetItem(str(item)))
                column += 1

            row_position = self.tableWidget_5.rowCount()
            self.tableWidget_5.insertRow(row_position)

        self.db.close()


    def Add_New_Book(self):

        self.db = MySQLdb.connect(host='localhost',port=8080,user='root',password='saadhaxxan',db='library')
        self.cur = self.db.cursor()

        book_title = self.lineEdit_2.text()
        book_description = self.textEdit.toPlainText()
        book_code = self.lineEdit_3.text()
        book_category = self.comboBox_3.currentText()
        book_author = self.comboBox_4.currentText()
        book_publisher = self.comboBox_5.currentText()
        book_price = self.lineEdit_4.text()

        self.cur.execute('''
            INSERT INTO book(book_name,book_description,book_code,book_category,book_author,book_publisher,book_price)
            VALUES (%s , %s , %s , %s , %s , %s , %s)
        ''' ,(book_title , book_description , book_code , book_category , book_author , book_publisher , book_price))

        self.db.commit()
        self.statusBar().showMessage('New Book Added')

        self.lineEdit_2.setText('')
        self.textEdit.setPlainText('')
        self.lineEdit_3.setText('')
        self.comboBox_3.setCurrentIndex(0)
        self.comboBox_4.setCurrentIndex(0)
        self.comboBox_5.setCurrentIndex(0)
        self.lineEdit_4.setText('')
        self.Show_All_Books()




    def Search_Books(self):

        self.db = MySQLdb.connect(host='localhost',port=8080,user='root',password='saadhaxxan',db='library')
        self.cur = self.db.cursor()

        book_title = self.lineEdit_5.text()

        sql = ''' SELECT * FROM book WHERE book_name = %s'''
        self.cur.execute(sql , [(book_title)])

        data = self.cur.fetchone()

        print(data)
        self.lineEdit_8.setText(data[1])
        self.textEdit_2.setPlainText(data[2])
        self.lineEdit_7.setText(data[3])
        self.comboBox_7.setCurrentText(data[4])
        self.comboBox_8.setCurrentText(data[5])
        self.comboBox_6.setCurrentText(data[6])
        self.lineEdit_6.setText(str(data[7]))





    def Edit_Books(self):
        self.db = MySQLdb.connect(host='localhost',port=8080,user='root',password='saadhaxxan',db='library')
        self.cur = self.db.cursor()

        book_title = self.lineEdit_8.text()
        book_description = self.textEdit_2.toPlainText()
        book_code = self.lineEdit_7.text()
        book_category = self.comboBox_7.currentText()
        book_author = self.comboBox_8.currentText()
        book_publisher = self.comboBox_6.currentText()
        book_price = self.lineEdit_6.text()


        search_book_title = self.lineEdit_5.text()

        self.cur.execute('''
            UPDATE book SET book_name=%s ,book_description=%s ,book_code=%s ,book_category=%s ,book_author=%s ,book_publisher=%s ,book_price=%s WHERE book_name = %s            
        ''', (book_title,book_description,book_code,book_category,book_author,book_publisher , book_price , search_book_title))

        self.db.commit()
        self.statusBar().showMessage('book updated')
        self.Show_All_Books()


    def Delete_Books(self):
        self.db = MySQLdb.connect(host='localhost',port=8080,user='root',password='saadhaxxan',db='library')
        self.cur = self.db.cursor()

        book_title = self.lineEdit_5.text()

        warning = QMessageBox.warning(self , 'Delete Book' , "are you sure you want to delete this book" , QMessageBox.Yes | QMessageBox.No)
        if warning == QMessageBox.Yes :
            sql = ''' DELETE FROM book WHERE book_name = %s '''
            self.cur.execute(sql , [(book_title)])
            self.db.commit()
            self.statusBar().showMessage('Book Deleted')

            self.Show_All_Books

    ########################################
    ######### Clients #################
    def Show_All_Clients(self):
        self.db = MySQLdb.connect(host='localhost',port=8080,user='root',password='saadhaxxan',db='library')
        self.cur = self.db.cursor()

        self.cur.execute(''' SELECT client_name , client_email ,client_nationalid FROM clients ''')
        data = self.cur.fetchall()

        print(data)
        self.tableWidget_6.setRowCount(0)
        self.tableWidget_6.insertRow(0)

        for row, form in enumerate(data):
            for column, item in enumerate(form):
                self.tableWidget_6.setItem(row, column, QTableWidgetItem(str(item)))
                column += 1

            row_position = self.tableWidget_6.rowCount()
            self.tableWidget_6.insertRow(row_position)

        self.db.close()


    def Add_New_Client(self):
        client_name = self.lineEdit_22.text()
        client_email = self.lineEdit_23.text()
        client_nationalid = self.lineEdit_24.text()

        self.db = MySQLdb.connect(host='localhost',port=8080,user='root',password='saadhaxxan',db='library')
        self.cur = self.db.cursor()

        self.cur.execute('''
            INSERT INTO clients(client_name , client_email , client_nationalid)
            VALUES (%s , %s , %s)
        ''' , (client_name , client_email , client_nationalid))
        self.db.commit()
        self.db.close()
        self.statusBar().showMessage('New CLient Added')
        self.Show_All_Clients()


    def Search_Client(self):
        client_national_id = self.lineEdit_25.text()
        self.db = MySQLdb.connect(host='localhost',port=8080,user='root',password='saadhaxxan',db='library')
        self.cur = self.db.cursor()

        sql = ''' SELECT * FROM clients WHERE client_nationalid = %s '''
        self.cur.execute(sql , [(client_national_id)])
        data = self.cur.fetchone()
        print(data)

        self.lineEdit_28.setText(data[1])
        self.lineEdit_27.setText(data[2])
        self.lineEdit_26.setText(data[3])


    def Edit_Client(self):
        client_original_national_id = self.lineEdit_25.text()
        client_name = self.lineEdit_28.text()
        client_email = self.lineEdit_27.text()
        client_national_id = self.lineEdit_26.text()

        self.db = MySQLdb.connect(host='localhost',port=8080,user='root',password='saadhaxxan',db='library')
        self.cur = self.db.cursor()

        self.cur.execute('''
            UPDATE clients SET client_name = %s , client_email = %s , client_nationalid = %s WHERE client_nationalid = %s
        ''' , (client_name , client_email , client_national_id , client_original_national_id))
        self.db.commit()
        self.db.close()
        self.statusBar().showMessage('CLient Data Updated ')
        self.Show_All_Clients()


    def Delete_Client(self):
        client_original_national_id = self.lineEdit_25.text()


        warning_message = QMessageBox.warning(self , "Delete CLient" , "are you sure you want to delete this client" , QMessageBox.Yes | QMessageBox.No)

        if warning_message == QMessageBox.Yes :
            self.db = MySQLdb.connect(host='localhost',port=8080,user='root',password='saadhaxxan',db='library')
            self.cur = self.db.cursor()

            sql = ''' DELETE FROM clients WHERE client_nationalid = %s '''
            self.cur.execute(sql , [(client_original_national_id)])

            self.db.commit()
            self.db.close()
            self.statusBar().showMessage('CLient Deleted ')
            self.Show_All_Clients()


    ########################################
    ######### users #################

    def Add_New_User(self):
        self.db = MySQLdb.connect(host='localhost',port=8080,user='root',password='saadhaxxan',db='library')
        
        self.cur = self.db.cursor()

        username = self.lineEdit_9.text()
        email = self.lineEdit_10.text()
        password = self.lineEdit_11.text()
        password2 = self.lineEdit_12.text()

        if password == password2 :
            self.cur.execute(''' 
                INSERT INTO users(user_name , user_email , user_password)
                VALUES (%s , %s , %s)
            ''' , (username , email , password))

            self.db.commit()
            self.statusBar().showMessage('New User Added')

        else:
            self.label_30.setText('please add a valid password twice')



    def Edit_User(self):

        username = self.lineEdit_17.text()
        email = self.lineEdit_15.text()
        password = self.lineEdit_16.text()
        password2 = self.lineEdit_18.text()

        original_name = self.lineEdit_14.text()

        if password == password2 :
            self.db = MySQLdb.connect(host='localhost',port=8080,user='root',password='saadhaxxan',db='library')
        
            self.cur = self.db.cursor()

            print(username)
            print(email)
            print(password)

            self.cur.execute('''
                UPDATE users SET user_name=%s , user_email=%s , user_password=%s WHERE user_name=%s
            ''', (username , email , password , original_name))

            self.db.commit()
            self.statusBar().showMessage('User Data Updated Successfully')

        else:
            print('make sure you entered you password correctly')


   ########################################
    ######### settings #################
    def Add_Category(self):
        self.db = MySQLdb.connect(host='localhost',port=8080,user='root',password='saadhaxxan',db='library')
        
        self.cur = self.db.cursor()

        category_name = self.lineEdit_19.text()

        self.cur.execute('''
            INSERT INTO category (category_name) VALUES (%s)
        ''' , (category_name,))
        self.db.commit()
        self.statusBar().showMessage('New Category Addedd ')
        self.lineEdit_19.setText('')
        self.Show_Category()
        self.Show_Category_Combobox()



    def Show_Category(self):
        self.db = MySQLdb.connect(host='localhost',port=8080,user='root',password='saadhaxxan',db='library')
        
        self.cur = self.db.cursor()

        self.cur.execute(''' SELECT category_name FROM category''')
        data = self.cur.fetchall()

        if data :
            self.tableWidget_2.setRowCount(0)
            self.tableWidget_2.insertRow(0)
            for row , form in enumerate(data):
                for column , item in enumerate(form) :
                    self.tableWidget_2.setItem(row , column , QTableWidgetItem(str(item)))
                    column += 1

                row_position = self.tableWidget_2.rowCount()
                self.tableWidget_2.insertRow(row_position)



    def Add_Author(self):
        self.db = MySQLdb.connect(host='localhost',port=8080,user='root',password='saadhaxxan',db='library')
        
        self.cur = self.db.cursor()

        author_name = self.lineEdit_20.text()
        self.cur.execute('''
            INSERT INTO authors (author_name) VALUES (%s)
        ''' , (author_name,))
        self.db.commit()
        self.lineEdit_20.setText('')
        self.statusBar().showMessage('New Author Addedd ')
        self.Show_Author()
        self.Show_Author_Combobox()


    def Show_Author(self):
        self.db = MySQLdb.connect(host='localhost',port=8080,user='root',password='saadhaxxan',db='library')
        
        self.cur = self.db.cursor()

        self.cur.execute(''' SELECT author_name FROM authors''')
        data = self.cur.fetchall()


        if data:
            self.tableWidget_3.setRowCount(0)
            self.tableWidget_3.insertRow(0)
            for row, form in enumerate(data):
                for column, item in enumerate(form):
                    self.tableWidget_3.setItem(row, column, QTableWidgetItem(str(item)))
                    column += 1

                row_position = self.tableWidget_3.rowCount()
                self.tableWidget_3.insertRow(row_position)


    def Add_Publisher(self):
        self.db = MySQLdb.connect(host='localhost',port=8080,user='root',password='saadhaxxan',db='library')
        
        self.cur = self.db.cursor()

        publisher_name = self.lineEdit_21.text()
        self.cur.execute('''
            INSERT INTO publisher (publisher_name) VALUES (%s)
        ''' , (publisher_name,))

        self.db.commit()
        self.lineEdit_21.setText('')
        self.statusBar().showMessage('New Publisher Addedd ')
        self.Show_Publisher()
        self.Show_Publisher_Combobox()


    def Show_Publisher(self):
        self.db = MySQLdb.connect(host='localhost',port=8080,user='root',password='saadhaxxan',db='library')
        
        self.cur = self.db.cursor()

        self.cur.execute(''' SELECT publisher_name FROM publisher''')
        data = self.cur.fetchall()


        if data:
            self.tableWidget_4.setRowCount(0)
            self.tableWidget_4.insertRow(0)
            for row, form in enumerate(data):
                for column, item in enumerate(form):
                    self.tableWidget_4.setItem(row, column, QTableWidgetItem(str(item)))
                    column += 1

                row_position = self.tableWidget_4.rowCount()
                self.tableWidget_4.insertRow(row_position)


   ########################################
    ######### show settings data in UI #################
    def Show_Category_Combobox(self):
        self.db = MySQLdb.connect(host='localhost',port=8080,user='root',password='saadhaxxan',db='library')
        
        self.cur = self.db.cursor()

        self.cur.execute(''' SELECT category_name FROM category ''')
        data = self.cur.fetchall()

        self.comboBox_3.clear()
        for category in data :
            self.comboBox_3.addItem(category[0])
            self.comboBox_7.addItem(category[0])



    def Show_Author_Combobox(self):
        self.db = MySQLdb.connect(host='localhost',port=8080,user='root',password='saadhaxxan',db='library')
        
        self.cur = self.db.cursor()

        self.cur.execute(''' SELECT author_name FROM authors''')
        data = self.cur.fetchall()

        self.comboBox_4.clear()
        for author in data :
            self.comboBox_4.addItem(author[0])
            self.comboBox_8.addItem(author[0])


    def Show_Publisher_Combobox(self):
        self.db = MySQLdb.connect(host='localhost',port=8080,user='root',password='saadhaxxan',db='library')
        
        self.cur = self.db.cursor()

        self.cur.execute(''' SELECT publisher_name FROM publisher''')
        data = self.cur.fetchall()

        self.comboBox_5.clear()
        for publisher in data :
            self.comboBox_5.addItem(publisher[0])
            self.comboBox_6.addItem(publisher[0])

    ########################################
    ######### Export Data #################
    def Export_Day_Operations(self):
        self.db = MySQLdb.connect(host='localhost',port=8080,user='root',password='saadhaxxan',db='library')
        
        self.cur = self.db.cursor()

        self.cur.execute(''' 
            SELECT book_name , client , type , date , to_date FROM dayoperations
        ''')

        data = self.cur.fetchall()
        wb = Workbook('day_operations.xlsx')
        sheet1  = wb.add_worksheet()

        sheet1.write(0,0,'book title')
        sheet1.write(0,1,'cliant name')
        sheet1.write(0,2,'type')
        sheet1.write(0,3,'from - date')
        sheet1.write(0,4,'to - date')


        row_number = 1
        for row in data :
            column_number = 0
            for item in row :
                sheet1.write(row_number , column_number , str(item))
                column_number += 1
            row_number += 1

        wb.close()
        self.statusBar().showMessage('Report Created Successfully')



    def Export_Books(self):
        self.db = MySQLdb.connect(host='localhost',port=8080,user='root',password='saadhaxxan',db='library')
        
        self.cur = self.db.cursor()

        self.cur.execute(''' SELECT book_code,book_name,book_description,book_category,book_author,book_publisher,book_price FROM book''')
        data = self.cur.fetchall()

        wb = Workbook('all_books.xlsx')
        sheet1 = wb.add_worksheet()

        sheet1.write(0,0 , 'Book Code')
        sheet1.write(0,1 , 'Book Name')
        sheet1.write(0,2 , 'Book Description')
        sheet1.write(0,3 , 'Book Category')
        sheet1.write(0,4 , 'Book Author')
        sheet1.write(0,5 , 'Book publisher')
        sheet1.write(0,6 , 'Book Price')


        row_number = 1
        for row in data :
            column_number = 0
            for item in row :
                sheet1.write(row_number , column_number , str(item))
                column_number += 1
            row_number += 1

        wb.close()
        self.statusBar().showMessage('Book Report Created Successfully')



    def Export_Clients(self):
        self.db = MySQLdb.connect(host='localhost',port=8080,user='root',password='saadhaxxan',db='library')
        
        self.cur = self.db.cursor()

        self.cur.execute(''' SELECT client_name , client_email ,client_nationalid FROM clients ''')
        data = self.cur.fetchall()

        wb = Workbook('all_CLients.xlsx')
        sheet1 = wb.add_worksheet()

        sheet1.write(0,0 , 'Client Name')
        sheet1.write(0,1 , 'CLient Email')
        sheet1.write(0,2 , 'CLient NationalID')


        row_number = 1
        for row in data :
            column_number = 0
            for item in row :
                sheet1.write(row_number , column_number , str(item))
                column_number += 1
            row_number += 1

        wb.close()
        self.statusBar().showMessage('CLients Report Created Successfully')




   ########################################
    #########  UI Themes #################

    def Dark_Blue_Theme(self):
        style = open('themes/darkblue.css' , 'r')
        style = style.read()
        self.setStyleSheet(style)

    def Dark_Gray_Theme(self):
        style = open('themes/darkgray.css' , 'r')
        style = style.read()
        self.setStyleSheet(style)

    def Dark_Orange_Theme(self):
        style = open('themes/darkorange.css' , 'r')
        style = style.read()
        self.setStyleSheet(style)

    def QDark_Theme(self):
        style = open('themes/qdark.css' , 'r')
        style = style.read()
        self.setStyleSheet(style)



def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()

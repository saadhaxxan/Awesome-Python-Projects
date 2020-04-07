import cv2
import numpy as np
import pyzbar.pyzbar as pyzbar
import base64
import sys
import time
from datetime import datetime
import xlwt 
from xlwt import Workbook
 
cap = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_PLAIN

fob=open(datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p")
+'.txt','w+')

names=[]
def enterData(z):
    if z in names:
        pass
    else:
        names.append(z)
        z=''.join(str(z))
        fob.write(z+'\n')
    return names

print('Reading...')
def checkData(data):
    try:
        data=str(base64.b64decode(data).decode())
    except(TypeError):
        print('Invalid ID !!!')
        return
    if data in names:
        print('Already Present')
    else:
        print('\n'+str(len(names)+1)+'\n'+data)
        enterData(data)
    cv2.putText(frame, str(base64.b64decode(obj.data)), (50, 50), font, 2,
                (255, 0, 0), 3)
    
while True:
    _, frame = cap.read()
    frame= cv2.flip(frame,1)
    decodedObjects = pyzbar.decode(frame)
    for obj in decodedObjects:
        checkData(obj.data)
        #print("Data", base64.b64decode(obj.data))
        #enterData(base64.b64decode(obj.data))
        #print(len(names))
        #sys.stdout.write('\r'+'Reading...'+str(len(names))+'\t'+str(base64.b64decode(obj.data)))
        #sys.stdout.flush()
        time.sleep(1)
       
    cv2.imshow("Frame", frame)

    if cv2.waitKey(1) == 13:
        cv2.destroyAllWindows()
        break
    
fob.close()


d_date = datetime.datetime.now()
reg_format_date = d_date.strftime("%d-%m-%Y %I:%M:%S %p")
reg_format_date=reg_format_date.replace(':',' ')


def writeExcel(names,reg_format_date):

    wb = Workbook()
    
    sheet1 = wb.add_sheet('Sheet 1')
    for i in range(0,len(names)):
        sheet1.write(i, 1, names[i]) 

    wb.save(reg_format_date+'.xls')
writeExcel(names,reg_format_date)

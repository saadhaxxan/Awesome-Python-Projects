import random
import string
import datetime
import os
import ctypes
os.system("title Secure Password Generator")
os.system('color 0a')
d_date = datetime.datetime.now()
reg_format_date = d_date.strftime("  %d-%m-%Y\t\t\t\t\t  Secure Password Generator\t\t\t\t  %I:%M:%S %p")
print ('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
print (reg_format_date)
print ('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
num=['1','2','3','4','5','6','7','8','9','0']
upper=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
lower=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
specialchar='`~!@#$%^&*()_+-=[]{}|/;:,<.>?'
specialchar=list(specialchar)
allchar=upper+lower+specialchar
n=(input('\n\nEnter length of your password: '))
password=[]

def simple(n):          #for simple password.
    for i in range(0,n):
        password.append(random.choice(upper+lower+num))
def hard(n):
    for i in range(0,n):    #for complex password
        password.append(random.choice(allchar))

def choice(n):
    z=eval(input('Press 1 for simple password\nPress 2 for complex password\n>'))
    if z==1:
        simple(n)
    if z==2:
        hard(n)
    elif z>2:
        print('Wrong input')
choice(n)
password=''.join(password)

if len(password)>0:
    print(('Your generated password is:\n'+password))
n=input('\n\n\nEnter Filename to save it: ')
fob=open(n+'.txt','w+')
fob.write('Your generated password is: \n\n')
fob.write(password)
fob.close()
ctypes.windll.user32.MessageBoxA(0,"Your Generated Password save successfully in a text file "+n+".txt","Message",0)

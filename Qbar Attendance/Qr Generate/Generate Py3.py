from MyQR import myqr
import os
import base64

f=open('names.txt','r')
lines = f.read().split("\n")
print (lines)


for i in range(0,len(lines)):
    data=lines[i].encode('utf-8')
    name=str(base64.b64encode(data).decode())
    print(name)
    
    
    version, level, qr_name = myqr.run(
    str(name),
    version = 1,
    level = 'H',
    picture = 'a.jpg',
    colorized = True,
    contrast = 1.0,
    brightness = 1.0,
    save_name = str(lines[i]+'.bmp'),
    save_dir = os.getcwd()
    )

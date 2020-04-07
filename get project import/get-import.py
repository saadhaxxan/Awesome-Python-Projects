from os import walk

def getFileName(name):
    f=open(name,'r+')
    lines = f.read().split("\n")

    data=[]
    for i in range(0,len(lines)):
        #this program also take this line because of import
        if 'import' in lines[i]:
            if 'from' in lines[i]:
                temp=lines[i].split(' ')
                data.append(temp[1])

            else:
                temp=lines[i].split(' ')
                data.append(temp[-1])
            
        #print(lines[i])

    #print('Imported modules are: ',data)
    print(data)
    return data



f = []
for (dirpath, dirnames, filenames) in walk("."):
    f.extend(filenames)
    break
print(f)

modulesName=[]

fileWrite=open('yourmodules.txt','w+')

def addin(data):
    for i in range(0,len(data)):
        if ',' in data[i]:
            temp=data[i].split(',')
            for i in range(0,len(temp)):
                modulesName.append(temp[i])
                fileWrite.write(temp[i]+'\n')
                
        else:
            modulesName.append(data[i])
            fileWrite.write(data[i]+'\n')

for i in range(0,len(f)):
    
    try:
        print(f[i])
        fileWrite.write(f[i]+'\n')
        data=getFileName(f[i])
        addin(data)
        fileWrite.write('\n')
    except:
        fileWrite.write(f[i]+'\n\n')        
        print('Cannot Process File !!!')
        pass

fileWrite.close()

#if file name is present then do not get fro modules

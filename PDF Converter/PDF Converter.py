from tkinter import *
import tkinter, tkinter.constants, tkinter.filedialog
import tkinter.filedialog as filedialog 
from tkinter import messagebox
import tkinter as tk
import tkinter.ttk as ttk
import random
from PyPDF2 import PdfFileWriter, PdfFileReader
import PyPDF2
import img2pdf 
from PIL import Image 
import os


def pdfconvert(pdf_path,img_path):
    image = Image.open(img_path) 
    pdf_bytes = img2pdf.convert(image.filename) 
    file = open(pdf_path, "wb") 
    file.write(pdf_bytes) 
    image.close() 
    file.close()

 
#pdf get file functionof btn
def get_img_func():
        root.img_file_name = tkinter.filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("JPG files","*.JPG"),("PNG files","*.PNG"),("all files","*.*")))
        tempname1 = (root.img_file_name).split('/')[-1]
        get_file_button.config(text = tempname1,state="disabled")
        return root.img_file_name

def convert():
        print((root.img_file_name))
        root.location = tkinter.filedialog.asksaveasfilename(initialdir = "/",title = "Select file",filetypes = (("PDF files","*.PDF"),("all files","*.*")))
        root.location=root.location+'.pdf'
       
        tempname=root.location.split('/')[-1]
        convert_button.config(text = tempname,state="disabled")        
        print(tempname)
        loc=str(root.location)
        name=str(root.img_file_name)
        print(loc)
        print(name)
        pdfconvert(loc,name) 
        messagebox.showinfo('Message', 'Your PDF file '+tempname+' is Saved Successfully')







def splitpdf(inpdf,outpdf,name):
        inputpdf = PdfFileReader(open(inpdf, "rb"))
        for i in range(inputpdf.numPages):
            output = PdfFileWriter()
            output.addPage(inputpdf.getPage(i))
            with open(outpdf+"/"+name+" page %s.pdf"%(i+1), "wb") as outputStream:
                output.write(outputStream)

def get_Split_file_func():
        root.get_split_filename = tkinter.filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("PDF files","*.PDF"),("all files","*.*")))
        tempname1 = (root.get_split_filename).split('/')[-1]
        split_file_get_button.config(text = tempname1,state="disabled")
        return root.get_split_filename

def split():
        print((root.get_split_filename))
        root.location = filedialog.askdirectory()
        print((root.location))

        tempname=os.path.splitext(os.path.basename(root.get_split_filename))[0]
        os.chdir(root.location)
        try:
                os.mkdir(tempname)
        except:
                pass
        spit_main_button.config(text = tempname,state="disabled")        
        root.location=root.location+'/'+tempname
        print(tempname)
        splitpdf(root.get_split_filename,root.location,tempname)
        t = (root.get_split_filename).split('/')[-1]
        messagebox.showinfo('Message', 'Your PDF file '+t+' is Splited Successfully')






def PDFmerge(pdfs, output):  
    # creating pdf file merger object 
    pdfMerger = PyPDF2.PdfFileMerger()
    for pdf in pdfs: 
        with open(pdf, 'rb') as f:
            pdfMerger.append(f) 
    with open(output, 'wb') as f: 
        pdfMerger.write(f) 


def get_first_pdf_fn():
        root.first_pdf_file = tkinter.filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("PDF files","*.PDF"),("all files","*.*")))
        tempname1 = (root.first_pdf_file).split('/')[-1]
        get_first_pdf_btn.config(text = tempname1,state="disabled")
        return root.first_pdf_file
def get_second_pdf_fn():
        root.second_pdf_file = tkinter.filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("PDF files","*.PDF"),("all files","*.*")))
        tempname2 = (root.second_pdf_file).split('/')[-1]
        get_second_pdf_btn.config(text = tempname2,state="disabled")
        return root.second_pdf_file

def merge():
        pdfs = [root.first_pdf_file, root.second_pdf_file]
        print((root.first_pdf_file))
        print(('\n'+root.second_pdf_file))
        root.filename = tkinter.filedialog.asksaveasfilename(initialdir = "/",title = "Select file",filetypes = (("PDF files","*.PDF"),("all files","*.*")))
        print((root.filename))
        root.filename=root.filename+'.pdf'
        tempname=root.filename.split('/')[-1]
        merge_button.config(text = tempname,state="disabled")        
        print(tempname)
        PDFmerge(pdfs = pdfs, output = root.filename)
        p1 = (root.first_pdf_file).split('/')[-1]
        p2 = (root.second_pdf_file).split('/')[-1]
        messagebox.showinfo('Message', 'Your PDF file '+p1+' and '+p2+' is Merged Successfully')



root = Tk()
style = ttk.Style(root)

root.configure( bg='white')




def select1():

	f2.grid_forget()
	f3.grid_forget()
	
	f1.place(x=100, y=200)
	f1.grid(row=1, column=1)

def select2():
	
	f1.grid_forget()
	f3.grid_forget()
	f2.place(x=100, y=200)
	f2.grid(row=1, column=1)

def select3():
	
	f1.grid_forget()
	f2.grid_forget()
	f3.place(x=100, y=200)
	f3.grid(row=1, column=1)





root.geometry('420x300')
option = IntVar()
root.title("PDF Converter v 1.0")


x=Radiobutton(root, bg='#ffffff',text="Convert",variable=option,value=1, command=select1,padx = 30,pady=50).grid(column=0, row=0)
y=Radiobutton(root, bg='#ffffff',text="Split", variable=option, value=2, command=select2,padx = 30,pady=50).grid(column=1, row=0)
z=Radiobutton(root,bg='#ffffff', text="Join", variable=option, value=3, command=select3,padx = 30,pady=50).grid(column=2, row=0)


f1 = Frame(root)
f2 = Frame(root)
f3 = Frame(root)
f1.configure( bg='red')
select1()






def reset_btn_fn():
	get_file_button.config(text='Load Image',state="enabled")
	convert_button.config(text='Convert to PDF',state="enabled")
	split_file_get_button.config(text='Load PDF',state="enabled")
	spit_main_button.config(text='Split',state="enabled")
	get_first_pdf_btn.config(text='Load PDF 1',state="enabled")
	get_second_pdf_btn.config(text='Load PDF 2',state="enabled")
	merge_button.config(text='Join PDF',state="enabled")

	root.update()
	messagebox.showinfo('Message', '         Reseted\n\nDeveloped by Saad')
actionBtn =ttk.Button(root, text="Reset", width=15,  command=reset_btn_fn).place(x=155, y=240)





#for Radio 1
get_file_button=ttk.Button(f1, text = "Load Image",width=25, command = get_img_func)
get_file_button.grid(row=0, column=1)
convert_button=ttk.Button(f1, text = "Convert to PDF",width=25, command = convert)
convert_button.grid(row=1, column=1)


#for Radio 2
split_file_get_button=ttk.Button(f2, text = "Load PDF",width=25, command = get_Split_file_func)
split_file_get_button.grid(row=0, column=1)
spit_main_button=ttk.Button(f2, text = "Split",width=25, command = split)
spit_main_button.grid(row=1, column=1)



# for Radio 3
get_first_pdf_btn=ttk.Button(f3, text = "Load PDF 1",width=25, command = get_first_pdf_fn)
get_first_pdf_btn.grid(row=0, column=1)
get_second_pdf_btn=ttk.Button(f3, text = "Load PDF 2",width=25, command = get_second_pdf_fn)
get_second_pdf_btn.grid(row=1, column=1)
merge_button=ttk.Button(f3, text = "Join PDF",width=25, command = merge)
merge_button.grid(row=2, column=1)
#change_style()

root.mainloop()
print('Task Compleated')



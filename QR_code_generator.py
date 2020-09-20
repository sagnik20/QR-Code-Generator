from tkinter import *
from tkinter import messagebox
import os
import pyqrcode
import barcode
from barcode.writer import ImageWriter
import PIL
from PIL import ImageTk,Image


s=0
#Creating the base window for the GUI
window = Tk()
window.title("QR and Bar Code Generator")

#func to set size
def setsize(a):
    global s
    s=a
    

#function generate the qr code
def generate():
    if len(Subject.get())!=0 :
        global qr,photo
        qr = pyqrcode.create(Subject.get())
        photo = BitmapImage(data = qr.xbm(scale=8))
    else:
        messagebox.showinfo("Please Enter some Subject")
    try:
        showcode()
    except:
        pass

#func to generate Barcode
def bargenerate():
    if len(Subject.get())!=0 :
        global brcode, brcodesvg, fpath
        brcode=barcode.get("code128", Subject.get(), writer=ImageWriter() )
        brcodesvg=barcode.get("code128", Subject.get() )
        dir = os.getcwd() + "\\bar Codes"
        if not os.path.exists(dir):
            os.makedirs(dir)
        fpath=os.path.join(dir,Subject.get())
        brcode.save(fpath)
        showbrcode()
    else:
        messagebox.showinfo("Please Enter some Subject")
    try:
        showcode()
    except:
        pass
    
#funct to save barcod in svg format
def brsvg():
    try:
        if len(name.get())!=0:
            dir = os.getcwd() + "\\bar Codes"
            if not os.path.exists(dir):
                os.makedirs(dir)
            spath=os.path.join(dir,name.get())
            brcodesvg.save(spath)
            os.remove(fpath+".png")
            messagebox.showinfo("","saved barcode")
        else:
            messagebox.showinfo("","Please enter a File Name")
    except:
        messagebox.showinfo("","Generate the Bar code first!")
    

#func to save barcode in png format
def brsave():
    try:
        if len(name.get())!=0:
            dir = os.getcwd() + "\\bar Codes"
            if not os.path.exists(dir):
                os.makedirs(dir)
            spath=os.path.join(dir,name.get())
            brcode.save(spath)
            os.remove(fpath+".png")
            messagebox.showinfo("barcode", "saved barcode in png")
            
        else:
            messagebox.showinfo("","Please enter a File Name")
    except:
        messagebox.showinfo("","Generate the Bar code first!")
    
    


#function to show the qr code
def showcode():
    imageLabel.config(image = photo)
    subLabel.config(text="QR of " + Subject.get())

#func to show barcode
def showbrcode():
    global photo1
    photo1= PhotoImage(file= fpath +".png")
    imageLabel1.config(image = photo1)



#function to save the generated code locally in png format
def save():
    dir = os.getcwd() + "\\QR Codes"
    if not os.path.exists(dir):
        os.makedirs(dir)
    try:
        if len(name.get())!=0:
            if s == 0:
                messagebox.showinfo("alert", "select size first")
            else:
                qr.png(os.path.join(dir,name.get()+".png"),scale=s)
                messagebox.showinfo("saved")
        else:
            messagebox.showinfo("Please enter a File Name")
    except:
        messagebox.showinfo("Generate the QR code first!")
    


#function to save the generated code locally in svg format
def svg():
    dir = os.getcwd() + "\\QR Codes"
    if not os.path.exists(dir):
        os.makedirs(dir)
    try:
        if len(name.get())!=0:
            if s == 0:
                messagebox.showinfo("alert", "select size first")
            else:
                qr.png(os.path.join(dir,name.get()+".svg"),scale=s)
                messagebox.showinfo("saved")
        else:
            messagebox.showinfo("Please enter a File Name")
    except:
        messagebox.showinfo("Generate the QR code first!")


#designing the GUI
Sub = Label(window,text="Enter subject", font=("Helvetica", 12))
Sub.grid(row =0,column =0,sticky=N+S+W+E)

FName = Label(window,text="Enter FileName", font=("Helvetica", 12))
FName.grid(row =2,column =0,sticky=N+S+W+E)

frmt = Label(window,text="Save QR in format", font=("Helvetica", 12))
frmt.grid(row = 3,column =0,sticky=N+S+W+E)

frmt1 = Label(window,text="Save Barcode in format", font=("Helvetica", 12))
frmt1.grid(row = 5,column =0,sticky=N+S+W+E)

frmt2 = Label(window,text="Select size of qr code", font=("Helvetica", 12))
frmt2.grid(row = 4,column =0,sticky=N+S+W+E)

frmt = Label(window,text="Choose type of code", font=("Helvetica", 12))
frmt.grid(row = 1,column =0,sticky=N+S+W+E)

Subject = StringVar()
SubEntry = Entry(window,textvariable = Subject, font=("Helvetica", 12))
SubEntry.grid(row =0,column =1,columnspan=2,sticky=N+S+W+E)

name = StringVar()
nameEntry = Entry(window,textvariable = name, font=("Helvetica", 12))
nameEntry.grid(row =2,column =1, columnspan=2,sticky=N+S+W+E)

f= Frame(window)
f.grid( row=4 , column =1,columnspan=2, sticky=N+S+W+E)

button = Button(window,text = "Qr code",width=15,command = generate, font=("Helvetica", 12))
button.grid(row =1,column =1,sticky=N+S+W+E)

s1 = Button(f,text = "SMALL",width=10 , command = lambda: setsize(8) , font=("Helvetica", 12))
s1.grid(row =4,column =1,sticky=N+S+W+E)

s1 = Button(f,text = "MEDIUM",width=10, command = lambda: setsize(10),  font=("Helvetica", 12))
s1.grid(row =4,column =2,sticky=N+S+W+E)

s1 = Button(f,text = "BIG",width=10, command = lambda: setsize(16) ,font=("Helvetica", 12))
s1.grid(row =4,column =3,sticky=N+S+W+E)

imageLabel = Label(window)
imageLabel.grid(row =6,column =1,sticky=N+S+W+E)

imageLabel1 = Label(window)
imageLabel1.grid(row =6,column =2,sticky=N+S+W+E)

subLabel = Label(window,text="")
subLabel.grid(row =7,column =1,sticky=N+S+W+E)

saveB = Button(window,text="Save QR as PNG",width=15,command = save , font=("Helvetica", 12))
saveB.grid(row =3,column =2,sticky=N+S+W+E)

saveB1 = Button(window,text="Save  as PNG",width=15,command = brsave , font=("Helvetica", 12))
saveB1.grid(row =5,column =2,sticky=N+S+W+E)

saveC = Button(window,text="Save QR as SVG",width=15,command = svg , font=("Helvetica", 12))
saveC.grid(row =3,column =1,sticky=N+S+W+E)

saveC1 = Button(window,text="Save  as SVG",width=15,command = brsvg , font=("Helvetica", 12))
saveC1.grid(row =5,column =1,sticky=N+S+W+E)

button1 = Button(window,text = "Barcode",width=15,command = bargenerate, font=("Helvetica", 12))
button1.grid(row =1,column = 2, sticky=N+S+W+E)


#making the GUI resposnsive
Rows = 7
Columns = 4

for row in range(Rows+1):
    window.grid_rowconfigure(row,weight=1)

for col in range(Columns+1):
    window.grid_columnconfigure(col,weight=1)


#looping the GUI
window.mainloop()

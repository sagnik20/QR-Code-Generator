from tkinter import *
from tkinter import messagebox
import os
import pyqrcode

s=0
#Creating the base window for the GUI
window = Tk()
window.title("QR Code Generator")

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


#function to show the qr code
def showcode():
    imageLabel.config(image = photo)
    subLabel.config(text="QR of " + Subject.get())



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

frmt = Label(window,text="Save in format", font=("Helvetica", 12))
frmt.grid(row = 3,column =0,sticky=N+S+W+E)

Subject = StringVar()
SubEntry = Entry(window,textvariable = Subject, font=("Helvetica", 12))
SubEntry.grid(row =0,column =1,sticky=N+S+W+E)

name = StringVar()
nameEntry = Entry(window,textvariable = name, font=("Helvetica", 12))
nameEntry.grid(row =2,column =1,sticky=N+S+W+E)

button = Button(window,text = "Generate",width=15,command = generate, font=("Helvetica", 12))
button.grid(row =0,column =2,sticky=N+S+W+E)

s1 = Button(window,text = "SMALL",width=15 , command = lambda: setsize(8) , font=("Helvetica", 12))
s1.grid(row =1,column =0,sticky=N+S+W+E)

s1 = Button(window,text = "MEDIUM",width=15, command = lambda: setsize(10),  font=("Helvetica", 12))
s1.grid(row =1,column =1,sticky=N+S+W+E)

s1 = Button(window,text = "BIG",width=15, command = lambda: setsize(16) ,font=("Helvetica", 12))
s1.grid(row =1,column =2,sticky=N+S+W+E)

imageLabel = Label(window)
imageLabel.grid(row =4,column =1,sticky=N+S+W+E)

subLabel = Label(window,text="")
subLabel.grid(row =5,column =1,sticky=N+S+W+E)

saveB = Button(window,text="Save as PNG",width=15,command = save , font=("Helvetica", 12))
saveB.grid(row =3,column =2,sticky=N+S+W+E)

saveC = Button(window,text="Save as SVG",width=15,command = svg , font=("Helvetica", 12))
saveC.grid(row =3,column =1,sticky=N+W+E)
#making the GUI resposnsive
Rows = 5
Columns = 3

for row in range(Rows+1):
    window.grid_rowconfigure(row,weight=1)

for col in range(Columns+1):
    window.grid_columnconfigure(col,weight=1)


#looping the GUI
window.mainloop()

from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
import os
import shutil
import barcode
from barcode.writer import ImageWriter
from MyQR import myqr
import csv
from datetime import datetime

s=0
#Creating the base window for the GUI
window = Tk()
window.resizable(width = False, height = False)
window.title("QR and Bar Code Generator")
window.iconbitmap("icon.ico")

#func to set size
def setsize(a):
    global s
    s=a
    messagebox.showinfo("","Select format")
    
def open_file(): 
    Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
    file = askopenfilename() # show an "Open" dialog box and return the path to the selected file
    return file

#fucn to store data in csv files
def storedata():
    if not os.path.isfile(os.getcwd() + "\\QrCode and Barcode Datas.csv"):
            with open("QrCode and Barcode Datas.csv","w",newline="") as codes:
                fields=["Subject","Type","Timestamp"]
                writer=csv.DictWriter(codes,fieldnames =fields)
                writer.writeheader()
    with open("QrCode and Barcode Datas.csv","a", newline="") as codes:
        writer=csv.writer(codes)
        if type1==1:
            writer.writerow([Subject.get(),"Qrcode",timestampStr1])
        elif type1==2:
            writer.writerow([Subject.get(),"Barcode",timestampStr2])



#function generate the qr code
def generate():
    if len(name.get())!=0 and name.get() != "Enter filename here" and len(Subject.get())!=0 and Subject.get() != "Enter subject here":
        if '/' not in name.get():
            global qr, photo, filename, save_dir, timestampStr1,type1
            filename = open_file()
            version, level, qr = myqr.run( Subject.get(), version=1, level='H', picture=filename, colorized=True, contrast=1.0, brightness=1.0, save_name=name.get()+".png", save_dir=os.path.join(os.getcwd(), "src"))
            dateTimeObj = datetime.now()
            timestampStr1 = dateTimeObj.strftime("%d-%b-%Y (%H:%M:%S.%f)")
            type1 = 1
            storedata()
            try: showcode()
            except: pass
        else: messagebox.showinfo("","filename can't contains '/'")
    else:
        messagebox.showinfo("","Please Enter some filename or subject")

#func to generate Barcode
def bargenerate():
    if len(name.get())!=0 and name.get() != "Enter filename here" and len(Subject.get())!=0 and Subject.get() != "Enter subject here":
        if '/' not in name.get():
            global brcode, fpath, type1,timestampStr2
            brcode=barcode.get("code128", Subject.get(), writer=ImageWriter() )
            brcodesvg=barcode.get("code128", Subject.get() )
            dummy = os.getcwd()+"\\images"
            if not os.path.exists(dummy):
                os.makedirs(dummy)
            fpath=os.path.join(dummy,name.get())
            brcode.save(fpath)
            dateTimeObj = datetime.now()
            timestampStr2 = dateTimeObj.strftime("%d-%b-%Y (%H:%M:%S.%f)")
            type1 = 2
            storedata()
            try: showbrcode()
            except: pass
        else: messagebox.showinfo("","filename can't contains '/'")
    else:
        messagebox.showinfo("","Please Enter some filename or subject")


#func to save barcode in png format
def brsave():
    try:
        if len(name.get())!=0 and name.get() != "Enter filename here":
            dir = "Bar_Codes"
            if not os.path.exists(dir):
                os.makedirs(dir)
            spath=os.path.join(dir,name.get())
            brcode.save(spath)
            os.remove(fpath+".png")
            messagebox.showinfo("", "Barcode saved in png format")
        else:
            messagebox.showinfo("","Please enter a File Name")
    except:
        messagebox.showinfo("","Generate the Bar code first!")
    

        
#function to show the qr code
def showcode():
    global photo
    photo = PhotoImage(file = os.path.join(os.getcwd(), "src") + "/" + name.get()+".png")
    imageLabel.config(image = photo)
    subLabel.config(text="QR of " + Subject.get())

#func to show barcode
def showbrcode():
    global photo1
    photo1 = PhotoImage(file= fpath +".png")
    imageLabel.config(image = photo1)
    subLabel.config(text="")



#function to save the generated code locally in png format
def save():
    dir = "QR_Codes"
    if not os.path.exists(dir):
        os.makedirs(dir)
    try:
        if len(name.get())!=0 and name.get() != "Enter filename here":
            if s == 0:
                messagebox.showinfo("alert", "Select size first")
            else:
                version, level, qr = myqr.run( Subject.get(), version=1, level='H', picture=filename, colorized=True, contrast=1.0, brightness=1.0, save_name=name.get()+".png", save_dir=os.path.join(os.getcwd(), "QR_Codes"))
                os.remove(os.path.join("src",name.get())+".png")
                messagebox.showinfo("","Saved")
        else:
            messagebox.showinfo("","Please enter a File Name")
    except:
        messagebox.showinfo("","Generate the QR code first!")
    


#function to save the generated code locally in svg format
def svg():
    dir = "QR_Codes"
    if not os.path.exists(dir):
        os.makedirs(dir)
    if not os.path.exists('src/'+Subject.get()+'.png'):
    	version, level, qr = myqr.run( Subject.get(), version=1, level='H', picture=filename, colorized=True, contrast=1.0, brightness=1.0, save_name=Subject.get()+".png", save_dir=os.path.join(os.getcwd(), "src"))
    shutil.copyfile('src/'+Subject.get()+'.png', 'QR_Codes/'+Subject.get()+'.svg')
    os.remove(os.path.join("src",Subject.get())+".png")
    messagebox.showinfo("","Saved")

#dummy func
def dummy():
    try:
        if len(name.get())!=0 and Subject.get() != "Enter subject here" and name.get() != "Enter filename here":
            messagebox.showinfo("","Select size")
        else:
            messagebox.showinfo("","Please enter a File Name")
    except:
        messagebox.showinfo("","Generate the QR code first!")

        
#func to clear out any entry boxes when the user shifts focus 
def clear_widget(event):
    if SubEntry == window.focus_get() and SubEntry.get() == "Enter subject here":
        SubEntry.delete(0, END)
    elif nameEntry == window.focus_get() and nameEntry.get() == "Enter filename here":
        nameEntry.delete(0, END)

#func to repopulate the default text previously inside the entry boxes if nothing is putin
#while focused and changes focus to another widget
def repopulate_defaults(event):
    if SubEntry != window.focus_get() and SubEntry.get() == "":
        SubEntry.insert(0, "Enter subject here")
    elif nameEntry != window.focus_get() and nameEntry.get() == "":
        nameEntry.insert(0, "Enter filename here")


#designing the GUI
f=Frame(window)
f.grid(row=0, column=0 ,sticky=N+S+W+E)

Subject = StringVar()
SubEntry = Entry(f,textvariable = Subject,width=50, font=("gothic", 12))
SubEntry.grid(row =0,column =0,columnspan=5,sticky=N+S+W+E)
SubEntry.insert(END,"Enter subject here")
SubEntry.bind("<FocusOut>", repopulate_defaults)
SubEntry.bind("<FocusIn>", clear_widget)

name = StringVar()
nameEntry = Entry(f,textvariable = name, width=50, font=("gothic", 12))
nameEntry.grid(row =1,column =0, columnspan=5,sticky=N+S+W+E)
nameEntry.insert(0,"Enter filename here")
nameEntry.bind("<FocusOut>", repopulate_defaults)
nameEntry.bind("<FocusIn>", clear_widget)


f2=Frame(window)
f2.grid(row=2, column=0, sticky=N+S+W+E)

s1 = Button(f2,text = "Qr code",width=9 , command = generate , font=("Helvetica", 12))
s1.grid(row =0,column =0,sticky=N+S+W+E)

s1 = Button(f2,text = "Save",width=9, command = dummy , font=("Helvetica", 12))
s1.grid(row =0,column =1,sticky=N+S+W+E)

s1=Label(f2,text=" ", width=3)
s1.grid(row=0,column=2,sticky=N+S+W+E)

s1 = Button(f2,text = "Bar code",width=9 , command = bargenerate , font=("Helvetica", 12))
s1.grid(row =0,column =3,sticky=N+S+W+E)

s1 = Button(f2,text = "Save",width=9 , command = brsave , font=("Helvetica", 12))
s1.grid(row =0,column =4,sticky=N+S+W+E)


f3= Frame(window)
f3.grid( row=3, column=0, columnspan=2, sticky=N+S+W+E)

s1 = Button(f3,text = "Small",width=4, command = lambda: setsize(8) , font=("Helvetica", 12))
s1.grid(row =0,column =0,sticky=N+S+W+E)

s1 = Button(f3,text = "Medium",width=7, command = lambda: setsize(10),  font=("Helvetica", 12))
s1.grid(row =0,column =1,sticky=N+S+W+E)

s1 = Button(f3,text = "Large",width=6, command = lambda: setsize(16) ,font=("Helvetica", 12))
s1.grid(row =0,column =2,sticky=N+S+W+E)

f4=Frame(window)
f4.grid( row=4, column=0, columnspan=2, sticky=N+S+W+E)

saveB = Button(f4,text="PNG",width=9,command = save, font=("Helvetica", 12))
saveB.grid(row =1,column =0,sticky=N+S+W+E)

saveC = Button(f4,text="SVG",width=9,command = svg , font=("Helvetica", 12))
saveC.grid(row =1,column =1,sticky=N+S+W+E)



imageLabel = Label(window)
imageLabel.grid(row =5,column =0,sticky=N+S+W+E)


subLabel = Label(window,text="")
subLabel.grid(row =6,column =0,sticky=N+S+W+E)





#making the GUI resposnsive
Rows = 6
Columns = 4

for row in range(Rows+1):
    window.grid_rowconfigure(row,weight=1)

for col in range(Columns+1):
    window.grid_columnconfigure(col,weight=1)


#looping the GUI
window.mainloop()

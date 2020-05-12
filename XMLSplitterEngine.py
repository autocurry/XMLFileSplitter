import tkinter as tk
from tkinter import *
from tkinter import filedialog
import os
from xmlsplitter import *
from tkinter import messagebox
import logging
from pathlib import Path

logging.basicConfig(level=logging.DEBUG, filename='app.log', filemode='w', format='%(asctime)s - %(message)s')

filepath = ''


validations = {
    0: 'Please select XML File to Split',
    1:'Please select the count of output records',
    2:'Please select splitter tag'
}

totalrecords = 0

def browse():
    global filepath
    filepath = filedialog.askopenfilename(
    title="Choose directory",
    initialdir=os.getcwd(),
    filetypes=[("XML Files", "*.xml")]  
    )   
    browsefilename.delete(0,END) 
    browsefilename.insert(END,Path(filepath).name)
    outputflename.delete(0,END)
    outputflename.insert(END,Path(filepath).name)
    #count = elementcount(filepath,str(splittertag.get()))
    #totalcountlabel['text'] = "Total = "+str(count)

def counting():
    checkcounter = os.path.exists(filepath)
    if(not checkcounter):
        messagebox.showinfo('Validation Error',"Please provide a valid file imput file")
    count = elementcount(filepath,str(splittertag.get()))
    totalcountvalue.delete(0,END)
    totalcountvalue.insert(END,count)

# trim function creates a smaller file with the number of records mentioned having the parent tag as the tag name mentioned
def trim():
    #validate
    messagelist=[]
    if(browsefilename.get() == ''):
        messagelist.append(validations[0])
    if(countbox.get() == ''):
        messagelist.append(validations[1])
    if(splittertag.get()== ''):
        messagelist.append(validations[2])
    
    if(len(messagelist)== 0):
        count = int(countbox.get())
        splittag=str(splittertag.get())
        outpath = outputflename.get()
        splitxmlfile(filepath,count,splittag,outpath)
        messagebox.showinfo('Success',f'File generated in the path: {os.getcwd()+"/Output"+"/"+outpath}')
    else:
        messages = ''
        for message in messagelist:
            messages = messages + message +"\n"
        messagebox.showinfo('Warning',messages)


# split function splits the whole xml file into child files having 10,000 records of the tag mentioned
def split():
    #validate
    messagelist=[]
    if(browsefilename.get() == ''):
        messagelist.append(validations[0])
    if(splittertag.get()== ''):
        messagelist.append(validations[2])

    if(len(messagelist)== 0):        
        splittag=str(splittertag.get())
        outpath = outputflename.get()
        splitxmlfilewithcounter(filepath,splittag,outpath)
        messagebox.showinfo('Success',f'Files generated in the path: {os.getcwd()+"/Output"+"/"}')
    else:
        messages = ''
        for message in messagelist:
            messages = messages + message +"\n"
        messagebox.showinfo('Warning',messages)

def searchandtrim():    
    messagelist=[]
    if(browsefilename.get() == ''):
        messagelist.append(validations[0])
    if(splittertag.get()== ''):
        messagelist.append(validations[2])

    if(len(messagelist)== 0):        
        splittag=str(splittertag.get())
        outpath = outputflename.get()
        splitxmlfilewithcounter(filepath,splittag,outpath)
        messagebox.showinfo('Success',f'Files generated in the path: {os.getcwd()+"/Output"+"/"}')
    else:
        messages = ''
        for message in messagelist:
            messages = messages + message +"\n"
        messagebox.showinfo('Warning',messages)

root=tk.Tk()
root.title("XML File Splitter")

baseframe = tk.Frame(root,height=400,width=700, borderwidth=5,bg='#CEEFF0')
baseframe.pack()

totalframe = tk.Frame(baseframe, bg='#FFFFFF')
totalframe.place(relx=0.5,rely=0.1,relwidth=0.8,relheight=0.7,anchor='n')

browselabel = tk.Label(totalframe, text="Please select the XML File *",fg="Black",font=('Helvetica','12'),bg="white")
browselabel.grid(column=0,row=0, padx=5,pady=5,sticky = W)

browsefilename = tk.Entry(totalframe,fg="Black",font=('Helvetica','12'),bg="white",width=20)
browsefilename.grid(column=1,row=0, padx=5,pady=5)

browsebutton = tk.Button(totalframe,text='Browse', command=browse,fg="Black",font=('Helvetica','12'))
browsebutton.grid(column=2,row=0,padx=5,pady=5)

countlabel = tk.Label(totalframe, text="Count of records", fg="Black",font=('Helvetica','12'),bg="white")
countlabel.grid(column=0,row=1, padx=5,pady=5,sticky = W)

countbox = tk.Entry(totalframe,fg="Black",font=('Helvetica','12'),bg="white",width=5)
countbox.grid(column=1,row=1, padx=5,pady=5,sticky = W)


outputbrowselabel = tk.Label(totalframe, text="Please select the output filename",fg="Black",font=('Helvetica','12'),bg="white")
outputbrowselabel.grid(column=0,row=2, padx=5,pady=5,sticky = W)

outputflename = tk.Entry(totalframe,fg="Black",font=('Helvetica','12'),bg="white",width=20)
outputflename.grid(column=1,row=2, padx=5,pady=5)

splitterlabel = tk.Label(totalframe, text="Splitter Tag",fg="Black",font=('Helvetica','12'),bg="white")
splitterlabel.grid(column=0,row=3, padx=5,pady=5,sticky = W)

splittertag = tk.Entry(totalframe,fg="Black",font=('Helvetica','12'),bg="white",width=10)
splittertag.insert(END,'employee')
splittertag.grid(column=1,row=3, padx=5,pady=5,sticky = W)


totalcountbutton = tk.Button(totalframe, text="Total",command=counting,relief=RAISED,fg="Black",font=('Helvetica','14','bold'))
totalcountbutton.grid(column=0,row=4, padx=5,pady=5,sticky = W)

totalcountvalue = tk.Entry(totalframe, relief=RAISED,fg="Black",font=('Helvetica','14','bold'))
totalcountvalue.grid(column=1,row=4, padx=5,pady=5,sticky = W)

trimbutton = tk.Button(baseframe,text="Trim",command=trim, relief=RAISED,fg="Black",font=('Helvetica','14','bold'))
trimbutton.place(relx=0.25,rely=0.65,relwidth=0.2,relheight=0.1,anchor='n')

removecontents = tk.Button(baseframe,text='Split', command=split, relief=RAISED,fg="Black",font=('Helvetica','14','bold'))
removecontents.place(relx=0.5,rely=0.65,relwidth=0.2,relheight=0.1,anchor='n')

searchandtrim = tk.Button(baseframe,text='Search&Trim', command=searchandtrim, relief=RAISED,fg="Black",font=('Helvetica','14','bold'))
searchandtrim.place(relx=0.75,rely=0.65,relwidth=0.2,relheight=0.1,anchor='n')



root.mainloop()
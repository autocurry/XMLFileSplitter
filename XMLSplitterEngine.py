import tkinter as tk
from tkinter import *
from tkinter import filedialog
import os
from xmlsplitter import *
from tkinter import messagebox
import logging
from pathlib import Path
from xmlremove import *

logging.basicConfig(level=logging.DEBUG, filename='app.log', filemode='w', format='%(asctime)s - %(message)s')

filepath = ''
validations = {
    0: 'Please select XML File to Split',
    1:'Please select the count of output records required',
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
    count = elementcount(filepath,str(splittertag.get()))
    totalcountlabel['text'] = "Total = "+str(count)


def split():
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
        logging.info(f'splitting the file: {filepath} with {count} records on {splittag} tag')
        #splitxmlfile(filepath,count,splittag,outpath) 
        #splitxmlfilewithcounter(filepath,splittag,outpath)       
        findandremove(filepath,'employee','id')
        messagebox.showinfo('Success',f"File generated in the path: {os.getcwd()}\{outputflename.get()}")
    else:
        messages = ''
        for message in messagelist:
            messages = messages + message +"\n"
        messagebox.showinfo('Warning',messages)

def remove():
    count = int(countbox.get())
    splittag=str(splittertag.get())
    outpath = outputflename.get()
    xmlremovecontents(filepath,count,splittag,outpath)
    messagebox.showinfo('Warning','done')
    

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

countlabel = tk.Label(totalframe, text="Count of records *", fg="Black",font=('Helvetica','12'),bg="white")
countlabel.grid(column=0,row=1, padx=5,pady=5,sticky = W)

countbox = tk.Entry(totalframe,fg="Black",font=('Helvetica','12'),bg="white",width=5)
countbox.grid(column=1,row=1, padx=5,pady=5,sticky = W)

totalcountlabel = tk.Button(totalframe, text="Total = "+str(totalrecords),command=counting,fg="Black",font=('Helvetica','12'),bg="white")
totalcountlabel.grid(column=2,row=1, padx=5,pady=5,sticky = W)

outputbrowselabel = tk.Label(totalframe, text="Please select the output filename",fg="Black",font=('Helvetica','12'),bg="white")
outputbrowselabel.grid(column=0,row=2, padx=5,pady=5,sticky = W)

outputflename = tk.Entry(totalframe,fg="Black",font=('Helvetica','12'),bg="white",width=20)
outputflename.grid(column=1,row=2, padx=5,pady=5)

splitterlabel = tk.Label(totalframe, text="Splitter Tag",fg="Black",font=('Helvetica','12'),bg="white")
splitterlabel.grid(column=0,row=3, padx=5,pady=5,sticky = W)

splittertag = tk.Entry(totalframe,fg="Black",font=('Helvetica','12'),bg="white",width=10)
splittertag.insert(END,'employee')
splittertag.grid(column=1,row=3, padx=5,pady=5,sticky = W)

convertbutton = tk.Button(baseframe,text='Split', command=split, relief=RAISED,fg="Black",font=('Helvetica','14','bold'))
convertbutton.place(relx=0.45,rely=0.55,relwidth=0.2,relheight=0.1,anchor='n')

removecontents = tk.Button(baseframe,text='Remove', command=remove, relief=RAISED,fg="Black",font=('Helvetica','14','bold'))
removecontents.place(relx=0.7,rely=0.55,relwidth=0.2,relheight=0.1,anchor='n')



root.mainloop()
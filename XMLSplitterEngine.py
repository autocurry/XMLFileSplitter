import tkinter as tk
from tkinter import *
from tkinter import filedialog
import os
from xmlsplitter import *
from tkinter import messagebox
import logging

logging.basicConfig(level=logging.DEBUG, filename='app.log', filemode='w', format='%(asctime)s - %(message)s')

filepath = ''
def browse():
    global filepath
    filepath = filedialog.askopenfilename(
    title="Choose directory",
    initialdir=os.getcwd(),
    filetypes=[("XML Files", "*.xml")]        
    )        

def split():
    if(filepath != NONE and filepath != ''):
        count = int(countbox.get())
        splittag=str(splittertag.get())
        logging.info(f'splitting the file: {filepath} with {count} records on {splittag} tag')
        splitxmlfile(filepath,count,splittag)
        messagebox.showinfo('Success','File generated')
    else:
        messagebox.showinfo('Warning','Please select xml file to split')
    

root=tk.Tk()
root.title("XML File Splitter")

baseframe = tk.Frame(root,height=300,width=400, borderwidth=5)
baseframe.pack()

totalframe = tk.Frame(baseframe, bg='#ffffff')
totalframe.place(relx=0.45,rely=0.2,relwidth=0.9,relheight=0.7,anchor='n')

browselabel = tk.Label(totalframe, text="Please select the XML File",fg="Black",font=('Helvetica','12'),bg="white")
browselabel.grid(column=0,row=0, padx=5,pady=5)

browsebutton = tk.Button(totalframe,text='Browse', command=browse,fg="Black",font=('Helvetica','12'))
browsebutton.grid(column=1,row=0,padx=5,pady=5)

countlabel = tk.Label(totalframe, text="Count of records",fg="Black",font=('Helvetica','12'),bg="white")
countlabel.grid(column=0,row=1, padx=5,pady=5)

countbox = tk.Entry(totalframe,fg="Black",font=('Helvetica','12'),bg="white",width=5)
countbox.grid(column=1,row=1, padx=5,pady=5)

splitterlabel = tk.Label(totalframe, text="Splitter Tag",fg="Black",font=('Helvetica','12'),bg="white")
splitterlabel.grid(column=0,row=2, padx=5,pady=5)

splittertag = tk.Entry(totalframe,fg="Black",font=('Helvetica','12'),bg="white",width=5)
splittertag.insert(END,'p')
splittertag.grid(column=1,row=2, padx=5,pady=5)

convertbutton = tk.Button(totalframe,text='Split', command=split, relief=RAISED,fg="Black",font=('Helvetica','14','bold'))
convertbutton.grid(column=0,row=4,padx=25,pady=5)

root.mainloop()
import tkinter as tk
from tkinter import ttk
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
    2:'Please select splitter tag',
    3:'Please select the folder path'
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
    

# split function creates a smaller file with the number of records mentioned having the parent tag as the tag name mentioned
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
        splitxmlfile(filepath,count,splittag,outpath)
        messagebox.showinfo('Success',f'File generated in the path: {os.getcwd()+"/Output"+"/"+outpath}')
    else:
        messages = ''
        for message in messagelist:
            messages = messages + message +"\n"
        messagebox.showinfo('Warning',messages)



root=tk.Tk()
root.title("XML File Splitter")
myunselect = "#ffffff"
myselected = "#CEEFF0"

style = ttk.Style()
style.theme_create( "mystyle", parent="alt", settings={
        "TNotebook": {"configure": {"tabmargins": [4, 5, 2, 0] } },
        "TNotebook.Tab": {
            "configure": {"padding": [20, 20], "background": myunselect, "font" : ('Helvetica', '14', 'bold') },
            "map":       {"background": [("selected", myselected)],
                          "expand": [("selected", [1, 1, 1, 0])] } } } )

style.theme_use("mystyle")




baseframe = tk.Frame(root,height=400,width=700, borderwidth=5,bg='#CEEFF0')
baseframe.pack()

tabmenu = ttk.Notebook(baseframe,height=300,width=700)

splittab = ttk.Frame(tabmenu)
tabmenu.add(splittab, text = 'SPLIT')

trimtab = ttk.Frame(tabmenu)
tabmenu.add(trimtab, text = 'TRIM')

searchandsplittab = ttk.Frame(tabmenu)
tabmenu.add(searchandsplittab, text = 'Search and Split')

totalcounttab = ttk.Frame(tabmenu)
tabmenu.add(totalcounttab, text = 'Total Count')

tabmenu.pack(expand=1, fill='both', padx=5, pady=5)





#SplitTab controls 

browselabel = tk.Label(splittab, text="Please select the XML File *",fg="Black",font=('Helvetica','12'),bg="white")
browselabel.grid(column=0,row=0, padx=5,pady=5,sticky = W)

browsefilename = tk.Entry(splittab,fg="Black",font=('Helvetica','12'),bg="white",width=20)
browsefilename.grid(column=1,row=0, padx=5,pady=5)

browsebutton = tk.Button(splittab,text='Browse', command=browse,fg="Black",font=('Helvetica','12'))
browsebutton.grid(column=2,row=0,padx=5,pady=5)

countlabel = tk.Label(splittab, text="Count of records", fg="Black",font=('Helvetica','12'),bg="white")
countlabel.grid(column=0,row=1, padx=5,pady=5,sticky = W)

countbox = tk.Entry(splittab,fg="Black",font=('Helvetica','12'),bg="white",width=5)
countbox.insert(END,'5')
countbox.grid(column=1,row=1, padx=5,pady=5,sticky = W)


outputbrowselabel = tk.Label(splittab, text="Please select the output filename",fg="Black",font=('Helvetica','12'),bg="white")
outputbrowselabel.grid(column=0,row=2, padx=5,pady=5,sticky = W)

outputflename = tk.Entry(splittab,fg="Black",font=('Helvetica','12'),bg="white",width=20)
outputflename.grid(column=1,row=2, padx=5,pady=5)

splitterlabel = tk.Label(splittab, text="Splitter Tag",fg="Black",font=('Helvetica','12'),bg="white")
splitterlabel.grid(column=0,row=3, padx=5,pady=5,sticky = W)

splittertag = tk.Entry(splittab,fg="Black",font=('Helvetica','12'),bg="white",width=10)
splittertag.insert(END,'employee')
splittertag.grid(column=1,row=3, padx=5,pady=5,sticky = W)


trimbutton = tk.Button(splittab,text="SPLIT",command=split, relief=RAISED,fg="Black",font=('Helvetica','14','bold'))
trimbutton.place(relx=0.3,rely=0.6,relwidth=0.2,relheight=0.1,anchor='n')

#Trim tab controls


# trim function splits the whole xml file into child files having 10,000 records of the tag mentioned
def trim():
    #validate
    messagelist=[]
    if(trimfilename.get() == ''):
        messagelist.append(validations[0])
    if(trimsplittertag.get()== ''):
        messagelist.append(validations[2])

    if(len(messagelist)== 0):        
        splittag=str(trimsplittertag.get()) 
        iterator = str(trimiteratortag.get())       
        splitxmlfilewithcounter(trimfilepath,splittag,iterator)
        messagebox.showinfo('Success',f'Files generated in the path: {os.getcwd()+"/Output"+"/"}')
    else:
        messages = ''
        for message in messagelist:
            messages = messages + message +"\n"
        messagebox.showinfo('Warning',messages)

trimfilepath =''
def trimbrowse():    
    global trimfilepath
    trimfilepath = filedialog.askopenfilename(
    title="Choose directory",
    initialdir=os.getcwd(),
    filetypes=[("XML Files", "*.xml")]  
    )   
    trimfilename.delete(0,END) 
    trimfilename.insert(END,Path(trimfilepath).name)

trimbrowselabel = tk.Label(trimtab, text="Please select the XML File *",fg="Black",font=('Helvetica','12'),bg="white")
trimbrowselabel.grid(column=0,row=0, padx=5,pady=5,sticky = W)

trimfilename = tk.Entry(trimtab,fg="Black",font=('Helvetica','12'),bg="white",width=20)
trimfilename.grid(column=1,row=0, padx=5,pady=5)

trimbrowsebutton = tk.Button(trimtab,text='Browse', command=trimbrowse,fg="Black",font=('Helvetica','12'))
trimbrowsebutton.grid(column=2,row=0,padx=5,pady=5)

trimsplitterlabel = tk.Label(trimtab, text="Splitter Tag",fg="Black",font=('Helvetica','12'),bg="white")
trimsplitterlabel.grid(column=0,row=1, padx=5,pady=5,sticky = W)

trimsplittertag = tk.Entry(trimtab,fg="Black",font=('Helvetica','12'),bg="white",width=10)
trimsplittertag.insert(END,'employee')
trimsplittertag.grid(column=1,row=1, padx=5,pady=5,sticky = W)


trimiteratorlabel = tk.Label(trimtab, text="Iterator",fg="Black",font=('Helvetica','12'),bg="white")
trimiteratorlabel.grid(column=0,row=2, padx=5,pady=5,sticky = W)

trimiteratortag = tk.Entry(trimtab,fg="Black",font=('Helvetica','12'),bg="white",width=10)
trimiteratortag.insert(END,'10000')
trimiteratortag.grid(column=1,row=2, padx=5,pady=5,sticky = W)


removecontents = tk.Button(trimtab,text='TRIM', command=trim, relief=RAISED,fg="Black",font=('Helvetica','14','bold'))
removecontents.place(relx=0.3,rely=0.6,relwidth=0.2,relheight=0.1,anchor='n')


#Total count tab controls
countfilepath = ''

def totalbrowse():    
    global countfilepath
    countfilepath = filedialog.askopenfilename(
    title="Choose directory",
    initialdir=os.getcwd(),
    filetypes=[("XML Files", "*.xml")]  
    )   
    totalbrowsefilename.delete(0,END) 
    totalbrowsefilename.insert(END,Path(countfilepath).name)

def totalcounting():
    checkcounter = os.path.exists(countfilepath)
    if(not checkcounter):
        messagebox.showinfo('Validation Error',"Please provide a valid file imput file")
    count = elementcount(countfilepath,str(totalsplittertag.get()))
    totalcountvalue.delete(0,END)
    totalcountvalue.insert(END,count)


totalbrowselabel = tk.Label(totalcounttab, text="Please select the XML File *",fg="Black",font=('Helvetica','12'),bg="white")
totalbrowselabel.grid(column=0,row=0, padx=5,pady=5,sticky = W)

totalbrowsefilename = tk.Entry(totalcounttab,fg="Black",font=('Helvetica','12'),bg="white",width=20)
totalbrowsefilename.grid(column=1,row=0, padx=5,pady=5)

totalbrowsebutton = tk.Button(totalcounttab,text='Browse', command=totalbrowse,fg="Black",font=('Helvetica','12'))
totalbrowsebutton.grid(column=2,row=0,padx=5,pady=5)

totalsplitterlabel = tk.Label(totalcounttab, text="Splitter Tag",fg="Black",font=('Helvetica','12'),bg="white")
totalsplitterlabel.grid(column=0,row=1, padx=5,pady=5,sticky = W)

totalsplittertag = tk.Entry(totalcounttab,fg="Black",font=('Helvetica','12'),bg="white",width=10)
totalsplittertag.insert(END,'employee')
totalsplittertag.grid(column=1,row=1, padx=5,pady=5,sticky = W)


totalcountbutton = tk.Button(totalcounttab, text="Total",command=totalcounting,relief=RAISED,fg="Black",font=('Helvetica','14','bold'))
totalcountbutton.grid(column=0,row=2, padx=5,pady=5,sticky = W)

totalcountvalue = tk.Entry(totalcounttab, relief=RAISED,fg="Black",font=('Helvetica','14','bold'))
totalcountvalue.grid(column=1,row=2, padx=5,pady=5,sticky = W)


#Search and Trim control goes here

# Search and trim method checks validations and splits the file based on the search criteria
def searchandtrim():      
    messagelist=[]    
    if(searchandtrimbrowsefiledirname.get()== ''):
        messagelist.append(validations[3])

    if(len(messagelist)== 0):        
        parenttag=str(searchandtrimparenttag.get())    
        tagname=str(searchandtrimtag.get())    
        value=int(searchandtrimvalue.get()) 
        filepathdir = searchandtrimbrowsefiledirname.get()  
        findandremove(parenttag,tagname,value,filepathdir)
        messagebox.showinfo('Success',f'Files generated in the path: {os.getcwd()+"/Output"+"/"}')
    else:
        messages = ''
        for message in messagelist:
            messages = messages + message +"\n"
        messagebox.showinfo('Warning',messages)



def selectdir():
    searchandtrimdir = filedialog.askdirectory()
    searchandtrimbrowsefiledirname.delete(0,END) 
    searchandtrimbrowsefiledirname.insert(END,searchandtrimdir)



searchandtrimbrowselabel = tk.Label(searchandsplittab, text="Please select the directory path*",fg="Black",font=('Helvetica','12'),bg="white")
searchandtrimbrowselabel.grid(column=0,row=0, padx=5,pady=5,sticky = W)

searchandtrimbrowsefiledirname = tk.Entry(searchandsplittab,fg="Black",font=('Helvetica','12'),bg="white",width=20)
searchandtrimbrowsefiledirname.grid(column=1,row=0, padx=5,pady=5)

searchandtrimbrowsebutton = tk.Button(searchandsplittab,text='Browse', command=selectdir,fg="Black",font=('Helvetica','12'))
searchandtrimbrowsebutton.grid(column=2,row=0,padx=5,pady=5)

searchandtrimparenttaglabel = tk.Label(searchandsplittab, text="Parent Tag",fg="Black",font=('Helvetica','12'),bg="white")
searchandtrimparenttaglabel.grid(column=0,row=1, padx=5,pady=5,sticky = W)

searchandtrimparenttag = tk.Entry(searchandsplittab,fg="Black",font=('Helvetica','12'),bg="white",width=10)
searchandtrimparenttag.insert(END,'employee')
searchandtrimparenttag.grid(column=1,row=1, padx=5,pady=5,sticky = W)


searchandtrimtaglabel = tk.Label(searchandsplittab, text="Search Tag",fg="Black",font=('Helvetica','12'),bg="white")
searchandtrimtaglabel.grid(column=0,row=2, padx=5,pady=5,sticky = W)

searchandtrimtag = tk.Entry(searchandsplittab,fg="Black",font=('Helvetica','12'),bg="white",width=10)
searchandtrimtag.insert(END,'id')
searchandtrimtag.grid(column=1,row=2, padx=5,pady=5,sticky = W)


searchandtrimvaluelabel = tk.Label(searchandsplittab, text="Search Value",fg="Black",font=('Helvetica','12'),bg="white")
searchandtrimvaluelabel.grid(column=0,row=3, padx=5,pady=5,sticky = W)

searchandtrimvalue = tk.Entry(searchandsplittab,fg="Black",font=('Helvetica','12'),bg="white",width=10)
searchandtrimvalue.insert(END,'200')
searchandtrimvalue.grid(column=1,row=3, padx=5,pady=5,sticky = W)

searchandtrim = tk.Button(searchandsplittab,text='Search and Trim', command=searchandtrim, relief=RAISED,fg="Black",font=('Helvetica','14','bold'))
searchandtrim.place(relx=0.3,rely=0.6,relwidth=0.3,relheight=0.1,anchor='n')



root.mainloop()
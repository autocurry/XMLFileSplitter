import xml.etree.ElementTree as ET
import sys
import logging
import os, fnmatch
import shutil
from pathlib import Path

outputpath = os.getcwd()+"\\Output"

def directoryclear():
    if(not (os.path.exists(outputpath))):
        os.mkdir(outputpath)
    else:
        shutil.rmtree(outputpath)
        os.mkdir(outputpath)

def elementcount(filepath,tag):
    count = 0
    for event, elem in ET.iterparse(filepath):
        if event == 'end':
                if elem.tag == tag:
                    count += 1
                    elem.clear() # discard the element
    return count  

def splitxmlfile(filepath,count,tag,outpath):
    syscount = count    
    directoryclear()  
    try:
        logging.info('Splitting in progress')
        context = ET.iterparse(filepath, events=('start', ))        
        filename = outputpath+"//"+format(outpath)
        with open(filename, 'wb') as f:
            f.write(b"<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n")                
            nodes =[]
            for event, elem in context:   
                if count > 0:             
                    if elem.tag == tag and count >= 0:
                        f.write(ET.tostring(elem)) 
                        elem.clear()
                        count -= 1
                    elif syscount == count:
                        nodes.append(elem.tag)
                        f.write(("<"+elem.tag+">").encode())
                else:
                    break
            nodes.reverse()
            for node in nodes:
                f.write(("</"+node+">").encode())
    except IOError:
        type, value, traceback = sys.exc_info()
        logging.error('Error opening %s: %s' % (value.filename, value.strerror))   

def splitxmlfilewithcounter(filepath,tag,terator):    
    directoryclear()
    totalcount = elementcount(filepath,tag)
    iterator = int(terator) 
    nooffiles = int(totalcount / iterator )
    diviser = totalcount % iterator
    if diviser > 0:
        nooffiles += 1
    init = 0
    maximu = iterator
    while (nooffiles>0):   
        syscount = 1
        count = 1             
        try:
            logging.info('Splitting in progress')
            context = ET.iterparse(filepath, events=('start', ))        
            filename = outputpath+"//"+str(init)+"to"+str(maximu)+"_"+format(Path(filepath).name)
            with open(filename, 'wb') as f:
                f.write(b"<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n")                
                nodes =[]
                for event, elem in context:                                    
                    if elem.tag == tag:
                        if count > init :
                            if count <= maximu:
                                f.write(ET.tostring(elem)) 
                                elem.clear()
                                
                            else:
                                init = maximu
                                maximu = init+iterator                                
                                break                    
                        count += 1
                    elif syscount == count:
                        nodes.append(elem.tag)
                        f.write(("<"+elem.tag+">").encode())
                        
                nodes.reverse()
                for node in nodes:
                    f.write(("</"+node+">").encode())
                nooffiles -= 1
        except IOError:
            type, value, traceback = sys.exc_info()
            logging.error('Error opening %s: %s' % (value.filename, value.strerror))  

def findandremove(parenttagname, tagname,value,filepaths = outputpath):    
    listoffiles = os.listdir(filepaths)
    pattern = "*.xml"
    xmlfiles =[]
    for entry in listoffiles:
        if fnmatch.fnmatch(entry,pattern):
            xmlfiles.append(entry)
    goahead = True        
    for xmlfile in xmlfiles:
        if goahead:        
            context = ET.iterparse(os.path.join(filepaths,xmlfile), events=('start', ))
            filename = 'trimmed.xml'
            syscount = 0
            with open(filename, 'wb') as f:
                f.write(b"<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n")                
                nodes =[]
                for event, elem in context:   
                    if elem.tag == parenttagname:
                        syscount += 1
                        contents = ET.tostring(elem).decode()
                        searchkey = '<'+tagname+'>'+str(value)+'</'+tagname+'>'
                        if (searchkey in contents):
                            logging.info("found matching value and printing")
                            f.write(ET.tostring(elem))
                            goahead = False
                            break
                    elif syscount == 0:
                        nodes.append(elem.tag)
                        f.write(("<"+elem.tag+">").encode())
                nodes.reverse()
                for node in nodes:
                    f.write(("</"+node+">").encode())
        
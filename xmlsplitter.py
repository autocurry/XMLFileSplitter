import xml.etree.ElementTree as ET
import sys
import logging
import os
import shutil

outputpath = os.getcwd()+"\\Output"

def directoryclear(filepath):
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
    directoryclear(filepath)  
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

def splitxmlfilewithcounter(filepath,tag,outpath):    
    directoryclear(filepath)
    totalcount = elementcount(filepath,tag)
    iterator = 10000
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
            filename = outputpath+"//"+str(init)+"to"+str(maximu)+"_"+format(outpath)
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

def findandremove(filepath, parenttagname, tagname, value=277):
    syscount = 0
    context = ET.iterparse(filepath, events=('start', ))
    filename = 'trimmed.xml'
    with open(filename, 'wb') as f:
        f.write(b"<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n")                
        nodes =[]
        for event, elem in context:   
            if elem.tag == parenttagname:
                syscount += 1
                contents = ET.tostring(elem).decode()
                searchkey = '<'+tagname+'>'+str(value)+'</'+tagname+'>'
                if (searchkey in contents):
                    print(ET.tostring(elem))
                    f.write(ET.tostring(elem))
                    break
            elif syscount == 0:
                nodes.append(elem.tag)
                f.write(("<"+elem.tag+">").encode())
        nodes.reverse()
        for node in nodes:
            f.write(("</"+node+">").encode())
    
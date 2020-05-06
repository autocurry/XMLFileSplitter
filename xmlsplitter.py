import xml.etree.ElementTree as ET
import sys
import logging

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
    try:
        logging.info('Splitting in progress')
        context = ET.iterparse(filepath, events=('start', ))        
        filename = format(outpath)
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
    totalcount = elementcount(filepath,tag)
    nooffiles = int(totalcount / 100 )
    diviser = totalcount % 100
    if diviser > 0:
        nooffiles += 1
    init = 0
    maximu = 100
    while (nooffiles>0):   
        syscount = 1
        count = 1             
        try:
            logging.info('Splitting in progress')
            context = ET.iterparse(filepath, events=('start', ))        
            filename = str(maximu)+format(outpath)
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
                                maximu = init+100
                                nooffiles -= 1
                                break                    
                        count += 1
                    elif syscount == count:
                        nodes.append(elem.tag)
                        f.write(("<"+elem.tag+">").encode())
                        
                nodes.reverse()
                for node in nodes:
                    f.write(("</"+node+">").encode())
        except IOError:
            type, value, traceback = sys.exc_info()
            logging.error('Error opening %s: %s' % (value.filename, value.strerror))   

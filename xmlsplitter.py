import xml.etree.ElementTree as ET
import sys
import logging

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
        
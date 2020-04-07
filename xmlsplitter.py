import xml.etree.ElementTree as ET
import sys
import logging

def splitxmlfile(filepath,count,tag):
    try:
        logging.info('Splitting in progress')
        context = ET.iterparse(filepath, events=('end', ))
        title = 'splittedfile'
        filename = format(title + ".xml")
        with open(filename, 'wb') as f:
            f.write(b"<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n")
            f.write(b"<root>\n")      
            for event, elem in context:
                
                if elem.tag == tag and count >= 0:
                    f.write(ET.tostring(elem)) 
                    count -= 1
                else:
                    break
            f.write(b"</root>\n")  
    except IOError:
        type, value, traceback = sys.exc_info()
        logging.error('Error opening %s: %s' % (value.filename, value.strerror))   
        
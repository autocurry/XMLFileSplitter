import xml.etree.ElementTree as ET
import sys
import logging
from shutil import copyfile


def xmlremovecontents(filepath,count,tag,outpath):
    syscount = count
    try:
        logging.info('Splitting in progress')
                
        filename = format(outpath)
        copyfile(filepath, outpath)
        context = ET.iterparse(outpath, events=('start', ))            
        for event, elem in context:   
            if count > 0:             
                if elem.tag == tag and count >= 0:
                    elem.remove()
                    count -= 1
                elif syscount == count:
                    pass                    
            else:
                break            

    except IOError:
        type, value, traceback = sys.exc_info()
        logging.error('Error opening %s: %s' % (value.filename, value.strerror))   
        
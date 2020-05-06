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
            if elem.tag == 'employee' and count >= 0:
                    for d in elem.iterfind("id"):
                        if count > 0:   
                            elem.remove(d)                            
                            count -= 1
                        else:
                            ET.dump(elem)
                            break       

    except IOError:
        type, value, traceback = sys.exc_info()
        logging.error('Error opening %s: %s' % (value.filename, value.strerror)) 


        
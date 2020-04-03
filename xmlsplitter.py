import xml.etree.ElementTree as ET

def split():
    context = ET.iterparse('output.xml', events=('end', ))
    title = 'splittedfile'
    filename = format(title + ".xml")
    with open(filename, 'wb') as f:
        f.write(b"<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n")
        f.write(b"<root>\n")
        count = 10
        for elem in context:
            count -= 1
            if elem.tag == 'p' and count >= 0:
                f.write(ET.tostring(elem)) 
        f.write(b"</root>\n")      
        
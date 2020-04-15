import xml
import xml.etree.ElementTree as ET

def searchXML(filepath, tagname, tagvalue):
    for event, elem in ET.iterparse(filepath, events=("start","end")):
        if elem.tag == tagname and elem.text==tagvalue and event == "end":
            print('value is ',ET.tostring(elem))
            tree = ET.Element(elem)
            parent = tree.find('..')
            print(parent)
            elem.clear()
            break

def getchild(someelement):
    childtag = ...
    if someelement.tag == 'id':
        childtag ='end'
    else:
        for child in someelement:
            childtag = child
    return childtag

def usingparse(filepath,tagname,tagvalue):
    context = ET.iterparse(filepath, events=('start','end',))
    title = 'splittedfile'
    filename = format(title + ".xml")
    with open(filename, 'w') as f:
        f.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n")
        flag = True
        for event, elem in context:
            if flag is True:
                if elem.tag == 'employee':
                    for child in elem:
                        if child.tag == 'id' and child.text == '9':
                            print(ET.tostring(elem).decode("utf-8"))
                            f.write(ET.tostring(elem).decode("utf-8"))
                            flag = False
                            elem.clear
                            break
            else:
                break

big =r"G:\MyWorld\Python\HugeXMLFileGenerator\outputlarge.xml"
small = r"G:\MyWorld\Python\HugeXMLFileGenerator\outputsmall.xml"
#searchXML(small,'id','55')
usingparse(big,'id','9999')

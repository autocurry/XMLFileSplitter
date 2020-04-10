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
    tree =  ET.parse(filepath)
    root = tree.getroot()
    print('root: ',root.tag)
    elementtype = root
    value = 'something'

    while(elementtype.tag != 'employee' and value == 'something'):
        child  = getchild(elementtype)
        print('childtag:',child.tag)
        elementtype = child



    for id in root.iter('id'):
        if id.text == '55':
            break

big =r"G:\MyWorld\Python\HugeXMLFileGenerator\outputlarge.xml"
small = r"G:\MyWorld\Python\HugeXMLFileGenerator\outputsmall.xml"
#searchXML(small,'id','55')
usingparse(small,'id','55')

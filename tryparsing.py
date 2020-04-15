import xml.parsers.expat


big =r"G:\MyWorld\Python\HugeXMLFileGenerator\outputlarge.xml"
small = r"G:\MyWorld\Python\HugeXMLFileGenerator\outputsmall.xml"

p = xml.parsers.expat.ParserCreate()
with open(small, 'rt') as xml_file:
    while True:
        # Read a chunk
        chunk = xml_file.read(10000)
        if len(chunk) < 10000:
            # End of file
            # tell the parser we're done
            p.Parse(chunk, 1)
            # exit the loop
            break
        # process the chunk
        p.Parse(chunk)
        print(p)
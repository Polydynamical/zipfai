import xml.etree.ElementTree as ET
from codecs import open

target_file = open("sample.xml", mode="r", encoding="unicode-escape")

tree = ET.parse(target_file)

var = ET.tostring(tree.getroot(), encoding='utf-8', method='text').decode("utf-8")


f = open('sample.xml', 'w')
f.write(var)
f.close()



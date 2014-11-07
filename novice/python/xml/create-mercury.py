import xml.dom.minidom
doc = xml.dom.minidom.parse('mercury.xml')
print doc.toxml('utf-8')

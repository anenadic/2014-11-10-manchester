import xml.dom.minidom

impl = xml.dom.minidom.getDOMImplementation()

doc = impl.createDocument(None, 'planet', None)
root = doc.documentElement
root.setAttribute('name', 'Mars')

period = doc.createElement('period')
root.appendChild(period)

text = doc.createTextNode('686.98')
period.appendChild(text)

print doc.toxml('utf-8')

import xml.dom.minidom

src = '''<planet name="Venus">
  <period units="days">224.7</period>
</planet>'''

doc = xml.dom.minidom.parseString(src)
print doc.toxml('utf-8')

import xml.dom.minidom

src = '''<heavenly_bodies>
  <planet name="Mercury"/>
  <planet name="Venus"/>
  <planet name="Earth"/>
  <moon name="Moon"/>
  <planet name="Mars"/>
  <moon name="Phobos"/>
  <moon name="Deimos"/>
</heavenly_bodies>'''

doc = xml.dom.minidom.parseString(src)
for node in doc.getElementsByTagName('moon'):
    print node.getAttribute('name')


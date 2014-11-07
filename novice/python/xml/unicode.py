import xml.dom.minidom

my_xml = '''<name>Donald Knuth</name>'''
my_doc = xml.dom.minidom.parseString(my_xml)
name = my_doc.documentElement.firstChild.data
print 'name is:', name
print 'but name in full is:', repr(name)

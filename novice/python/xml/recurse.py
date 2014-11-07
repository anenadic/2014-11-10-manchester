import xml.dom.minidom

src = '''<solarsystem>
<planet name="Mercury"><period units="days">87.97</period></planet>
<planet name="Venus"><period units="days">224.7</period></planet>
<planet name="Earth"><period units="days">365.26</period></planet>
</solarsystem>
'''

def walkTree(currentNode, indent=0):
    spaces = ' ' * indent
    if currentNode.nodeType == currentNode.TEXT_NODE:
        print spaces + 'TEXT' + ' (%d)' % len(currentNode.data)
    else:
        print spaces + currentNode.tagName
        for child in currentNode.childNodes:
            walkTree(child, indent+1)

doc = xml.dom.minidom.parseString(src)
walkTree(doc.documentElement)

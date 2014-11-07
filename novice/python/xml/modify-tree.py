import re, xml.dom.minidom

# func:start
def emphasizeText(doc, para, textNode):

    # Look for optional spaces, a word, and the rest of the paragraph.
    m = re.match(r'^(\s*)(\S*)\b(.*)$', str(textNode.data))
    if not m:
        return
    leadingSpace, firstWord, restOfText = m.groups()
    if not firstWord:
        return

    # If there's text after the first word, re-save it.
    if restOfText:
        restOfText = doc.createTextNode(restOfText)
        para.insertBefore(restOfText, para.firstChild)

    # Emphasize the first word.
    emph = doc.createElement('em')
    emph.appendChild(doc.createTextNode(firstWord))
    para.insertBefore(emph, para.firstChild)

    # If there's leading space, re-save it.
    if leadingSpace:
        leadingSpace = doc.createTextNode(leadingSpace)
        para.insertBefore(leadingSpace, para.firstChild)

    # Get rid of the original text.
    para.removeChild(textNode)
# func:end

# emphasize:start
def emphasize(doc):
    paragraphs = doc.getElementsByTagName('p')
    for para in paragraphs:
        first = para.firstChild
        if first.nodeType == first.TEXT_NODE:
            emphasizeText(doc, para, first)
# emphasize:end

# test:start
if __name__ == '__main__':

    src = '''<html><body>
<p>First paragraph.</p>
<p>Second paragraph contains <em>emphasis</em>.</p>
<p>Third paragraph.</p>
</body></html>'''

    doc = xml.dom.minidom.parseString(src)
    emphasize(doc)
    print doc.toxml('utf-8')
# test:end

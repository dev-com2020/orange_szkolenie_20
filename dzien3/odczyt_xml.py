import xml.dom.minidom

doc = xml.dom.minidom.parse("sample.xml")
print(doc.nodeName)
print(doc.firstChild.tagName)

new_exp = doc.createElement("expertise")
new_exp.setAttribute("name", "Big Data")
doc.firstChild.appendChild(new_exp)
print(doc.toxml())

exp = doc.getElementsByTagName("expertise")
print(exp.length)

for skill in exp:
    print(skill.getAttribute("name"))

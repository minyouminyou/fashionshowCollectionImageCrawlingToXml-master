# <Person date="2017-04-22" time="14:03:00">
#
# <name>홍길동</name>
#
# <age>22</age>
#
# <adress>대구</adress>
#
# </Person>



from xml.etree.ElementTree import Element,dump,SubElement,ElementTree
from lxml import etree
n =1
person=Element('Person')
index = Element(str(n))
name=Element('name')
name.text='홍길동'
name.attrib["index"]=str(n)
person.append(name)

age=Element('age')

age.text='22'

person.append(age)

SubElement(person,'adress').text="대구"

no=Element('no')
no.text='17'

person.insert(1,no)

person.remove(no)

person.attrib['date']='2017-04-22'
doc = etree.parse()

print(etree.tostring(doc), encoding='UTF-8', xml_declaration=True,
                         pretty_print=True)
dump(person)
ElementTree(person).write('c:\person.xml')


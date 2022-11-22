import re

p = re.compile('[a-z]+')

m1 = p.match('3pa2bc')
print(m1)
m2 = p.search('3pa2bc')
print(m2)
m3 = p.findall('3pa2bc')
print(m3)
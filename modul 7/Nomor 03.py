import re

f = open("Indonesia.txt", "r")
p = r'di\s[\w\.-]+'
string3 = re.findall(p, f.read())
print (string3)

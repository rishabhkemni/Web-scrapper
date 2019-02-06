from urllib.request import urlopen
import re
u='https://www.safaribooksonline.com'
print('1')
w=urlopen(u)
print('2')
h=str(w.read())
print('3')
print(h)
l=re.findall(r"((http|ftp)s?://[\w\.-]+)",h)
print('4')
print(l)
for i in l:
    print(i[0])
    
x=re.findall(r"((http|ftp)s?://.*?)",h)
y=re.findall(r"((http|ftp)s?://.*?)\w",h)
print(x)
print(y)


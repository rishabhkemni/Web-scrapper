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
###2
##
####u='https://www.safaribooksonline.com'
####print('1')
####w=urlopen(u)
####print('2')
####f=open(r"f:\rk.txt",'wt')
####x=str(w.read())
####print('3')
####f.write((x))
######f.close()
####print('done sir ji')
##
###3
##
####f=open(r"f:\r1.txt",'wt')
####print('name-:',f.name)
####print('closed?',f.closed)
####print('opening in ',f.mode)
####f.close()
####print('closed',f.closed)
####
####
####f=open(r'f:\r1.txt','w')
####s=input('text daalo')
####f.write(s)
####f.write('\n hi i m rishi')
####f.close()
####print('done')
####
####
#####4
####
####f=open(r'f:\r1.txt','w')
####c=0
####while c<5:
####    s=input('text please')
####    f.write(s+'\n')
####    c=c+1
####f.close()
####print('done')
##
##
###5
##
####f=open(r'f:\r1.txt','a')
####while True:
####    s=input('text please sir')
####    f.write((s+'\n'))
####    c=input('exit ke liye x')
####    if c=='x' or c=='X':
####        break
####    else:
####        continue
####f.close()
####print('done')
##
##
##
###6
####f=open(r'f:\r1.txt','r')
####s=f.read()
####f1=open(r'f:\r2.txt','w')
####f1.write(s)
####f1.close()
####f.close()
####print('done')
##
###7
####f=open(r'f:\r2.txt','r')
####s=f.read(10)
####print('reading---:  ',s)
####s=f.read(15)
####print('reading---:  ',s)
####s=f.read(5)
####f.close()
####print('done')
##
###8
##with open(r'f:\r2.txt','r') as o:
##    for l in o:
##        s=l
##        print('string:',s,'data type-:',type(s))
##

import datetime
from datetime import *
f=open("books.txt","r+")
f1=open("books1.txt","w+")
f2=open("books2.txt","w+")
f3=open("books3.txt","w+")
data=f.read()
data=data.split('\n')
ls=[]
for x in data:
    k=x.split(',')
    if 'Comedy' in k[4]:
        ls.append(k)
ls=sorted(ls,key=lambda x: x[0] )
for x in ls:
    f1.write(",".join(x))
    f1.write("\n")
f1.close()
ls=[]
for x in data:
    k=x.split(',')
    if int(k[5])>100:
        l=str(k[1])
        l=l.split('-')
        if l[0]=='2020':
            ls.append(k)
ls=sorted(ls,key=lambda x: datetime.strptime(x[1]),"")
for x in ls:
    f2.write(",".join(x))
    f2.write("\n")
f2.close()
ls=[]
for x in data:
    k=x.split(',')
    if 50000 <int(k[3])< 100000:
        ls.append(k)
ls=sorted(ls,key=lambda x: int(x[3]))
for x in ls:
    f3.write(",".join(x))
    f3.write("\n")
f3.close()
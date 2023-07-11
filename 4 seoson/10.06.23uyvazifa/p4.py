f=open("son.txt","r")
ls=f.readline()
k=ls.split( '.' and ' ')
for i in k:
    if i[0]>= 'A' and i[0] <= 'Z' :
       print(i)
    else :
        continue
f.close()
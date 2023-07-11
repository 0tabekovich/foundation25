f=open("son.txt","r")
c=0
for i in f.read():
    c+=int(i)
print(c)
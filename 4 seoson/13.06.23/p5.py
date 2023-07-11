file=open("Numbers.txt","r+")
data=file.read()
data=data.split('\n')
ls=[]
ls1=[]
for x in data:
    k=x.split()
    ls1.append([k[2],k[3],k[4]])
    if k[1] not in ls:
        ls.append([k[1],data.count(k[1])])
print(ls)
d=0
for x in ls1:
    d=-1
    for y in x:
        if x.count(y)==1:
            continue
        else :
            d=1
            break
    #if d==-1:
        #print(x)


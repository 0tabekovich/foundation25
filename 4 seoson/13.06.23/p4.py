file=open("Karta.txt","r+")
fayl=file.read()
ls=fayl.split('\n')
dc={}
ls1=[]
ls.pop(0)
for x in ls:
    k=x.split(',')
    ls1.append(k[5])
dc=dc.fromkeys(ls1,)
for x in ls1:
    dc[x]=ls1.count(x)
print(dc)
ls1.clear()
for x in ls:
    k=x.split(",")
    if 'visa' in k[1] :
        ls1.append([k[1],k[5]])
ls1=sorted(ls1,key=lambda x : x[1],)
print(ls1)
j=['1','2','3','4','5','6','7','8','9','0']
for x in ls:
    k=x.split(',')
    for x in j:
        d=-1
        if x in k[0]:
            continue
        else :
            d=1
            break
    if d==-1:
        print(f"{k[0]} {k[5]} {k[2]} {k[4]}")

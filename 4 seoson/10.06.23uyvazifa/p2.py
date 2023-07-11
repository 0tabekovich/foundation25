n=int(input("n= "))
f=open("son.txt","w+")
k=0
i=2
while i<=n:
    k=-1
    for x in range(2,i):
        if i%x==0:
            k=1
            break
        else :
            continue
    if k==-1:
        f.write(str(i))
    i=i+1
import os
n=int(input("n= "))
f=open("son.txt","a")
ls=str()
k,c=0,0
if n%2==1:
    for x in range(1,n+1):
        k=x
        c=0
        while k:
            f.write(str(x))
            if k!=1:
                f.write("+")
            else:
                f.write("=")
            c+=x
            k-=1
        f.write(str(c))
        f.write('\n')
else :
    for x in range(n,0,-1):
        k=x
        c=0
        while k:
            f.write(str(x))
            if k!=1:
                f.write("+")
            else:
                f.write("=")
            c+=x
            k-=1
        f.write(str(c))
        f.write('\n')
f.close()
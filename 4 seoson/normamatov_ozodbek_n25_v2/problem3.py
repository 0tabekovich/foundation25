n=input("satr ")
ls=n.split()
k=0
for x in ls:
    if x.isalpha() :
        k+=1
    else :
        break
if k>=3:
    print("True")
else :
    print("False")
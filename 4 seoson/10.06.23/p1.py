import os
d=3
c=0
while d:
    filename=input("fayl nomini kiriting ")
    try :
        f=open(filename,"x")
        c+=1
    except:
        print("fayl mavjud edi")
    else :
        print("fayl yaratildi")
    d-=1
print(f"{c}ta papka yaratildi")
import pickle
import os
file=open("player.dat",'rb+')
while True:
    res=pickle.load(file)
    if res==None:
        break
    if res[1]<30:
        res[3]+=5000
    else :
        res[3]=res[3]-5000
 while True:
    res=pickle.load(file)
    if res==None:
        break
    print(f"nomi {res[0]}")
    print(f"yoshi {res[1]}")
    print(f"club {res[2]}")
    print(f"salary {res[3]}")

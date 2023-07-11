import pickle
import os
file=open("player.dat",'wb')
while True:
    os.system("cls")
    temp=input("Faylga malumot qo'shish uchun Yes ni tugatish uchun No ni bosing ")
    if temp.lower()=='yes':
        name=input("futbolchinig ismini kiriting ")
        age=int(input("yoshini kiriting "))
        club=input("jamosini kiriting ")
        salar=int(input("Maoshini kiriting "))
        pickle.dump([name,age,club,salar],file)
    else :
        break
file.close()
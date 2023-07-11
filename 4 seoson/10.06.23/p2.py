import os
f=open("FULL_NAME.txt","wb+")
st=list()
st=f.readlines()
k=open("new_names.txt","rb+")
sorted(st,key=lambda x:x , )
print(st)
n=input("satr ")
ls=n.split()
f=open("FILE.txt","w")
st=""
sana=ls[0].split('.')
vaqt=ls[1].split(':')
st+=str(int(sana[0]))
match sana[1]:
    case "01":
        st+=" January "
    case '02':
        st+=' february '
    case '03':
        st += ' march '
    case '04':
        st += ' april '
    case '05':
        st += ' may '
    case '06':
        st += ' june '
    case '07':
        st += ' july '
    case '08':
        st += ' august '
    case '09':
        st += ' september '
    case '10':
        st += ' october '
    case '11':
        st += ' november '
    case '12':
        st += ' december '
st+=sana[2]
st+=" year "
st+=str(int(vaqt[0]))
if int(vaqt[0])==1:
    st+='  hour '
else :
    st+=' hours '
st+=str(int(vaqt[1]))
if int(vaqt[1])==1:
    st+=' minute'
else :
    st+=' minutes'
f.write(st)
f.close()
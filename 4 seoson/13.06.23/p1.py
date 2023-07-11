n=input("oyni birinchi sanasini kiriting ")
k=int(input("qaysi kunni topmoqchisiz "))
l=0
match n:
    case 'dushanba':
        l=1
    case 'seshanba ':
        l=2
    case 'chorshanba':
        l=3
    case 'payshanba ':
        l=4
    case 'juma':
        l=5
    case 'shanba ':
        l=6
    case 'yakshanba ':
        l=7
d=(k-l)%7
match d:
    case 1:
        print("dushanba")
    case 2:
        print("sehanba")
    case 3:
        print("chorshanba")
    case 4:
        print("payshanba")
    case 5:
        print("juma")
    case 6:
        print("shanba")
    case 7:
        print("yakshanba")

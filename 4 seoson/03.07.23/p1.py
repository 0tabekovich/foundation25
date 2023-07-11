class bank:
    self.user=[]
    def royxatdan_otish():
        F.I.SH=input("FISH ")
        age=int(input("age "))
        jinsi=input("jinsi ")
        tel=int(input("telefon raqam(996787290)"))
        Email=input("Email ")
        parol=int(input("parol "))
        adress=input("Adress ")
        pasport_raqami=input("pasport raqami ")
        pochta=int(input("Pochta indeksi "))
        self.user.append([F.I.SH,age,jinsi,tel,Email,parol,adress,pasport_raqami,pochta])
    def kirish_qismi(self):
        self.k=input("Emailni kiriting ")
        n=int(input("parolni kiriting "))
        for x in self.user:
            if x[4]==self.k :
                if x[5]==n:
                    self.__bosh_menyu()
                else:
                    print("parol xato kiritdingiz")
            else:
                print("Email xato kiritdingiz")
    def __bosh_menyu(self):
        print("1.Kredit olish\n2.Kredit hisoblash kalkulatori\n3.Parolni ozgartirish")
        i=int(input(">>>"))
        match i:
            case 1:
                pass
            case 2:
                pass
            case 3:

                l=int(input("yangi parolni kiriting "))
                for x in self.user:
                    if x[4]==self.k
                        x[5]=l

class Soliq:

    __davlat_gaznasi=0
    def royxatdan_otish(self):
        self.user = []
        FI_SH=input("F.I.SH ")
        age=int(input("Yoshi "))
        sex=input("Jinsi ")
        phone=input("Phone number ")
        Email=input("Email ")
        password=int(input("Create password "))
        adress=input("Adress ")
        pasport=input("Pasport number ")
        mail_index=input("Mail index ")
        self.user.append([FI_SH,age,sex,phone,Email,password,adress,pasport,mail_index])
        self.kirish_qismi()
    def kirish_qismi(self):
        self.Email=input("Put your email ")
        password=int(input("put your password "))
        for x in self.user:
            if self.Email==x[4] and password==x[5]:
                print("You are logged in!")
                self.__bosh_menyu()
            else:
                print("\tEamil or password are not found!\n\tPlease try again ")
                self.kirish_qismi()
    def __bosh_menyu(self):
        print("1.Tax payment \n2.Tax calculator \n3.Change password")
        n=int(input(">>>"))
        match n:
            case 1:
                k=int(input("Karta raqamini kiriting "))
                j=int(input("Smsdan yuborilgan kodni kiriting "))
                if j>999 and j<10000:
                    l=int(input("To'lov summasini kiriting "))
                    Soliq.__davlat_gaznasi+=l
                    print("To'lov muvaffaqiyatli amalga oshirildi! ")
                else:
                    print("No'tog'ri kodni kiritdingiz ")

            case 2:
                #1 sotix yer uchun ortacha soliq = 56500 so'm
                kv=float(input("Yer maydoningizni kiriting(sotixda) "))
                print(f"Hurmatli fuqori siz {kv} sotix yeringiz uchun 1 yilga {56500*kv} so'm etib belgilangan.")
            case 3:
                for x in self.user:
                    if x[4]==self.Email :
                        new_password=int(input("Yangi parolni kiriting "))
                        x[5]=new_password
        self.__bosh_menyu()


k=Soliq()
k.royxatdan_otish()

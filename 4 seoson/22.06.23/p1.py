class Mashina:
    def __init__(self,yoqil):
        self.__yoqilgi=yoqil
        self.__yurgan_masofa=100
        self.hamyon=0
    def mijoz(self,sum,yuradigan_yoli):
        #100 km ga 1l sarf boladi
        if (self.__yoqilgi-(yuradigan_yoli/100))>0:
            print(f"{yuradigan_yoli} kmga mijoz olindi , u hamyonga {sum}som qoshdi ")
            self.hamyon+=sum
            self.__yoqilgi-=yuradigan_yoli/100
            self.__yurgan_masofa+=yuradigan_yoli
        else:
            print(f"bizda {self.__yoqilgi}l yoqilgi qoldi va u {yuradigan_yoli}ga yetmaydi")
    def check_hamyon(self):
        print(f"hamyonda {self.hamyon} sum bor")
    def check_yoqilgi(self):
        print(f"bizda {self.__yoqilgi}l yoqilgi qoldi")

    def yurgan_yol(self):
        print(f"{self.__yurgan_masofa}km boldi")
    def zaprafka(self,qancha_yoqilgi_olish):
        #yoqilgi 1l=20sum
        if qancha_yoqilgi_olish*20<self.hamyon:
            Mashina.check_yoqilgi(self)
            self.__yoqilgi+=qancha_yoqilgi_olish
        else:
            print(f"bizda {qancha_yoqilgi_olish}l yoqilgiga pul mavjud emas")
            Mashina.check_hamyon(self)

taksi=Mashina(15)
taksi.mijoz(25,100)
taksi.check_hamyon()
taksi.check_yoqilgi()
taksi.zaprafka(1)
taksi.yurgan_yol()

class hayvon:
    def __init__(self):
        self._energy=0
    def ovqatlanish(self,x):
        if self._energy+x<=100:
            print(f"hayvon {x}kkal bolgan ovqat yedi")
            self._energy+=x
        elif self._energy<100:
            self._energy=100
        else:
            print("100kkal bor")
    def chech_kkal(self):
        print(f"hayvonda hozir {self._energy}kkal mavjud")
class ovqat(hayvon):
    def __init__(self,beda,som):
        self.__beda=beda
        self.__somon=som
    def bedaberish(self):
        hayvon.ovqatlanish(self.__beda)
    def somonberish(self):
        hayvon.ovqatlanish(self.__somon)
s=ovqat(45,55)
s.bedaberish()
s.somonberish()
s.chech_kkal()

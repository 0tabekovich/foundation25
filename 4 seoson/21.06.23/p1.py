class Bus:
    def __init__(self):
        self.passengers=0
        self.capacity=40
    def addpass(self,n):
        if (self.passengers+n) > self.capacity:
            print(f"{self.capacity-self.passengers} ta odam sig'adi {n} ta odamga joy yo'q")
        else:
            self.passengers=self.passengers+n
    def countpass(self):
        print(self.passengers)
    def removepass(self,k):
       if  (self.passengers-k)<0:
           print(f"avtobusda {k}ta odam mavjud emas, {self.passengers} ta odam bor ")
       else:
           self.passengers-=k
s=Bus()
s.addpass(39)
s.countpass()
s.addpass(2)
s.countpass()
s.removepass(40)
s.countpass()



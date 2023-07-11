import abc
class konditsioner(abc.ABC):
    @abc.abstractmethod
    def __init__(self,n,k,c,r):
        self.name=n
        self.kv=k
        self.country=c
        self.color=r
    @abc.abstractmethod
    def show_info(self):
        print(f"\t{self.name} konditsioeri haqida malumot")
        print(f"Rangi {self.color}")
        print(f"U {self.kv} metr kub. hajmli xonaga mo'ljanlangan")
        print(f"Bu konditsioner {self.country} davlatida ishlab chiqarilgan")

class AUX(konditsioner):
    def __init__(self,n,k,c,r):
        super().__init__(n,k,c,r)
    def show_info(self):
        super().show_info()

a=AUX("AUX",22,"XItoy","Oq")
a.show_info()
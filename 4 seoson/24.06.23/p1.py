import abc
class najot_talim(abc.ABC):
    def __init__(self):
        self.uquvchisoni=None
        self.ochilsana=None
        self.ishsoati=None
    @abc.abstractmethod
    def input_data(self,q,o,t,n):
        self.nomi=n
        self.uquvchisoni=q
        self.ochilsana=o
        self.ishsoati=t
    def show_info(self):
        print(f"\tNajot ta'limning {self.nomi} filiali haqida malumot")
        print(f"o'quvchilar soni {self.uquvchisoni}")
        print(f"ochilgan sanasi {self.ochilsana}")
        print(f"kunlik ishlash soati {self.ishsoati} soat ")
class chilonzor(najot_talim):
    def __init__(self):
        super().__init__()
    def input_data(self,q,o,t,n):
        super().input_data(q,o,t,n)
    def show_info(self):
        super().show_info()

s=chilonzor()
s.input_data(1200,"12.06.2019",18,"chilonzor")
s.show_info()


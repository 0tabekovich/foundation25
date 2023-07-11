class shape:
    def __init__(self,tomon1,tomon2):
        self.tomon1=tomon1
        self.tomon2=tomon2

    def show_info(self):
        print(f"Tomoni {self.tomon1} va {self.tomon2} ",end="")
class square(shape):
    def __init__(self):
        super().__init__(self.tomon1,self.tomon2)
        self.tomon2=tomon22
        self.tomon1=tomon1
    def show_info(self):
        super().show_info()
        print(f" bolgan shakl yuzasi {self.tomon1**2} perimetri esa {self.tomon1*4}")
class retangle(shape):
    def __init__(self,tomon1,tomon2):
        super().__init__(tomon1,tomon2)
    def show_info(self):
        super().show_info()
        print(f" bolgan shakl yuzasi {self.tomon1 * self.tomon2} perimetri esa {(self.tomon1+self.tomon2 )*2}")
class triangle(shape):
    def __init__(self,tomon3):
        super().__init__(self.tomon1, self.tomon2)
        self.tomon2 = tomon2
        self.tomon1 = tomon1
        self.tomon3=tomon3

    def show_info(self):
        super().show_info()
        print(f" bolgan shakl yuzasi {self.tomon1 * self.tomon2*self.tomon3} perimetri esa {self.tomon1 +self.tomon2 +self.tomon3}")

classshape=shape()
classshape.show_info()
classrec=retangle(4,3)
classrec.show_info()

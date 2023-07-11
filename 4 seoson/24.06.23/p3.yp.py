class triangle:
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
    def check_triangle(self):
        if self.a<0 or self.b<0 or self.c<0 :
            print("Manfiy tomon kiritilgan")
        elif self.a+self.c>self.b and self.a+self.b>self.c and self.c+self.b>self.a:
            print("Uchburchak yasash mumkin")
        else:
            print("Uchburchak yasab bolmaydi")

t=triangle(3,4,5)
t.check_triangle()

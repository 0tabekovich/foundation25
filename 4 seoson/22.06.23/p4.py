class country:
    def __init__(self):
        print("country class ishga tushdi")

    def language(self):
        print("Har bir davlatning o'z tili mavjud")
    def area(self):
        print("har bir davlat maydoniga ega ")
    def population(self):
        print("har bir davlatninig o'z aholisi soni mavjud")

class russia(country):
    def __init__(self,name,area,l):
        self.name=name
        self.__area=area
        self.__population=0
        self.lan=l
    def add_population(self,x):
        self.__population+=x
    def language(self):
        print(f"{self.name} davlat tili {self.lan}")
    def area(self):
        print(f"{self.name}davlat yer maydoni {self.__area} kv.km")
    def population(self):
        print(f"{self.name} davlat aholisi {self.__population} millon kishi ")


class canada(country):
    def __init__(self, name, area, l):
        self.name = name
        self.__area = area
        self.__population = 0
        self.lan = l

    def add_population(self, x):
        self.__population += x

    def language(self):
        print(f"{self.name} davlat tili {self.lan}")

    def area(self):
        print(f"{self.name} davlat yer maydoni {self.__area} kv.km")

    def population(self):
        print(f"{self.name} davlat aholisi {self.__population} millon kishi ")

c=russia("rossiya",234,"rus tili")
c.area()
c.add_population(120)
c.language()
c.population()
c=canada("canada",122,"english tili")
c.area()
c.add_population(60)
c.language()
c.population()
c=country()
c.area()
c.language()
c.population()
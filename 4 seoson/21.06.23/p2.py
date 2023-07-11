class Bus:
    def __init__(self, addList):
        self.capacity = 40
        self.passengers_list = list()
        self.address_list = addList

    def addPas(self, passenger):
        if len(self.passengers_list) == self.capacity:
            print(f"avtobusda bo'sh joy mavjud emas")
        elif passenger.get_address() in self.address_list and passenger.fromAddress in self.address_list:
            self.passengers_list.append(passenger)

    def outPas(self):
        for x in self.passengers_list:
            for y in self.address_list:






    def getCountPas(self):
        return len(self.passengers_list)

    def getEmptyCount(self):
        return self.capacity - len(self.passengers_list)


class Passenger:
    def __init__(self, name, fromAddress, address):
        self.name = name
        self.fromAddress = fromAddress
        self.address = address

    def get_address(self):
        return self.address

    def get_fromAddress(self):
        return self.fromAddress

    def get_name(self):
        return self.name

l = ["Chilonzor", "Olmazor", "Bektemir", "Yakkasaroy"]
b = Bus(l)
p1 = Passenger("p1","Olmazor", "Chilonzor")
p2 = Passenger("p2","Chilonzor", "Bektemir")
b.addPas(p1)
b.addPas(p2)

b.outPas()

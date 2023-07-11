class battery:
    def __init__(self):
        self._batter=100
    @property
    def name(self):
        return self._batter
    @name.setter
    def name(self):
        self._batter-=30
    @name.getter
    def name(self):
        print(f"bateriya korsatkichi {self._batter}%")
    @name.deleter
    def name(self):
        print("batareya ochirildi")
        del self._batter

laptop=battery()
print(laptop.name)
del laptop.name()

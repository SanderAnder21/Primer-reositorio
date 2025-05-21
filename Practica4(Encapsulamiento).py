class Pisto:
    def __init__(self, hielera, hielera2):
        self.__hielera = hielera
        self.hielera2 = hielera2
    def pistear_1(self):
        self.__hielera = "Vaciar"
        return self.__hielera
    def pistear_2(self):
        self.hielera2 ="Mah, está vacia"
        return self.hielera2
fiesta = Pisto("Cartón en hielera", "Unas cuantas frias")
print(fiesta.pistear_2())
print(fiesta.pistear_1)        
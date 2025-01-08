class car:
    __marca = None
    __km = None
    def __init__(self, marca, kilometratge):
        self.__marca = marca
        self.__km = kilometratge
        print("car created: ",self.__marca, " / ", self.__km)

    @property    
    def Marca(self):
        return self.__marca
    @Marca.setter
    def Marca(self,marca):
        self.__marca = marca    
    @property
    def km(self):
        return self.__km
    @km.setter
    def km(self,km):
        self.__km = km   

objCar = car("Volkswagen", 300)
print(objCar.km)
print(objCar.Marca)
objCar.Marca = "Ferrari"
objCar.km = 50000
print(objCar.km)
print(objCar.Marca)
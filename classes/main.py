class car:
    __marca = None
    __km = None
    def __init__(self, marca, kilometratge):
        self.__marca = marca
        self.__km = kilometratge
        print("car created: ",self.__marca, " / ", self.__km)
        
    def getMarca(self):
        return self.__marca
    def getkm(self):
        return self.__km

objCar = car("Volkswagen", 300)
print(objCar.getkm())
print(objCar.getMarca())

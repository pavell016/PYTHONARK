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
    @Marca.deleter    
    def Marca(self):
        print("Deleting Marca...")
        self.__marca = None     
    @property
    def km(self):
        return self.__km
    @km.setter
    def km(self,km):
        self.__km = km   
    @km.deleter    
    def km(self):
        print("Deleting km...")
        self.__km = None     

objCar = car("Volkswagen", 300) #crear objecte
print(objCar.km)
print(objCar.Marca)
objCar.Marca = "Ferrari"  #canviar atribut
objCar.km = 50000 # cambiar atribut
print(objCar.km)
print(objCar.Marca)
del objCar.Marca # eliminar atribut
del objCar.km #eliminar atribut
print(objCar.km)
print(objCar.Marca)
del objCar # eliminar objecte
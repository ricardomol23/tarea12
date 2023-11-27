class Vehicle:

    def __init__(self, speed_atributo, passengers_atributo, fuelType_atributo):
        self.speed = speed_atributo
        self.passengers = passengers_atributo
        self.fuelType = fuelType_atributo

    def go(self):
        print("El carro está en movimiento")

    def stop(self):
        print("El carro está quieto")

    def cambio_direccion(self):
        print("El carro ha cambiado de dirección")

class Car(Vehicle):
    def __init__(self, speed, passengers, fuelType, model_type_atributo, doors_atributo, autoMaker_atributo):
        Vehicle.__init__(self, speed, passengers, fuelType)
        self.model_type = model_type_atributo
        self.doors = doors_atributo
        self.autoMaker = autoMaker_atributo

    def radio(self):
        print("La radio está encendida")

    def plumillas(self):
        print("Las plumillas están prendidas")


carro = Car(100, 5, "gasolina", "sedán", 4, "Toyota")

carro.go()
carro.stop()
carro.cambio_direccion()
carro.radio()
carro.plumillas()
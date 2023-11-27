class Sensor:

    def __init__(self, valor_umbral):
        self.valor_umbral = valor_umbral

    def medir(self):
        return int(input("Introduce un valor: "))


class Timbre:

    def __init__(self):
        self.activado = False

    def activar(self):
        print("El timbre suena")

    def desactivar(self):
        print("El timbre se apaga")


class Alarma:

    def __init__(self, sensor, timbre):
        self.sensor = sensor
        self.timbre = timbre

    def comprobar(self):
        valor = self.sensor.medir()
        if valor > self.sensor.valor_umbral:
            self.timbre.activar()
        else:
            self.timbre.desactivar()


class AlarmaLuminosa(Alarma):

    def __init__(self, sensor, timbre):
        super().__init__(sensor, timbre)
        self.luz = None

    def comprobar(self):
        valor = self.sensor.medir()
        if valor > self.sensor.valor_umbral:
            self.timbre.activar()
            self.luz = Luz()
            self.luz.encender()
        else:
            self.timbre.desactivar()
            if self.luz:
                self.luz.apagar()


class Luz:

    def __init__(self):
        self.estado = False

    def encender(self):
        self.estado = True
        print("La luz se enciende")

    def apagar(self):
        self.estado = False
        print("La luz se apaga")


sensor = Sensor(50)
timbre = Timbre()
alarma = Alarma(sensor, timbre)
alarma_luminosa = AlarmaLuminosa(sensor, timbre)

for i in range(100):
    alarma.comprobar()
    alarma_luminosa.comprobar()

class Planetas:

    def __init__(self, masa_atributo, diametro_atributo, periodo_rotacion_atributo, periodo_traslacion_atributo, distancia_media_atributo, excentricidad_atributo):
        self.masa = masa_atributo
        self.diametro = diametro_atributo
        self.periodo_rotacion = periodo_rotacion_atributo
        self.periodo_traslacion = periodo_traslacion_atributo
        self.distancia_media = distancia_media_atributo
        self.excentricidad = excentricidad_atributo

    def imprimir_datos(self):
        print("Masa:", self.masa)
        print("Diámetro:", self.diametro)
        print("Período de rotación:", self.periodo_rotacion)
        print("Período de traslación:", self.periodo_traslacion)
        print("Distancia media:", self.distancia_media)
        print("Excentricidad:", self.excentricidad)


class Planeta(Planetas):

    def __init__(self, masa, diametro, periodo_rotacion, periodo_traslacion, distancia_media, excentricidad, nombre):
        super().__init__(masa, diametro, periodo_rotacion, periodo_traslacion, distancia_media, excentricidad)
        self.nombre = nombre


class Satelite(Planetas):

    def __init__(self, masa, diametro, periodo_rotacion, periodo_traslacion, distancia_media, excentricidad, nombre_atributo, planeta_atributo):
        super().__init__(masa, diametro, periodo_rotacion, periodo_traslacion, distancia_media, excentricidad)
        self.nombre = nombre_atributo
        self.planeta = planeta_atributo


# Ejemplos

sol = Planeta(1.989e30, 1.391e8, 25.92, 31557600, 1.496e11, 0.01671, "Sol")
tierra = Planeta(5.972e24, 1.2742e7, 23.93, 31557600, 1.496e11, 0.01671, "Tierra")
luna = Satelite(7.348e22, 3.474e6, 27.32, 27.321661, 3.844e8, 0.0549, "Luna", tierra)

# Impresión de datos

sol.imprimir_datos()
tierra.imprimir_datos()
luna.imprimir_datos()

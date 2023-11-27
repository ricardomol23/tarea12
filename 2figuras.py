class Figuras:

    def __init__(self, peso_atributo, color_atributo, nombre_atributo):
        self.peso = peso_atributo
        self.color = color_atributo
        self.nombre = nombre_atributo


class Cuadrado(Figuras):

    def __init__(self, lado_izquierdo_atributo, lado_abajo_atributo, peso=0, color="", nombre=""):
        Figuras.__init__(self, peso, color, nombre)
        self.lado_izquierdo = lado_izquierdo_atributo
        self.lado_abajo = lado_abajo_atributo

    def calcular_area(self):
        return self.lado_izquierdo * self.lado_abajo


class Circulo(Figuras):

    def __init__(self, radio_atributo, peso=0, color="", nombre=""):
        Figuras.__init__(self, peso, color, nombre)
        self.radio = radio_atributo

    def calcular_area(self):
        return 3.14 * self.radio ** 2


class Triangulo(Figuras):

    def __init__(self, base_atributo, altura_atributo, peso=0, color="", nombre=""):
        Figuras.__init__(self, peso, color, nombre)
        self.base = base_atributo
        self.altura = altura_atributo

    def calcular_area(self):
        return (self.base * self.altura) / 2


def main():
    cuadrado = Cuadrado(10, 20, 5, "Rojo", "Cuadrado 1")
    area_cuadrado = cuadrado.calcular_area()
    print(f"El área del cuadrado es {area_cuadrado}cm^2, su peso es {cuadrado.peso} kg, y su color es {cuadrado.color}.")

    circulo = Circulo(5, 2, "Azul", "Círculo 1")
    area_circulo = circulo.calcular_area()
    print(f"El área del círculo es {area_circulo}cm^2, su peso es {circulo.peso} kg, y su color es {circulo.color}.")

    triangulo = Triangulo(10, 20, 3, "Verde", "Triángulo 1")
    area_triangulo = triangulo.calcular_area()
    print(f"El área del triángulo es {area_triangulo}cm^2 , su peso es {triangulo.peso} kg, y su color es {triangulo.color}.")

main()

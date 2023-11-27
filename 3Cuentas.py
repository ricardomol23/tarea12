class Persona:
    def __init__(self, nombre_atributo, apellidos_atributo, cc_atributo):
        self.nombre = nombre_atributo
        self.apellidos = apellidos_atributo
        self.cc = cc_atributo


class Cuenta:
    def __init__(self, cliente_atributo, numero_cuenta_atributo):
        self.cliente = cliente_atributo
        self.numero_cuenta = numero_cuenta_atributo
        self.saldo = 0

    def ingresar(self, monto):
        self.saldo += monto

    def retirar(self, monto):
        pass  

    def actualizar_saldo(self):
        pass  


class CuentaCorriente(Cuenta):
    def __init__(self, cliente, numero_cuenta):
        Cuenta.__init__(self, cliente, numero_cuenta)
        self.interes_fijo = 1.5

    def actualizar_saldo(self):
        self.saldo += self.saldo * (self.interes_fijo / 100)


class CuentaAhorro(Cuenta):
    def __init__(self, cliente, numero_cuenta, interes_variable, saldo_minimo):
        Cuenta.__init__(self, cliente, numero_cuenta)
        self.interes_variable = interes_variable
        self.saldo_minimo = saldo_minimo

    def retirar(self, monto):
        if self.saldo - monto >= self.saldo_minimo:
            self.saldo -= monto
        else:
            print("No se puede retirar. Saldo mínimo necesario no alcanzado.")

    def cambiar_interes_variable(self, nuevo_interes):
        self.interes_variable = nuevo_interes

    def actualizar_saldo(self):
        self.saldo += self.saldo * (self.interes_variable / 100)


cliente1 = Persona("Juan", "Pérez", "123456789")


cuenta_corriente = CuentaCorriente(cliente1, "123456")
cuenta_ahorro = CuentaAhorro(cliente1, "789012", 2.0, 1000)


cuenta_corriente.ingresar(5000)
cuenta_corriente.actualizar_saldo()

cuenta_ahorro.ingresar(2000)
cuenta_ahorro.retirar(500)
cuenta_ahorro.actualizar_saldo()


print(f"Cuenta Corriente - Saldo: {cuenta_corriente.saldo}")
print(f"Cuenta Ahorro - Saldo: {cuenta_ahorro.saldo}")

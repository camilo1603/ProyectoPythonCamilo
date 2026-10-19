
# ZONA DE CLASES

class CuentaBancaria:

    # Constructor
    def __init__(self, saldo_inicial):
        self.__saldo = saldo_inicial

    # Get y set del saldo
    def get_saldo(self):
        return self.__saldo

    def set_saldo(self, nuevo_saldo):
        self.__saldo = nuevo_saldo

    # Metodo para consultar
    def consultar(self):
        return self.__saldo

    # Metodo para retirar
    def retirar_dinero(self, cantidad):
        if cantidad <= 0:
            return "El retiro debe ser mayor que cero."
        elif cantidad > self.__saldo:
            return "No hay saldo suficiente."
        else:
            self.__saldo -= cantidad
            return "Retiro exitoso."

    # Metodo para depositar
    def ingresar_dinero(self, cantidad):
        if cantidad <= 0:
            return "El deposito debe ser mayor que cero."
        else:
            self.__saldo += cantidad
            return "Deposito exitoso."

    # Metodo para mostrar informacion
    def mostrar_datos(self):
        return f"Saldo disponible: ${self.__saldo:.2f}"


# ZONA PRINCIPAL

saldo = float(input("Ingrese el saldo inicial: "))
cuenta = CuentaBancaria(saldo)

opcion = 0

while opcion != 4:
    print("\n===== MENU BANCARIO =====")
    print("1. Consultar saldo")
    print("2. Retirar dinero")
    print("3. Depositar dinero")
    print("4. Salir")

    opcion = int(input("Seleccione una opcion: "))

    if opcion == 1:
        print(cuenta.mostrar_datos())

    elif opcion == 2:
        cantidad = float(input("Cuanto desea retirar? "))
        mensaje = cuenta.retirar_dinero(cantidad)
        print(mensaje)
        print(cuenta.mostrar_datos())

    elif opcion == 3:
        cantidad = float(input("Cuanto desea depositar? "))
        mensaje = cuenta.ingresar_dinero(cantidad)
        print(mensaje)
        print(cuenta.mostrar_datos())

    elif opcion == 4:
        print("Gracias por utilizar el cajero.")

    else:
        print("Opcion incorrecta.")

print("Saldo final:", cuenta.get_saldo())

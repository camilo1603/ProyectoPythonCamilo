
# ZONA DE CLASES

class ControlTemperatura:

    # Constructor
    def __init__(self, habitacion, grados):
        self.__habitacion = habitacion
        self.__grados = grados
        self.__estado = ""

    # Get y set de habitacion
    def get_habitacion(self):
        return self.__habitacion

    def set_habitacion(self, nueva_habitacion):
        self.__habitacion = nueva_habitacion

    # Get y set de grados
    def get_grados(self):
        return self.__grados

    def set_grados(self, nuevos_grados):
        self.__grados = nuevos_grados

    # Metodo para evaluar la temperatura
    def evaluar_temperatura(self):
        if self.__grados < 18:
            self.__estado = "Fria"
            return "Encender calefaccion"
        elif self.__grados <= 25:
            self.__estado = "Optima"
            return "Temperatura adecuada"
        else:
            self.__estado = "Caliente"
            return "Encender aire acondicionado"

    # Metodo para mostrar informacion
    def mostrar_datos(self):
        return f"Habitacion {self.__habitacion}: {self.__grados} grados - {self.__estado}"


# ZONA PRINCIPAL

cantidad = int(input("Cuantas habitaciones desea revisar? "))

frias = 0
adecuadas = 0
calientes = 0

for numero in range(1, cantidad + 1):
    grados = float(input(f"Temperatura de la habitacion {numero}: "))

    habitacion = ControlTemperatura(numero, grados)

    accion = habitacion.evaluar_temperatura()
    print(accion)
    print(habitacion.mostrar_datos())

    if grados < 18:
        frias += 1
    elif grados <= 25:
        adecuadas += 1
    else:
        calientes += 1

print("\n===== INFORME DE TEMPERATURAS =====")
print("Habitaciones frias:", frias)
print("Habitaciones adecuadas:", adecuadas)
print("Habitaciones calientes:", calientes)

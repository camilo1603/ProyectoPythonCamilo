
# ZONA DE CLASES

class RegistroAcademico:

    # Constructor
    def __init__(self, codigo, notas):
        self.__codigo = codigo
        self.__notas = notas
        self.__promedio = 0
        self.__resultado = ""

    # Get y set del codigo
    def get_codigo(self):
        return self.__codigo

    def set_codigo(self, nuevo_codigo):
        self.__codigo = nuevo_codigo

    # Get y set de las notas
    def get_notas(self):
        return self.__notas

    def set_notas(self, nuevas_notas):
        self.__notas = nuevas_notas

    # Metodo para calcular el promedio
    def obtener_promedio(self):
        self.__promedio = sum(self.__notas) / len(self.__notas)
        return self.__promedio

    # Metodo para determinar el resultado
    def determinar_resultado(self):
        if self.__promedio < 3.0:
            self.__resultado = "Reprobado"
        elif self.__promedio < 4.0:
            self.__resultado = "Regular"
        elif self.__promedio <= 4.5:
            self.__resultado = "Bueno"
        else:
            self.__resultado = "Excelente"

        return self.__resultado

    # Metodo para mostrar informacion
    def mostrar_datos(self):
        return f"Estudiante {self.__codigo} - Promedio: {self.__promedio:.2f} - Resultado: {self.__resultado}"


# ZONA PRINCIPAL

cantidad = int(input("Cantidad de estudiantes: "))

reprobados = 0
regulares = 0
buenos = 0
excelentes = 0

for numero in range(1, cantidad + 1):
    print(f"\nEstudiante {numero}")

    notas = []

    for posicion in range(1, 5):
        nota = float(input(f"Ingrese la nota {posicion}: "))
        notas.append(nota)

    estudiante = RegistroAcademico(numero, notas)

    promedio = estudiante.obtener_promedio()
    resultado = estudiante.determinar_resultado()

    print(estudiante.mostrar_datos())

    if resultado == "Reprobado":
        reprobados += 1
    elif resultado == "Regular":
        regulares += 1
    elif resultado == "Bueno":
        buenos += 1
    else:
        excelentes += 1

print("\n===== ESTADISTICAS DEL CURSO =====")
print("Reprobados:", reprobados)
print("Regulares:", regulares)
print("Buenos:", buenos)
print("Excelentes:", excelentes)

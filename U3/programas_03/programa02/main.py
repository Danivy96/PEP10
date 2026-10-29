# imports de la librería estándar
import sys

# imports de librerías de terceros
# ?
# imports de módulos propios
import operaciones


# Definición de funciones principales
def principal():

    # """Función principal del programa"""
    print("Hola, este es el programa principal")
    num1 = float(input("Introduce el primer número: "))
    num2 = float(input("Introduce el segundo número: "))

    suma = operaciones.sumar(num1, num2)
    resta = operaciones.restar(num1, num2)
    multiplicar = operaciones.multiplicar(num1, num2)
    dividir = operaciones.division(num1, num2)

    print(f"Suma: {suma}")
    print(f"Resta: {resta}")
    print(f"Multiplicar: {multiplicar}")
    print(f"Dividir: {dividir}")


# Bloque para asegurar ejecución sólo si el archivo es el principal
if __name__ == "__main__":
    # Se pueden procesar argumentos, inicializar variables, etc.
    principal()

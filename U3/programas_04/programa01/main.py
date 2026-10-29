# imports de la librería estándar
import sys

# imports de librerías de terceros

# imports de módulos propios
from matematicas import operaciones, figuras, conversiones


def principal():
    """Función principal del programa"""
    print("Hola, este es el programa principal")

    while True:
        print("1. Operaciones ")
        print("2. Cálculo areas")
        print("3. Conversiones")
        print("4. Finalizar")

        opcion = int(input("Elige una opción del 1-4: "))

        match opcion:
            case 1:
                print("\nOPERACOINES")
                num1 = float(input("Introduce el primer número: "))
                num2 = float(input("Introduce el segundo número: "))
                print(f"Suma: {operaciones.sumar(num1, num2)}")
                print(f"Resta: {operaciones.restar(num1, num2)}")
                print(f"Multiplicación: {operaciones.multiplicar(num1, num2)}")
                print(f"División: {operaciones.division(num1, num2)}")

            case 2:
                print("\nCALCULAR ÁREA")
                print("1. Rectángulo")
                print("2. Triángulo")
                print("3. Círculo")
                opcion = int(input("Elige figura (1-3): "))

                if opcion == 1:
                    base = float(input("Introduce la base: "))
                    altura = float(input("Introduce la altura: "))
                    print(f"Área del rectángulo: {figuras.areaRect(base, altura)}")
                elif opcion == 2:
                    base = float(input("Introduce la base: "))
                    altura = float(input("Introduce la altura: "))
                    print(f"Área del triángulo: {figuras.areaTri(base, altura)}")
                elif opcion == 3:
                    radio = float(input("Introduce el radio: "))
                    print(f"Área del círculo: {figuras.areaCirc(radio)}")
                else:
                    print("Opción de figura no válida.")

            case 3:
                print("\nCONVERSIONES")
                print("1. Entero a Binario")
                print("2. Entero a Hexadecimal")
                print("3. Texto a Entero")
                opcion = int(input("Elige conversión (1-3): "))

                if opcion == 1:
                    num = int(input("Introduce un número entero: "))
                    print(f"Binario : {conversiones.binario(num)}")
                elif opcion == 2:
                    num = int(input("Introduce un número entero: "))
                    print(
                        f"Representación hexadecimal: {conversiones.hexadecimal(num)}"
                    )
                elif opcion == 3:
                    str = input("Introduce el texto numérico: ")
                    print(f"Conversión a entero: {conversiones.entero(str)}")
                else:
                    print("Opción no válida.")

            case 4:
                print("Finalizar programa")
                break


# Bloque para asegurar ejecución sólo si el archivo es el principal
if __name__ == "__main__":
    # Se pueden procesar argumentos, inicializar variables, etc.
    principal()

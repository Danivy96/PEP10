from math import radians, sin, cos, sqrt, pow


def menu():
    print("1. Seno de un ángulo")
    print("2. Coseno de un ángulo")
    print("3. Raíz cuadrada de un número")
    print("4. Potencia de dos números")
    print("5. Salir")


def principal():
    while True:
        menu()
        escoger = int(input("Escoge una opción del 1-5: "))
        if escoger >= 1 and escoger <= 4:
            match escoger:
                case 1:
                    grados = float(input("Introduce el ángulo en grados: "))
                    radianes = radians(grados)
                    resultado = sin(radianes)
                    print(f"El seno de {grados} grado es: {resultado}")
                    print("")

                case 2:
                    grados = float(input("Introduce el ángulo en grados: "))
                    radianes = radians(grados)
                    resultado = cos(radianes)
                    print(f"El coseno de {grados}grados es: {resultado}")
                    print("")

                case 3:
                    numero = float(input("Introduce un número: "))
                    if numero >= 0:
                        resultado = sqrt(numero)
                        print(f"La raíz cuadrada de {numero} es: {resultado}")
                    else:
                        print("No puede ser un número negativo")

                case 4:
                    base = float(input("Introduce la base: "))
                    exponente = float(input("Introduce el exponente: "))
                    resultado = pow(base, exponente)
                    print(f"El total es: {resultado}")
                    print("")

                case 5:
                    print("Finalizar programa")
                    print("")
                    break
        else:
            print("No has seleccionado un valor correcto, elige otra vez")


principal()

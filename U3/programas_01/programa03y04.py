import math


def area_circulo(radio):
    return math.pi * (radio**2)


def area_triangulo(base, altura):
    return (base * altura) / 2


def area_rectangulo(base, altura):
    return base * altura


def menu():
    print("1. Area de un circulo")
    print("2. Area de un tringulo")
    print("3. Area de un rectangulo")
    print("4. Finalizar")


def opcion1():
    while True:
        radio = float(input("Introduce el radio del circulo: "))
        if radio > 0:
            area = area_circulo(radio)
            print("El area del circulo es ", area)
            print("")
            break
        else:
            print("El radio no puede ser menor de 0")


def opcion2():
    while True:
        base = float(input("Introduce la base del triangul: "))
        altura = float(input("Introduce la altura del triangulo: "))

        if base > 0 and altura > 0:
            area = area_triangulo(base, altura)
            print("El area del triangulo es ", area)
            print("")
            break
        else:
            print("El valor introducido no puede ser menor de 0")


def opcion3():
    while True:
        base = float(input("Introduce la base del rectangulo: "))
        altura = float(input("Introduce la altura del rectangulo: "))

        if base > 0 and altura > 0:
            area = area_rectangulo(base, altura)
            print("El area del rectangulo es ", area)
            print("")
            break
        else:
            print("El valor introducido no puede ser menor de 0")


def principal():
    while True:
        menu()
        escoger = int(input("Escoge una opción del 1-4: "))
        if escoger >= 1 and escoger <= 4:
            match escoger:
                case 1:
                    opcion1()
                case 2:
                    opcion2()
                case 3:
                    opcion3()
                case 4:
                    print("Se ha cerrado el programa")
                    print("")
                    break
        else:
            print("No has seleccionado un valor correcto, elige otra vez")


principal()

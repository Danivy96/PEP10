import random

numSecreto = random.randrange(1, 21)
fallos = 0
print("Adivina un número entre el 1 y 20: ")

while True:
    num = int(input("Introduce un número: "))
    if fallos < 3:
        if num > numSecreto:
            print("El número secreto es menor")
            fallos += 1
        elif num < numSecreto:
            print("El número secreto es mayor")
            fallos += 1
        else:
            print(f"Enhorabuen!!!! El número era {num}")
            break
    else:
        print("HAS SOBREPASADO EL LÍMITE DE INTENTOS")

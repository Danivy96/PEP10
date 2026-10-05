adivinar = True

while True:
    num = int(input("Dame un número: "))

    if num == 45:
        print("¡Has dejado el bucle con éxito")
        break
    else:
        print("No has acertado, escoge otra vez")


adivinar2 = False

while adivinar != True:
    num2 = int(input("Dame un número: "))

    if num == 45:
        print("¡Has dejado el bucle con éxito")
        adivinar = True
    else:
        print("No has acertado, escoge otra vez")

pedirnumero = True

while True:
    num = int(input("Dame un número comprendido entre el 1 y 10: "))
    if 1 <= num <= 10:
        print("El número seleccionado es ", num)
        break
    else:
        print("El número", num, "no es válido")

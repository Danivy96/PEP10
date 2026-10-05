continuar = True
cont = 0
suma = 0

while True:
    num = int(input("Dame un número: "))
    if num != 0:
        suma += num
        cont += 1

    else:
        media = suma / cont
        print(f"La suma total de los números introducidos es {suma}")
        print(f"La media de los números introducidos es {media}")
        break

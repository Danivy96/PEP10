continuar = True

while True:
    num = int(input("Dame un número: "))

    if num <= 0 or num > 10:
        print("Numero no válido")
    else:
        for cont in range(1, num + 1):
            print(cont)
        break

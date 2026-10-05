continuar = True

while True:
    num = int(input("Dame un número: "))

    if num <= 0 or num > 10:
        print("Numero no válido")
    else:
        for cont in range(1, num + 1):
            multiplicar = cont * num
            print(f"{cont} X {num} = {multiplicar}")
        respuesta = input("Deseas introducir otro numero? (S/N): ")
        if respuesta == "S":
            continue
        elif respuesta == "N":
            break

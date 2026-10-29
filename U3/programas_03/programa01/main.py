import operaciones


def principal():

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


principal()

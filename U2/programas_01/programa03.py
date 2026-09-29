num1 = int(input("Dame un primer número: "))
num2 = int(input("Dame un segundo número: "))

if num2 == 0:
    print("No se puede dividir entre 0")
else:
    division = num1 / num2
    print("La división de " + str(num1) + " y " + str(num2) + " es :" + str(division))

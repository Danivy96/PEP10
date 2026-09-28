num1 = int(input("Dame un primer número: "))
num2 = int(input("Dame un segundo número: "))

if num1 == num2:
    print("Los números que has escogido coinciden!")
elif num1 > num2:
    print(num1, " es mayor que ", num2)
else:
    print(int(num1), " es menor que ", int(num2))

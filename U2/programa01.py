numPar = int(input("Dame un número par: "))
if numPar % 2 != 0:
    print(str(numPar) + " NO ES PAR")
else:
    print("El número " + str(numPar) + " es par")

numImpar = int(input("Dame un número impar: "))
if numImpar % 2 == 0:
    print(str(numImpar) + " NO ES IMPAR")
else:
    print("El númer es " + str(numImpar) + " es impar")

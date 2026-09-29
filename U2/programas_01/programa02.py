numPar = int(input("Dame un número par: "))
if numPar % 2 != 0:
    print(str(numPar) + " NO ES PAR")
else:
    numImpar = int(input("Dame un número impar: "))
    if numImpar % 2 == 0:
        print(str(numImpar) + " NO ES IMPAR")
    else:
        print("El número par escogido es: " + str(numPar))
        print("El númro impar escogido es: " + str(numImpar))

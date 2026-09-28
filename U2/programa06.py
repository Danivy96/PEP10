dia = int(input("Dame un día: "))
if dia < 0 or dia > 31:
    print("El día ", dia, " no es válido")
else:
    mes = int(input("Dame un mes: "))
    if mes < 0 or mes > 12:
        print("El mes ", mes, " no es válido")
    else:
        ano = int(input("Dame un año: "))
        if ano < 0:
            print("El año ", ano, " no es válido")
        else:
            print(dia, ".", mes, ".", ano)

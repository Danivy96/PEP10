anio = int(input("Dame una fecha en años: "))
if anio < 0:
    print(anio, " no es una fecha válida")
if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
    print(anio, " es bisiesto!!")
else:
    print(anio, " no es bisiesto :(")

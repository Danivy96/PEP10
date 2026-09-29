import random

print("1. Piedra")
print("2. Papel")
print("3. Tijera")
eleccion = int(input("Seleccione una opción (1, 2, o 3) : "))
eleccionPrograma = int(random.randrange(1, 3))

if eleccion == eleccionPrograma:
    print("EMPATE!")
elif (
    (eleccion == 1 and eleccionPrograma == 3)
    or (eleccion == 2 and eleccionPrograma == 1)
    or (eleccion == 3 and eleccionPrograma == 2)
):
    print("FELICIDADES! HAS GANADO A LA MÁQUINA!")
else:
    print("TE HA GANADO LA MÁQUINA")

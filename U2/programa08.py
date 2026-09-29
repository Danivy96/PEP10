import random

print("El primer jugador tira los dados: ")
tirada1 = int(random.randrange(1, 7))
print("Primera tirada: ", tirada1)
tirada2 = int(random.randrange(1, 7))
print("Segunda tirada: ", tirada2)
suma1 = tirada1 + tirada2
if tirada1 > tirada2:
    alto1 = tirada1
else:
    alto1 = tirada2

print("Suma total de los dados: ", suma1)
print("")

print("El segundo jugador tira los dados: ")
tirada3 = int(random.randrange(1, 7))
print("Primera tirada: ", tirada3)
tirada4 = int(random.randrange(1, 7))
print("Segunda tirada: ", tirada4)
suma2 = tirada3 + tirada4
if tirada3 > tirada4:
    alto2 = tirada3
else:
    alto2 = tirada4


print("Suma total de los dados: ", suma2)
print("")

if suma1 > suma2:
    print("El primer jugador es el ganador!")
elif suma1 < suma2:
    print("El segundo jugador es el ganador!")
elif suma1 == suma2:
    print("LOS DOS JUGADORES HAN EMPATADO!!")
    if alto1 > alto2:
        print("El primer jugador gana con un ", alto1)
    elif alto2 < alto1:
        print("El segundo jugador gana con un ", alto2)
    else:
        print(
            "LOS JUGADORES HAN EMPATADO TANTO EN EL TOTAL COMO EN EL VALOR MÁS ALTO!!!"
        )

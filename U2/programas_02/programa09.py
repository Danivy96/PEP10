import random

continuar = True
puntosJugador = 0

jugadaPC = random.randrange(17, 21 + 1)

while True:
    carta = random.randrange(1, 5 + 1)
    puntosJugador += carta
    print(f"Valor de tu carta: {carta}")
    print(f"Tu puntuación actual es {puntosJugador}")
    if puntosJugador > 21:
        print("LA MÁQUINA GANA! Has sobrepasado los 21 puntos")
        break
    else:
        respuesta = print("Quieres sacar otra carta? S/N : ")
        if respuesta == "S":
            continue
        elif respuesta == "N":
            break

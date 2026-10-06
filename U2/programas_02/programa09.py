import random

continuar = True
puntosJugador = 0

jugadaPC = random.randrange(17, 21 + 1)

while True:
    carta = random.randrange(1, 5 + 1)
    puntosJugador += carta
    print(f"Valor de la máquina: {jugadaPC}")
    print(f"Valor de tu carta: {carta}")
    print(f"Tu puntuación actual es {puntosJugador}")
    if puntosJugador < 21:
        respuesta = input("Quieres sacar otra carta? S/N : ").strip().upper()
        if respuesta.upper() == "S":
            continue
        elif respuesta.upper() == "N":
            if puntosJugador > jugadaPC and puntosJugador < 21:
                print(
                    f"ENHORABUENA!!! HAS GANADO CON UNA PUNTUACIÓN DE {puntosJugador} frente a su {jugadaPC}"
                )
                break
            elif puntosJugador == jugadaPC:
                print("HABÉIS EMPATADO!!")
            elif puntosJugador < jugadaPC and puntosJugador < 21:
                print(f"La máquina gana con {jugadaPC} frente a tu {puntosJugador}")
                break
    elif puntosJugador > jugadaPC and puntosJugador < 21:
        print(f"ENHORABUENA!!! HAS GANADO CON UNA PUNTUACIÓN DE {puntosJugador}")
    else:
        print("LA MÁQUINA GANA! Has sobrepasado los 21 puntos")
        break

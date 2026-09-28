horasA= int(input("Hora de salida:"))
minutosA= int(input("Minuto de salida:"))
segundosA= int(input("Segundo de salida:"))

segundosTot= int(input("Segundos totales transcurridos entre A y B: "))

total= (horasA*3600) + (minutosA*60) + segundosA + segundosTot
total = total%86400

horasB= int(total/3660)
minutosB= int((total%3660)/60)
segundosB= (int(total%60))

print("Llego a las ", horasB, minutosB, segundosB)
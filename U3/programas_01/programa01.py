def saludo(nombre, primer_apellido, segundo_apellido):
    print(f"{nombre}{primer_apellido}{segundo_apellido}")


nom = input("Introduce nombre: ")
ap1 = input("Introduce primer apellido: ")
ap2 = input("Introduce segundo apellido: ")

saludo(nom, ap1, ap2)

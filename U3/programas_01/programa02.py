def saludo(nombre, primer_apellido, segundo_apellido, curso="2ºDAW"):
    print(f"Hola {nombre} {primer_apellido} {segundo_apellido} de {curso}")


nom = input("Introduce nombre: ")
ap1 = input("Introduce primer apellido: ")
ap2 = input("Introduce segundo apellido: ")

saludo(nom, ap1, ap2)
saludo("Leda", "Oses", "Oliv", "2ºDAM")

curso = input("Introduce el curso del alumno: ")

saludo("Rafael", "A", "T", curso)

saludo(primer_apellido="Lopez", nombre="Juan", segundo_apellido="Perez", curso="Asir")

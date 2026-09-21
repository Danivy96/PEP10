var1 = 6
print(var1, " es un objeto de tipo" , type(6), " y apunt a ", type(var1))

var2 = var1
print(var2, " es un objeto de tipo" , type(6), " y apunt a ", type(var2))

print("var1 = var2: ", var1 is var2)
print("var1 =! var2: ", var1 is not var2)
print(var1, " está en la posición de memoria ", id(var1))
print(var2, " está en la posición de memoria ", id(var2))

var1 = "Hola"
print(var1, " es un objeto de tipo" , type("Hola"), " y apunt a ", type(var1))

print(isinstance(var1,int))
print(isinstance(var2,str))
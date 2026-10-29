mensahe = "Variable global"


def valLocal():
    mensajeLocal = "Variable local dentro de una función"
    print(mensajeLocal)


def valGlobal():
    global mensahe
    mensahe = "Variable global modificado dentro de una función"
    print(mensahe)


def valExt():
    mensajeExt = "Variable externa"

    def funInterna():
        nonlocal mensajeExt
        mensajeExt = "Variable externa moodificado con nonlocal"

    print(mensajeExt)
    funInterna()
    print(mensajeExt)


print(mensahe)
valLocal()
valGlobal()
valExt()

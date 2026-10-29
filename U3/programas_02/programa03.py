import platform
import os


def infoSistema():

    procesador = platform.processor()
    print(f"Procesador: {procesador if procesador else 'No disponible'}")

    sistema = platform.system()
    version = platform.release()
    print(f"Sistema Operativo: {sistema} {version})")

    nombreHost = platform.node()
    print(f"Nombre del host: {nombreHost}")

    directorio = os.getcwd()
    print(f"Directorio actual: {directorio}")


infoSistema()

import json
import os

def guardar_datos(ruta, datos):

    with open(ruta, "w") as archivo:

        json.dump(datos, archivo, indent=4)


def cargar_datos(ruta):

    if os.path.exists(ruta):

        with open(ruta, "r") as archivo:

            return json.load(archivo)

    return []

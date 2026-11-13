import os

from almacenamiento import guardar_datos, cargar_datos
from login import iniciar_sesion
from usuarios import registrar_usuario
from pacientes import registrar_paciente
from diagnosticos import registrar_consulta
from historia_clinica import consultar_historia


RUTA_DATOS = os.path.join(os.path.dirname(__file__), "data", "datos.json")


def inicializar_sistema():

    os.makedirs(os.path.dirname(RUTA_DATOS), exist_ok=True)

    if not os.path.exists(RUTA_DATOS):

        datos = {
            "usuarios": [{
                "identificacion": "0000",
                "nombres": "Admin",
                "apellidos": "Administrador",
                "telefono": "555 000111",
                "email": "admin@acmeclinic.com",
                "direccion": "Cl 185 # 26 - 85",
                "contrasena": "Admin123*",
                "rol": "administrativo"
            }],
            "pacientes": [],
            "consultas": []
        }

        guardar_datos(RUTA_DATOS, datos)


def main():

    inicializar_sistema()
    datos = cargar_datos(RUTA_DATOS)

    usuario = iniciar_sesion(datos["usuarios"])

    if usuario is None:
        return

    while True:

        print("\n===== CLINICA ACME =====")
        print("1. Registrar operador")
        print("2. Registrar paciente")
        print("3. Registrar consulta")
        print("4. Consultar historia clinica")
        print("5. Cerrar sesion")

        opcion = input("Seleccione una opcion: ")

        if opcion == "1":

            if usuario["rol"] == "administrativo":
                registrar_usuario(datos, RUTA_DATOS)
            else:
                print("No tiene permisos.")

        elif opcion == "2":

            if usuario["rol"] == "administrativo":
                registrar_paciente(datos, RUTA_DATOS)
            else:
                print("No tiene permisos.")

        elif opcion == "3":

            if usuario["rol"] == "medico":
                registrar_consulta(datos, RUTA_DATOS, usuario)
            else:
                print("No tiene permisos.")

        elif opcion == "4":
            consultar_historia(datos)

        elif opcion == "5":
            print("Sesion cerrada.")
            break

        else:
            print("Opcion incorrecta.")


if __name__ == "__main__":
    main()

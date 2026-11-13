from almacenamiento import guardar_datos

def registrar_usuario(datos, ruta_datos):

    print("\n===== REGISTRO DE OPERADOR =====")

    identificacion = input("Ingrese la identificacion: ").strip()

    for usuario in datos["usuarios"]:

        if usuario["identificacion"] == identificacion:

            print("\nEsta identificacion ya esta registrada")
            return

    nombres = input("Ingrese los nombres: ").strip()
    apellidos = input("Ingrese los apellidos: ").strip()
    telefono = input("Ingrese el telefono: ").strip()
    email = input("Ingrese el correo corporativo: ").strip()
    direccion = input("Ingrese la direccion: ").strip()
    contrasena = input("Asigne una contrasena: ").strip()

    print("\nSeleccione el rol:")
    print("1. Medico")
    print("2. Administrativo")

    opcion = input("Ingrese una opcion: ")

    if opcion == "1":
        rol = "medico"

    elif opcion == "2":
        rol = "administrativo"

    else:
        print("\nOpcion incorrecta. No se registro el operador")
        return

    for usuario in datos["usuarios"]:

        if usuario["email"].lower() == email.lower():

            print("\nEste correo ya esta registrado")
            return

    nuevo_usuario = {
        "identificacion": identificacion,
        "nombres": nombres,
        "apellidos": apellidos,
        "telefono": telefono,
        "email": email,
        "direccion": direccion,
        "contrasena": contrasena,
        "rol": rol
    }

    datos["usuarios"].append(nuevo_usuario)

    guardar_datos(ruta_datos, datos)

    print("\nOperador registrado correctamente")

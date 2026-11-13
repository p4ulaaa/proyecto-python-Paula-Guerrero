from almacenamiento import guardar_datos

def registrar_paciente(datos, ruta_datos):

    print("\n===== REGISTRO DE PACIENTE =====")

    identificacion = input("Ingrese la identificacion: ").strip()

    for paciente in datos["pacientes"]:

        if paciente["identificacion"] == identificacion:

            print("\nEste paciente ya esta registrado")
            return

    nombres = input("Ingrese los nombres: ").strip()
    apellidos = input("Ingrese los apellidos: ").strip()
    telefono = input("Ingrese el telefono: ").strip()
    email = input("Ingrese el correo electronico: ").strip()
    direccion = input("Ingrese la direccion: ").strip()
    genero = input("Ingrese el genero: ").strip()
    estado_civil = input("Ingrese el estado civil: ").strip()

    nuevo_paciente = {
        "identificacion": identificacion,
        "nombres": nombres,
        "apellidos": apellidos,
        "telefono": telefono,
        "email": email,
        "direccion": direccion,
        "genero": genero,
        "estado_civil": estado_civil
    }

    datos["pacientes"].append(nuevo_paciente)

    guardar_datos(ruta_datos, datos)

    print("\nPaciente registrado correctamente")

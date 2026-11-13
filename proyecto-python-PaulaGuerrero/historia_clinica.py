
def consultar_historia(datos):

    print("\n===== CONSULTA DE HISTORIA CLINICA =====")

    identificacion = input("Identificacion del paciente: ").strip()

    paciente_encontrado = None

    for paciente in datos["pacientes"]:

        if paciente["identificacion"] == identificacion:
            paciente_encontrado = paciente
            break

    if paciente_encontrado is None:
        print("\nNo se encontro el paciente.")
        return

    print("\n===== HISTORIA CLINICA =====")

    print("Identificacion:", paciente_encontrado["identificacion"])
    print("Nombres:", paciente_encontrado["nombres"])
    print("Apellidos:", paciente_encontrado["apellidos"])
    print("Telefono:", paciente_encontrado["telefono"])
    print("Correo:", paciente_encontrado["email"])
    print("Direccion:", paciente_encontrado["direccion"])
    print("Genero:", paciente_encontrado["genero"])
    print("Estado civil:", paciente_encontrado["estado_civil"])

    hay_consultas = False

    for consulta in datos["consultas"]:

        if consulta["paciente_identificacion"] == identificacion:

            hay_consultas = True

            receta = consulta["prescripcion"]

            print("\n--------------------------------")
            print("Fecha:", consulta["fecha"])
            print("Medico:", consulta["medico_nombre"])
            print("Sintomas:", consulta["sintomas"])
            print("Diagnostico:", consulta["diagnostico"])

            print("\nPRESCRIPCION")
            print("Medicamento:", receta["medicamento"])
            print("Cantidad:", receta["cantidad"])
            print("Dosis diaria:", receta["dosis_diaria"])
            print("Duracion:", receta["duracion_dias"], "dias")

    if not hay_consultas:
        print("\nEste paciente aun no tiene consultas registradas.")

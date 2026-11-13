def iniciar_sesion(usuarios):

    print("\n===== LOGIN CLINICA ACME =====")

    correo = input("Ingrese su correo: ").strip()
    contrasena = input("Ingrese su contrasena: ").strip()

    for usuario in usuarios:

        if (usuario["email"].strip().lower() == correo.lower()
                and usuario["contrasena"] == contrasena):

            print("\nInicio de sesion exitoso")

            return usuario

    print("\nCorreo o contrasena incorrectos")

    return None


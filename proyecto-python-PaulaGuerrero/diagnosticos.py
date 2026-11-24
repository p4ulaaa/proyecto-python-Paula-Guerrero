from datetime import datetime
import os
from almacenamiento import guardar_datos


def registrar_consulta(datos, ruta_datos, medico):

    print("\n===== REGISTRO DE DIAGNOSTICO =====")

    identificacion = input("Identificacion del paciente: ").strip()

    paciente_encontrado = None

    for paciente in datos["pacientes"]:
        if paciente["identificacion"] == identificacion:
            paciente_encontrado = paciente
            break

    if paciente_encontrado is None:
        print("No se encontro el paciente.")
        return

    sintomas = input("Sintomas del paciente: ").strip()
    diagnostico = input("Diagnostico: ").strip()

    print("\n===== PRESCRIPCION =====")

    medicamento = input("Medicamento: ").strip()
    cantidad = input("Cantidad: ").strip()
    dosis_diaria = input("Dosis diaria: ").strip()
    duracion = input("Duracion en dias: ").strip()

    if not all([sintomas, diagnostico, medicamento, cantidad, dosis_diaria, duracion]):
        print("Todos los campos son obligatorios.")
        return

    consulta = {
        "fecha": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "paciente_identificacion": paciente_encontrado["identificacion"],
        "paciente_nombre": paciente_encontrado["nombres"] + " " + paciente_encontrado["apellidos"],
        "medico_identificacion": medico["identificacion"],
        "medico_nombre": medico["nombres"] + " " + medico["apellidos"],
        "sintomas": sintomas,
        "diagnostico": diagnostico,
        "prescripcion": {
            "medicamento": medicamento,
            "cantidad": cantidad,
            "dosis_diaria": dosis_diaria,
            "duracion_dias": duracion
        }
    }

    datos["consultas"].append(consulta)

    guardar_datos(ruta_datos, datos)

    print("\nDiagnostico registrado correctamente.")

def reporte_carga_medicos(ruta_usuarios, ruta_diagnosticos, ruta_reporte):
    ruta_usuarios = os.path.join ("datos", "datos.json")
    ruta_diagnosticos = os.path.join("datos", "datos.json")
    ruta_reporte = os.path.join("datos", "reporte_carga_medicos.json")


try:
     with open ("ruta_usuarios", "r")

# El programa utiliza un diccionario para mantener un registro detallado
# de los pacientes, incluyendo su información personal y clínica.

def registrar_paciente(nombre: str, edad: int, diagnostico: str, estado_salud: bool) -> dict:
    """
    Registra la información de un paciente en el hospital.
    Parámetros:
        nombre (str): El nombre del paciente.
        edad (int): La edad del paciente.
        diagnostico (str): El diagnóstico médico del paciente.
        estado_salud (bool): Estado de salud del paciente (True si está estable).
    Retorna:
        dict: Un diccionario con los datos del paciente.
    """
    paciente = {
        "nombre": nombre,
        "edad": edad,
        "diagnostico": diagnostico,
        "estado_salud": estado_salud
    }
    return paciente

# Solicitar los datos del paciente
nombre_paciente = input("Introduce el nombre del paciente: ")
edad_paciente = int(input("Introduce la edad del paciente: "))
diagnostico_paciente = input("Introduce el diagnóstico del paciente: ")
estado_salud_paciente = input("¿Está estable de salud? (sí/no): ").strip().lower() == "sí"

# Registrar el paciente
paciente = registrar_paciente(nombre_paciente, edad_paciente, diagnostico_paciente, estado_salud_paciente)

# Mostrar la información del paciente
print(f"\nInformación del Paciente:")
print(f"Nombre: {paciente['nombre']}")
print(f"Edad: {paciente['edad']}")
print(f"Diagnóstico: {paciente['diagnostico']}")
print(f"Estado de salud: {'Estable' if paciente['estado_salud'] else 'Inestable'}")
# ==========================================
# Trabajo Práctico - Equipo de Agentes IA
# Sistema de Gestión de Turnos Médicos
# ==========================================


class AgenteAnalista:
    def trabajar(self):
        print("\n[Analista] Analizando requerimientos...")
        requisitos = [
            "Registro de pacientes",
            "Inicio de sesión",
            "Reserva de turnos",
            "Cancelación de turnos",
            "Historial médico"
        ]

        print("[Analista] Requisitos definidos.")
        return requisitos


class AgenteBackend:
    def trabajar(self, requisitos):
        print("\n[Backend] Desarrollando lógica del sistema...")

        funciones = [
            "API de pacientes",
            "API de médicos",
            "Control de disponibilidad",
            "Autenticación",
            "Gestión de turnos"
        ]

        print("[Backend] Desarrollo completado.")
        return funciones


class AgenteFrontend:
    def trabajar(self):
        print("\n[Frontend] Diseñando interfaces...")

        pantallas = [
            "Pantalla de Login",
            "Registro de Usuarios",
            "Agenda Médica",
            "Reserva de Turnos",
            "Perfil del Paciente"
        ]

        print("[Frontend] Interfaces terminadas.")
        return pantallas


class AgenteBaseDatos:
    def trabajar(self):
        print("\n[Base de Datos] Diseñando estructura...")

        tablas = [
            "Pacientes",
            "Medicos",
            "Turnos",
            "Especialidades",
            "Usuarios"
        ]

        print("[Base de Datos] Modelo generado.")
        return tablas


class AgenteQA:
    def trabajar(self):
        print("\n[QA] Ejecutando pruebas...")

        pruebas = [
            "Prueba de Login",
            "Reserva de Turno",
            "Cancelación",
            "Seguridad",
            "Tiempo de Respuesta"
        ]

        print("[QA] Todas las pruebas aprobadas.")
        return pruebas


class Orquestador:

    def __init__(self):
        self.analista = AgenteAnalista()
        self.backend = AgenteBackend()
        self.frontend = AgenteFrontend()
        self.bd = AgenteBaseDatos()
        self.qa = AgenteQA()

    def ejecutar_proyecto(self):

        print("=" * 50)
        print("INICIO DEL PROYECTO")
        print("=" * 50)

        requisitos = self.analista.trabajar()

        backend = self.backend.trabajar(requisitos)

        frontend = self.frontend.trabajar()

        base_datos = self.bd.trabajar()

        pruebas = self.qa.trabajar()

        print("\n" + "=" * 50)
        print("RESUMEN DEL PROYECTO")
        print("=" * 50)

        print("\nRequisitos:")
        for r in requisitos:
            print("-", r)

        print("\nBackend:")
        for b in backend:
            print("-", b)

        print("\nFrontend:")
        for f in frontend:
            print("-", f)

        print("\nBase de Datos:")
        for t in base_datos:
            print("-", t)

        print("\nPruebas QA:")
        for p in pruebas:
            print("-", p)

        print("\nProyecto finalizado correctamente.")


# Programa principal
if __name__ == "__main__":
    sistema = Orquestador()
    sistema.ejecutar_proyecto()
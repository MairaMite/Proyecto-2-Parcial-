#Integrantes del proyecto grupo 3 [Tigua holguin Nicole Andrea, Veteri Roca Helen Adriana, Mite Reyes Maira Alejandra ]
from src.dominio.espacio import Espacio


class Auditorio(Espacio):
    def __init__(self, id_espacio=None, nombre=None, capacidad=None, horario_disponible=None):
        super().__init__(id_espacio, nombre, capacidad, horario_disponible, "Auditorio")

    def validar_disponibilidad(self):
        # Implementación específica para Auditorio
        # Ejemplo: un auditorio podría requerir reserva por día completo o para eventos específicos.
        if "24/7" in self.horario_disponible:
            return True
        return False

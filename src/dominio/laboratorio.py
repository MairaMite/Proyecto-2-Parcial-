#Integrantes del proyecto grupo 3 [Tigua holguin Nicole Andrea, Veteri Roca Helen Adriana, Mite Reyes Maira Alejandra ]
from src.dominio.espacio import Espacio

class Laboratorio(Espacio):
    def __init__(self, id_espacio=None, nombre=None, capacidad=None, horario_disponible=None):
        super().__init__(id_espacio, nombre, capacidad, horario_disponible, "Laboratorio")

    def validar_disponibilidad(self):
        # Implementación específica para Laboratorio
        # Ejemplo: un laboratorio podría tener horarios específicos o requerir reserva previa.
        if "08:00 - 17:00" in self.horario_disponible:
            return True
        return False
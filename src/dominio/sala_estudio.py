#Integrantes del proyecto grupo 3 [Tigua holguin Nicole Andrea, Veteri Roca Helen Adriana, Mite Reyes Maira Alejandra ]
from src.dominio.espacio import Espacio


class SalaEstudio(Espacio):
    def __init__(self, id_espacio=None, nombre=None, capacidad=None, horario_disponible=None):
        super().__init__(id_espacio, nombre, capacidad, horario_disponible, "Sala de Estudio")

    def validar_disponibilidad(self):
        # Implementación específica para Sala de Estudio
        # Ejemplo: una sala de estudio podría estar disponible si tiene capacidad > 0.
        return self.capacidad > 0

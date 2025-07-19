#Integrantes del proyecto grupo 3 [Tigua holguin Nicole Andrea, Veteri Roca Helen Adriana, Mite Reyes Maira Alejandra ]
class Espacio:
    def __init__(self, id_espacio=None, nombre=None, capacidad=None, horario_disponible=None, tipo=None):
        self._id_espacio = id_espacio
        self._nombre = nombre
        self._capacidad = capacidad
        self._horario_disponible = horario_disponible
        self._tipo = tipo # El tipo se almacena aquí, ya que hay una sola tabla

    @property
    def id_espacio(self):
        return self._id_espacio

    @id_espacio.setter
    def id_espacio(self, id_espacio):
        self._id_espacio = id_espacio

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def capacidad(self):
        return self._capacidad

    @capacidad.setter
    def capacidad(self, capacidad):
        self._capacidad = capacidad

    @property
    def horario_disponible(self):
        return self._horario_disponible

    @horario_disponible.setter
    def horario_disponible(self, horario_disponible):
        self._horario_disponible = horario_disponible

    @property
    def tipo(self):
        return self._tipo

    @tipo.setter
    def tipo(self, tipo):
        self._tipo = tipo

    def validar_disponibilidad(self):
        """
        Método polimórfico para validar la disponibilidad del espacio.
        Debe ser implementado por las subclases.
        """
        raise NotImplementedError("Este método debe ser implementado por las subclases.")

    def __str__(self):
        return f"ID: {self._id_espacio}, Nombre: {self._nombre}, Capacidad: {self._capacidad}, Horario: {self._horario_disponible}, Tipo: {self._tipo}"
#Integrantes del proyecto grupo 3 [Tigua holguin Nicole Andrea, Veteri Roca Helen Adriana, Mite Reyes Maira Alejandra ]
from src.datos.conexion import Conexion
from src.dominio.auditorio import Auditorio
from src.dominio.espacio import Espacio
from src.dominio.laboratorio import Laboratorio
from src.dominio.sala_estudio import SalaEstudio


class EspacioDAO:
    _SELECCIONAR = 'SELECT id, nombre, capacidad, horario_disponible, tipo FROM Espacio ORDER BY nombre'
    _INSERTAR = 'INSERT INTO Espacio(nombre, capacidad, horario_disponible, tipo) VALUES(?, ?, ?, ?)'
    _ACTUALIZAR = 'UPDATE Espacio SET nombre=?, capacidad=?, horario_disponible=?, tipo=? WHERE id=?'
    _ELIMINAR = 'DELETE FROM Espacio WHERE id=?'
    _BUSCAR_POR_NOMBRE = 'SELECT id, nombre, capacidad, horario_disponible, tipo FROM Espacio WHERE nombre LIKE ? ORDER BY nombre'
    _BUSCAR_POR_ID = 'SELECT id, nombre, capacidad, horario_disponible, tipo FROM Espacio WHERE id = ?'


    @classmethod
    def _crear_espacio_desde_fila(cls, fila):
        id_espacio, nombre, capacidad, horario_disponible, tipo = fila
        if tipo == "Laboratorio":
            return Laboratorio(id_espacio, nombre, capacidad, horario_disponible)
        elif tipo == "Sala de Estudio":
            return SalaEstudio(id_espacio, nombre, capacidad, horario_disponible)
        elif tipo == "Auditorio":
            return Auditorio(id_espacio, nombre, capacidad, horario_disponible)
        else:
            # Caso genérico o si el tipo no coincide con una subclase específica
            return Espacio(id_espacio, nombre, capacidad, horario_disponible, tipo)

    @classmethod
    def seleccionar(cls):
        with Conexion.obtenerCursor() as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            espacios = []
            for registro in registros:
                espacios.append(cls._crear_espacio_desde_fila(registro))
            return espacios

    @classmethod
    def insertar(cls, espacio):
        with Conexion.obtenerConexion() as conexion:
            with conexion.cursor() as cursor:
                valores = (espacio.nombre, espacio.capacidad, espacio.horario_disponible, espacio.tipo)
                cursor.execute(cls._INSERTAR, valores)
                conexion.commit() # Confirmar la transacción
                print(f"Espacio insertado: {espacio.nombre}")
                return cursor.rowcount # Retorna el número de filas afectadas

    @classmethod
    def actualizar(cls, espacio):
        with Conexion.obtenerConexion() as conexion:
            with conexion.cursor() as cursor:
                valores = (espacio.nombre, espacio.capacidad, espacio.horario_disponible, espacio.tipo, espacio.id_espacio)
                cursor.execute(cls._ACTUALIZAR, valores)
                conexion.commit() # Confirmar la transacción
                print(f"Espacio actualizado: {espacio.nombre}")
                return cursor.rowcount

    @classmethod
    def eliminar(cls, id_espacio):
        with Conexion.obtenerConexion() as conexion:
            with conexion.cursor() as cursor:
                cursor.execute(cls._ELIMINAR, (id_espacio,))
                conexion.commit() # Confirmar la transacción
                print(f"Espacio eliminado con ID: {id_espacio}")
                return cursor.rowcount

    @classmethod
    def buscar_por_nombre(cls, nombre):
        with Conexion.obtenerCursor() as cursor:
            cursor.execute(cls._BUSCAR_POR_NOMBRE, (f'%{nombre}%',))
            registros = cursor.fetchall()
            espacios = []
            for registro in registros:
                espacios.append(cls._crear_espacio_desde_fila(registro))
            return espacios

    @classmethod
    def buscar_por_id(cls, id_espacio):
        with Conexion.obtenerCursor() as cursor:
            cursor.execute(cls._BUSCAR_POR_ID, (id_espacio,))
            registro = cursor.fetchone()
            if registro:
                return cls._crear_espacio_desde_fila(registro)
            return None

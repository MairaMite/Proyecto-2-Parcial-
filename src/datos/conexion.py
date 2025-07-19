#Integrantes del proyecto grupo 3 [Tigua holguin Nicole Andrea, Veteri Roca Helen Adriana, Mite Reyes Maira Alejandra ]
import pyodbc as bd
import sys
# import logging as log # Descomentar si quieres usar logging

class Conexion:
    """
    Clase que permite abrir conexion a la BBDD y abrir cursor.
    """
    # CORRECCIÓN CLAVE AQUÍ: Usamos el nombre del PC y la instancia de SQL Server
    _SERVIDOR = 'ASISTENTE3-PC\\MEROSQLSERVER'
    _BBDD = 'PlataformaReservas' # Nombre de la base de datos, según el proyecto
    _USUARIO = 'Maira' # Usuario de la base de datos, según lo acordado
    _PASSWORD = '123456789' # Contraseña del usuario, según lo acordado
    _conexion = None
    _cursor = None

    @classmethod
    def obtenerConexion(cls):
        """
        Obtiene la conexion a la BBDD con los parametros de conexion pasados como constantes
        """
        if cls._conexion is None:
            try:
                # Asegúrate de que el DRIVER coincida con la versión exacta instalada en tu sistema.
                # Tu archivo 'conexion (1).py' [cite: 2] usa 'ODBC Driver 18 for SQL Server'.
                # Si tienes el 17, cámbialo a 'ODBC Driver 17 for SQL Server'.
                cls._conexion = bd.connect('DRIVER={ODBC Driver 18 for SQL Server};SERVER=' +
                                           cls._SERVIDOR + ';DATABASE=' + cls._BBDD + ';UID=' + cls._USUARIO + ';PWD=' + cls._PASSWORD
                                           + ';TrustServerCertificate=yes')
                print(f'Conexión exitosa: {cls._conexion}')
                return cls._conexion
            except Exception as e:
                print(f'Ocurrió una excepción al obtener la conexión: {e}')
                sys.exit()
        else:
            return cls._conexion

    @classmethod
    def obtenerCursor(cls):
        """
        Obtiene el cursor para ejecutar consultas SQL
        """
        if cls._cursor is None:
            try:
                cls._cursor = cls.obtenerConexion().cursor()
                print(f'Se abrió correctamente el cursor: {cls._cursor}')
                return cls._cursor
            except Exception as e:
                print(f'Ocurrió una excepción al obtener el cursor: {e}')
                sys.exit()
        else:
            return cls._cursor

# Ejemplo de uso y prueba de conexión
if __name__ == '__main__':
    print("Probando conexión a la base de datos...")
    conn = None
    cursor = None
    try:
        conn = Conexion.obtenerConexion()
        cursor = Conexion.obtenerCursor()
        if conn and cursor:
            print("Conexión y cursor obtenidos exitosamente.")
            # Opcional: Ejecutar una consulta simple para verificar
            # cursor.execute("SELECT GETDATE();")
            # print(f"Fecha/Hora actual del servidor SQL: {cursor.fetchone()[0]}")
    except Exception as e:
        print(f"Error durante la prueba de conexión: {e}")
    finally:
        if cursor:
            cursor.close()
            print("Cursor cerrado.")

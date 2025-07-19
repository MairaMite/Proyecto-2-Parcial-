### Gestión de Espacios Universitarios
## Integrantes del proyecto grupo 3 [Tigua holguin Nicole Andrea, Veteri Roca Helen Adriana, Mite Reyes Maira Alejandra ]

Este proyecto es un sistema de escritorio para la gestión de espacios dentro de una universidad, permitiendo el registro, consulta, edición y eliminación de diferentes tipos de espacios como Laboratorios, Salas de Estudio y Auditorios. La aplicación está construida con Python y utiliza PySide6 para la interfaz gráfica de usuario (GUI), y se conecta a una base de datos SQL Server para la persistencia de los datos.

## 🗃️ Estructura del Proyecto

El proyecto sigue una arquitectura organizada en capas para separar las responsabilidades:

.
├── src/
│   ├── UI/
│   │   └── vtnPlataforma.py          # Clase generada por Qt Designer para la UI
│   ├── datos/
│   │   ├── conexion.py               # Módulo para la conexión a la base de datos SQL Server
│   │   └── espacioDao.py             # Objeto de Acceso a Datos (DAO) para interactuar con la tabla Espacio
│   ├── dominio/
│   │   ├── espacio.py                # Clase base abstracta para los espacios
│   │   ├── laboratorio.py            # Implementación de la clase Espacio para Laboratorios
│   │   ├── sala_estudio.py           # Implementación de la clase Espacio para Salas de Estudio
│   │   └── auditorio.py              # Implementación de la clase Espacio para Auditorios
│   └── servicio/
│       └── espacio_servicio.py       # Lógica de negocio y manejo de la UI (hereda de QMainWindow)
├── main.py                           # Punto de entrada de la aplicación
├── PlataformaReservas.sql            # Script SQL para la creación de la base de datos y tabla
└── README.md                         # Archivo de documentación del proyecto

## Imagen de la interfaz
<img width="783" height="620" alt="image" src="https://github.com/user-attachments/assets/7e6f1674-ce70-41df-9c66-5c4503154e7d" />
<img width="779" height="630" alt="image" src="https://github.com/user-attachments/assets/256697f9-73c1-4415-ae64-46fa0fb1ec7a" />

## Sql registro
<img width="1904" height="991" alt="image" src="https://github.com/user-attachments/assets/ec59f1f5-0421-4489-b595-d8b5d7595731" />




##  ⚙️ Requisitos del Sistema

Para ejecutar este proyecto, necesitas lo siguiente:

* **Python 3.x**
* **SQL Server**: Una instancia de SQL Server accesible (ej. SQL Server Express, Developer Edition).
* **Controlador ODBC para SQL Server**: Necesario para que Python se conecte a SQL Server. Se recomienda `ODBC Driver 18 for SQL Server` o `ODBC Driver 17 for SQL Server`.

##  📦 Instalación

Sigue estos pasos para configurar y ejecutar el proyecto:

###  1. Clonar el Repositorio

```bash
git clone <url-del-repositorio>
cd <nombre-del-repositorio>
2. Configurar la Base de Datos
Crear la Base de Datos y la Tabla:
Ejecuta el script PlataformaReservas.sql en tu instancia de SQL Server. Este script creará la base de datos PlataformaReservas y la tabla Espacio con los campos necesarios y algunos datos de ejemplo.

SQL

-- Contenido de PlataformaReservas.sql
CREATE DATABASE [PlataformaReservas]
GO

USE [PlataformaReservas]
GO

CREATE TABLE Espacio (
    id INT IDENTITY(1,1) PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL UNIQUE,
    capacidad INT NOT NULL,
    horario_disponible VARCHAR(255),
    tipo VARCHAR(50) NOT NULL CHECK (tipo IN ('Laboratorio', 'Sala de Estudio', 'Auditorio'))
);
GO

INSERT INTO Espacio (nombre, capacidad, horario_disponible, tipo) VALUES
('Laboratorio 101', 30, '08:00 - 18:00', 'Laboratorio'),
('Sala de Estudio A', 15, '09:00 - 20:00', 'Sala de Estudio'),
('Auditorio Principal', 200, '07:00 - 22:00', 'Auditorio');
GO
Configurar Credenciales de Conexión:
Abre src/datos/conexion.py y actualiza las siguientes constantes con los detalles de tu servidor SQL Server:

_SERVIDOR: Nombre de tu servidor SQL Server y la instancia (ej. 'TU_PC\\SQLEXPRESS').

_BBDD: Nombre de la base de datos (ya configurado como 'PlataformaReservas').

_USUARIO: Tu nombre de usuario para la base de datos.

_PASSWORD: Tu contraseña para el usuario de la base de datos.

DRIVER: Asegúrate de que el nombre del controlador ODBC coincida con el que tienes instalado. Por ejemplo, ODBC Driver 18 for SQL Server.




Python

##   src/datos/conexion.py
class Conexion:
    _SERVIDOR = 'ASISTENTE3-PC\\MEROSQLSERVER' # ¡ACTUALIZA ESTO!
    _BBDD = 'PlataformaReservas'
    _USUARIO = 'Maira' # ¡ACTUALIZA ESTO!
    _PASSWORD = '123456789' # ¡ACTUALIZA ESTO!
    # ...
    _conexion = bd.connect('DRIVER={ODBC Driver 18 for SQL Server};SERVER=' + # Verifica el DRIVER
                           cls._SERVIDOR + ';DATABASE=' + cls._BBDD + ';UID=' + cls._USUARIO + ';PWD=' + cls._PASSWORD
                           + ';TrustServerCertificate=yes')
##  3. Crear un Entorno Virtual (Recomendado)
Bash

python -m venv venv
#  En Windows
.\venv\Scripts\activate
#  En macOS/Linux
source venv/bin/activate
##  4. Instalar Dependencias
Bash

pip install PySide6 pyodbc
## ▶️ Ejecución de la Aplicación
Una vez configurado, puedes iniciar la aplicación ejecutando el archivo main.py:

Bash

python main.py
Esto abrirá la ventana principal de la aplicación de Gestión de Espacios Universitarios.

## 🚀 Funcionalidades
El sistema permite realizar las siguientes operaciones sobre los espacios universitarios:

Registro de Espacios: Crea nuevos registros de Laboratorios, Salas de Estudio y Auditorios, especificando su nombre, capacidad, horario disponible y tipo.

Edición de Espacios: Modifica los detalles de un espacio existente seleccionándolo de la tabla.

Eliminación de Espacios: Elimina un espacio seleccionado de la base de datos.

Consulta de Espacios: Visualiza todos los espacios registrados en una tabla.

Búsqueda de Espacios: Filtra los espacios por nombre para encontrar rápidamente un registro específico.

Validación de Datos: Incluye validaciones para asegurar la integridad de los datos ingresados (ej. nombre obligatorio, capacidad mínima, formato de horario).

Manejo de Mensajes: Muestra mensajes informativos, de advertencia o de error al usuario.



## Validaciones Específicas:
Nombre: Obligatorio y con un mínimo de 3 caracteres. No permite nombres duplicados.

Capacidad: Debe ser un número entero mayor o igual a 50.

Horario Disponible: Formato HH:MM - HH:MM (ej. 08:00 - 17:00).

Tipo de Espacio: Debe ser uno de los predefinidos (Laboratorio, Sala de Estudio, Auditorio).




##  Polimorfismo en validar_disponibilidad:
Cada tipo de espacio (Laboratorio, Sala de Estudio, Auditorio) tiene su propia implementación del método validar_disponibilidad, demostrando el polimorfismo. Sin embargo, en esta versión de la aplicación, este método no se utiliza directamente en la lógica de la UI para controlar la disponibilidad, sino que es un ejemplo de cómo cada subclase puede tener un comportamiento específico.

Laboratorio.validar_disponibilidad(): Retorna True si el horario incluye "08:00 - 17:00".

SalaEstudio.validar_disponibilidad(): Retorna True si la capacidad es mayor que 0.

Auditorio.validar_disponibilidad(): Retorna True si el horario incluye "24/7".

## 🛠️ Tecnologías Utilizadas
Python: Lenguaje de programación principal.

PySide6: Framework para el desarrollo de interfaces gráficas de usuario (GUI).

pyodbc: Módulo Python para conectar a bases de datos ODBC (SQL Server).

SQL Server: Sistema de gestión de bases de datos relacionales.

#Integrantes del proyecto grupo 3 [Tigua holguin Nicole Andrea, Veteri Roca Helen Adriana, Mite Reyes Maira Alejandra ]
import sys
import os
from PySide6.QtWidgets import QApplication

# Asegúrate de que el directorio raíz del proyecto esté en sys.path para imports absolutos
project_root = os.path.dirname(os.path.abspath(__file__))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

# Importa la clase de la ventana principal que ahora incluye la lógica del servicio
from src.servicio.espacio_servicio import EspacioServicio

if __name__ == "__main__":
    # Esta sección es la única encargada de la ejecución de la aplicación.
    # No contiene lógica de negocio ni validaciones.
    app = QApplication(sys.argv)
    vtn_plataforma = EspacioServicio() # Se instancia la CLASE DE VENTANA (EspacioServicio)
    vtn_plataforma.show()
    sys.exit(app.exec())
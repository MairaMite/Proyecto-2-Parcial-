#Integrantes del proyecto grupo 3 [Tigua holguin Nicole Andrea, Veteri Roca Helen Adriana, Mite Reyes Maira Alejandra ]
import re
from PySide6.QtWidgets import QMainWindow, QMessageBox, QTableView, QHeaderView, QAbstractItemView
from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtCore import Qt

# Importa la clase de UI generada por Qt Designer
from src.UI.vtnPlataforma import Ui_vtnPlataforma
from src.datos.espacioDao import EspacioDAO
from src.dominio.auditorio import Auditorio
from src.dominio.espacio import Espacio
from src.dominio.laboratorio import Laboratorio
from src.dominio.sala_estudio import SalaEstudio



class EspacioServicio(QMainWindow):  # Hereda solo de QMainWindow
    """
    Clase de la ventana principal de la aplicación.
    Maneja la interacción con el usuario y contiene la lógica de negocio y validaciones.
    Utiliza composición para la interfaz de usuario (Ui_vtnPlataforma).
    """

    def __init__(self):
        super().__init__()  # Llama al constructor de QMainWindow
        self.ui = Ui_vtnPlataforma()  # Crea una instancia de la clase de UI generada
        self.ui.setupUi(self)  # Inicializa la interfaz de usuario en la instancia 'self.ui'

        # Configurar el modelo para QTableView
        self.model = QStandardItemModel(0, 5)  # 0 filas iniciales, 5 columnas
        self.ui.table_espacios.setModel(self.model)  # Acceso a través de self.ui
        self.model.setHorizontalHeaderLabels([
            "ID", "Nombre", "Capacidad", "Horario", "Tipo"
        ])
        self.ui.table_espacios.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents)
        self.ui.table_espacios.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)
        self.ui.table_espacios.horizontalHeader().setSectionResizeMode(2, QHeaderView.ResizeToContents)
        self.ui.table_espacios.horizontalHeader().setSectionResizeMode(3, QHeaderView.Stretch)
        self.ui.table_espacios.horizontalHeader().setSectionResizeMode(4, QHeaderView.ResizeToContents)
        self.ui.table_espacios.setSelectionBehavior(QAbstractItemView.SelectRows)

        # Conectar señales/slots (acceso a los elementos de la UI a través de self.ui)
        self.ui.btn_guardar.clicked.connect(self.guardar_espacio)
        self.ui.btn_limpiar.clicked.connect(self.limpiar_campos)
        self.ui.btn_cancelar.clicked.connect(self.cancelar_edicion)
        self.ui.btn_buscar.clicked.connect(self.buscar_espacios)
        self.ui.btn_editar.clicked.connect(self.cargar_espacio_seleccionado_para_edicion)
        self.ui.btn_eliminar.clicked.connect(self.eliminar_espacio_seleccionado)
        self.ui.cmb_tipo.currentIndexChanged.connect(self._actualizar_campos_especificos_ui)

        # Deshabilitar el campo ID inicialmente (es auto-generado por la BD)
        self.ui.txt_id.setEnabled(False)  # Acceso a través de self.ui
        self.ui.txt_id.setReadOnly(True)  # Acceso a través de self.ui

        # Cargar todos los espacios desde la base de datos al inicio
        self.cargar_todos_espacios()

        # Ocultar campos específicos (siguen sin existir en la UI)
        self._actualizar_campos_especificos_ui()

    def mostrar_mensaje(self, titulo, mensaje, tipo="information"):
        """
        Muestra un cuadro de mensaje al usuario.
        """
        msg_box = QMessageBox(self)
        msg_box.setWindowTitle(titulo)
        msg_box.setText(mensaje)
        if tipo == "information":
            msg_box.setIcon(QMessageBox.Information)
        elif tipo == "warning":
            msg_box.setIcon(QMessageBox.Warning)
        elif tipo == "error":
            msg_box.setIcon(QMessageBox.Critical)
        msg_box.exec()

    def _actualizar_campos_especificos_ui(self):
        """
        Esta función es un placeholder. En esta versión con una sola tabla,
        no hay campos específicos de subclase en la UI para ocultar/mostrar.
        """
        pass

    def limpiar_campos(self):
        """
        Limpia todos los campos del formulario de registro/edición.
        """
        self.ui.txt_id.clear()  # Acceso a través de self.ui
        self.ui.txt_nombre.clear()  # Acceso a través de self.ui
        self.ui.spin_capacidad.setValue(1)  # Acceso a través de self.ui
        self.ui.txt_horario.clear()  # Acceso a través de self.ui
        self.ui.cmb_tipo.setCurrentIndex(0)  # Acceso a través de self.ui
        self.ui.btn_guardar.setText("Guardar")  # Acceso a través de self.ui
        # _actualizar_campos_especificos_ui() es pasiva ahora

    def cancelar_edicion(self):
        """
        Cancela la edición y limpia los campos, volviendo a la pestaña de consulta.
        """
        self.limpiar_campos()
        self.ui.tabWidget.setCurrentIndex(1)  # Acceso a través de self.ui

    def cargar_todos_espacios(self):
        """
        Carga todos los espacios desde la base de datos y los muestra en la tabla de la UI.
        """
        self.model.setRowCount(0)  # Limpiar tabla existente
        try:
            espacios_db = EspacioDAO.seleccionar()
            if not espacios_db:
                self.mostrar_mensaje("Información",
                                     "No se encontraron espacios en la base de datos. Agregue nuevos registros.",
                                     "information")
            self.cargar_tabla_ui(espacios_db)  # Carga la tabla con los datos de la DB
        except Exception as e:
            self.mostrar_mensaje("Error de Conexión/Carga",
                                 f"Ocurrió un error al cargar los espacios de la base de datos. Detalles: {e}",
                                 "error")

    def cargar_tabla_ui(self, espacios_a_mostrar=None):
        """
        Popula la QTableView con la lista de espacios proporcionada.
        """
        self.model.setRowCount(0)  # Limpiar tabla existente
        if espacios_a_mostrar is None:
            espacios_a_mostrar = []  # Si no se pasa nada, muestra vacío

        for espacio in espacios_a_mostrar:
            row_position = self.model.rowCount()
            self.model.insertRow(row_position)
            self.model.setItem(row_position, 0, QStandardItem(str(espacio.id_espacio)))  # Acceso a .id_espacio
            self.model.setItem(row_position, 1, QStandardItem(espacio.nombre))
            self.model.setItem(row_position, 2, QStandardItem(str(espacio.capacidad)))
            self.model.setItem(row_position, 3, QStandardItem(espacio.horario_disponible))
            self.model.setItem(row_position, 4, QStandardItem(espacio.tipo))  # Acceso a .tipo

    def guardar_espacio(self):
        """
        Maneja el guardado (creación o actualización) de un espacio.
        Realiza validaciones y llama al DAO.
        """
        id_espacio_str = self.ui.txt_id.text()  # Acceso a través de self.ui
        id_espacio = int(id_espacio_str) if id_espacio_str else None
        nombre = self.ui.txt_nombre.text()  # Acceso a través de self.ui
        capacidad = self.ui.spin_capacidad.value()  # Acceso a través de self.ui
        horario = self.ui.txt_horario.text()  # Acceso a través de self.ui
        tipo_espacio = self.ui.cmb_tipo.currentText()  # Acceso a través de self.ui

        # --- Validaciones ---
        valido, mensaje = self._validar_nombre(nombre)
        if not valido:
            self.mostrar_mensaje("Error de Validación", mensaje, "warning")
            return
        valido, mensaje = self._validar_capacidad(capacidad)
        if not valido:
            self.mostrar_mensaje("Error de Validación", mensaje, "warning")
            return
        valido, mensaje = self._validar_horario(horario)
        if not valido:
            self.mostrar_mensaje("Error de Validación", mensaje, "warning")
            return
        valido, mensaje = self._validar_tipo(tipo_espacio)
        if not valido:
            self.mostrar_mensaje("Error de Validación", mensaje, "warning")
            return

        # Control de duplicados por nombre
        existing_spaces = EspacioDAO.buscar_por_nombre(nombre)
        for esp in existing_spaces:
            if esp.nombre.lower() == nombre.lower() and esp.id_espacio != id_espacio:
                self.mostrar_mensaje("Error de Validación", "Ya existe un espacio con ese nombre.", "warning")
                return

        # Crear el objeto espacio de dominio
        espacio_obj = None
        if tipo_espacio == "Laboratorio":
            espacio_obj = Laboratorio(id_espacio, nombre, capacidad, horario)
        elif tipo_espacio == "Sala de Estudio":
            espacio_obj = SalaEstudio(id_espacio, nombre, capacidad, horario)
        elif tipo_espacio == "Auditorio":
            espacio_obj = Auditorio(id_espacio, nombre, capacidad, horario)
        else:
            espacio_obj = Espacio(id_espacio, nombre, capacidad, horario, tipo_espacio)

        # --- Lógica de guardado en la base de datos ---
        db_success = False
        try:
            if id_espacio:  # Edición
                db_success = EspacioDAO.actualizar(espacio_obj)
            else:  # Nuevo registro
                db_success = EspacioDAO.insertar(espacio_obj)

            if db_success > 0:  # Asumiendo que DAO.insertar/actualizar retorna el número de filas afectadas
                self.mostrar_mensaje("Éxito", "Operación realizada exitosamente en la base de datos.", "information")
            else:
                self.mostrar_mensaje("Error", "No se pudo realizar la operación en la base de datos.", "error")
        except Exception as e:
            self.mostrar_mensaje("Error de Base de Datos",
                                 f"Ocurrió un error al interactuar con la base de datos: {e}",
                                 "error")
            print(f"Error en guardar_espacio: {e}")  # Para depuración en consola

        self.limpiar_campos()
        self.cargar_todos_espacios()  # Recarga la tabla desde la DB
        self.ui.tabWidget.setCurrentIndex(1)  # Acceso a través de self.ui

    def _validar_nombre(self, nombre):
        if not nombre or not nombre.strip():
            return False, "El nombre del espacio es obligatorio."
        if len(nombre) < 3:
            return False, "El nombre debe tener al menos 3 caracteres."
        return True, ""

    def _validar_capacidad(self, capacidad):
        # CORRECCIÓN: La capacidad debe ser un número entero y al menos 50.
        if not isinstance(capacidad, int) or capacidad < 50:
            return False, "La capacidad debe ser un número entero y al menos 50."
        return True, ""

    def _validar_horario(self, horario):
        if not horario or not horario.strip():
            return False, "El horario disponible es obligatorio."
        if not re.fullmatch(r'\d{2}:\d{2} - \d{2}:\d{2}', horario):
            return False, "El formato de horario debe ser HH:MM - HH:MM (ej. 08:00 - 17:00)."
        return True, ""

    def _validar_tipo(self, tipo):
        if tipo not in ["Laboratorio", "Sala de Estudio", "Auditorio"]:
            return False, "Tipo de espacio inválido."
        return True, ""

    def buscar_espacios(self):
        """
        Realiza una búsqueda de espacios por nombre en la base de datos y actualiza la tabla.
        """
        nombre_busqueda = self.ui.txt_buscar.text().strip()  # Acceso a través de self.ui
        if not nombre_busqueda:
            self.cargar_todos_espacios()  # Si no hay búsqueda, muestra todo lo de la DB
            return

        try:
            espacios_filtrados = EspacioDAO.buscar_por_nombre(nombre_busqueda)
            if not espacios_filtrados:
                self.mostrar_mensaje("Búsqueda",
                                     f"No se encontraron espacios con el nombre '{nombre_busqueda}' en la base de datos.",
                                     "information")
            self.cargar_tabla_ui(espacios_filtrados)  # Muestra solo los filtrados
        except Exception as e:
            self.mostrar_mensaje("Error de Búsqueda",
                                 f"Ocurrió un error al buscar en la base de datos: {e}",
                                 "error")
            print(f"Error en buscar_espacios: {e}")  # Para depuración

    def cargar_espacio_seleccionado_para_edicion(self):
        """
        Carga los datos del espacio seleccionado en el formulario para su edición.
        """
        selected_rows = self.ui.table_espacios.selectionModel().selectedRows()  # Acceso a través de self.ui
        if not selected_rows:
            self.mostrar_mensaje("Error de Selección", "Seleccione un espacio de la tabla para editar.", "warning")
            return

        row = selected_rows[0].row()
        id_espacio_str = self.model.item(row, 0).text()  # Obtener ID del modelo

        try:
            espacio_a_editar = EspacioDAO.buscar_por_id(int(id_espacio_str))
            if espacio_a_editar:
                self.ui.txt_id.setText(str(espacio_a_editar.id_espacio))  # Acceso a través de self.ui
                self.ui.txt_nombre.setText(espacio_a_editar.nombre)  # Acceso a través de self.ui
                self.ui.spin_capacidad.setValue(espacio_a_editar.capacidad)  # Acceso a través de self.ui
                self.ui.txt_horario.setText(espacio_a_editar.horario_disponible)  # Acceso a través de self.ui

                tipo = espacio_a_editar.tipo  # Obtener el tipo directamente del objeto
                index = self.ui.cmb_tipo.findText(tipo)  # Acceso a través de self.ui
                if index >= 0:
                    self.ui.cmb_tipo.setCurrentIndex(index)  # Acceso a través de self.ui

                self.ui.btn_guardar.setText("Actualizar")  # Acceso a través de self.ui
                self.ui.tabWidget.setCurrentIndex(
                    0)  # Acceso a través de self.ui # Cambia a la pestaña de registro/edición
            else:
                self.mostrar_mensaje("Error",
                                     "No se pudo cargar los detalles del espacio para edición desde la base de datos.",
                                     "error")
        except Exception as e:
            self.mostrar_mensaje("Error de Carga para Edición",
                                 f"Ocurrió un error al cargar el espacio para edición: {e}",
                                 "error")
            print(f"Error en cargar_espacio_seleccionado_para_edicion: {e}")  # Para depuración

    def eliminar_espacio_seleccionado(self):
        """
        Elimina el espacio seleccionado de la base de datos previa confirmación.
        """
        selected_rows = self.ui.table_espacios.selectionModel().selectedRows()  # Acceso a través de self.ui
        if not selected_rows:
            self.mostrar_mensaje("Error de Selección", "Seleccione un espacio de la tabla para eliminar.", "warning")
            return

        row = selected_rows[0].row()
        id_espacio_str = self.model.item(row, 0).text()  # Obtener ID del modelo
        nombre_espacio = self.model.item(row, 1).text()  # Obtener nombre del modelo

        reply = QMessageBox.question(self, 'Confirmar Eliminación',
                                     f"¿Está seguro de que desea eliminar el espacio '{nombre_espacio}' (ID: {id_espacio_str})?",
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            try:
                db_success = EspacioDAO.eliminar(int(id_espacio_str))
                if db_success > 0:
                    self.mostrar_mensaje("Éxito", "Espacio eliminado exitosamente de la base de datos.", "information")
                    self.cargar_todos_espacios()  # Recargar la tabla desde la DB
                else:
                    self.mostrar_mensaje("Error", "No se pudo eliminar el espacio de la base de datos.", "error")
            except Exception as e:
                self.mostrar_mensaje("Error de Eliminación",
                                     f"Ocurrió un error al intentar eliminar el espacio: {e}",
                                     "error")
                print(f"Error en eliminar_espacio_seleccionado: {e}")  # Para depuración

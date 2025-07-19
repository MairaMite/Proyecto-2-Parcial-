# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'vtnPlataforma.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFormLayout, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QSpinBox,
    QStatusBar, QTabWidget, QTableView, QVBoxLayout,
    QWidget)

class Ui_vtnPlataforma(object):
    def setupUi(self, vtnPlataforma):
        if not vtnPlataforma.objectName():
            vtnPlataforma.setObjectName(u"vtnPlataforma")
        vtnPlataforma.resize(800, 600)
        self.centralwidget = QWidget(vtnPlataforma)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab_registro_edicion = QWidget()
        self.tab_registro_edicion.setObjectName(u"tab_registro_edicion")
        self.formLayout = QFormLayout(self.tab_registro_edicion)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setHorizontalSpacing(10)
        self.formLayout.setVerticalSpacing(10)
        self.lbl_id = QLabel(self.tab_registro_edicion)
        self.lbl_id.setObjectName(u"lbl_id")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.lbl_id)

        self.txt_id = QLineEdit(self.tab_registro_edicion)
        self.txt_id.setObjectName(u"txt_id")
        self.txt_id.setEnabled(False)
        self.txt_id.setReadOnly(True)

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.txt_id)

        self.lbl_nombre = QLabel(self.tab_registro_edicion)
        self.lbl_nombre.setObjectName(u"lbl_nombre")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.lbl_nombre)

        self.txt_nombre = QLineEdit(self.tab_registro_edicion)
        self.txt_nombre.setObjectName(u"txt_nombre")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.txt_nombre)

        self.lbl_capacidad = QLabel(self.tab_registro_edicion)
        self.lbl_capacidad.setObjectName(u"lbl_capacidad")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.lbl_capacidad)

        self.spin_capacidad = QSpinBox(self.tab_registro_edicion)
        self.spin_capacidad.setObjectName(u"spin_capacidad")
        self.spin_capacidad.setMinimum(1)
        self.spin_capacidad.setMaximum(1000)

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.spin_capacidad)

        self.lbl_horario = QLabel(self.tab_registro_edicion)
        self.lbl_horario.setObjectName(u"lbl_horario")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.lbl_horario)

        self.txt_horario = QLineEdit(self.tab_registro_edicion)
        self.txt_horario.setObjectName(u"txt_horario")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.txt_horario)

        self.lbl_tipo = QLabel(self.tab_registro_edicion)
        self.lbl_tipo.setObjectName(u"lbl_tipo")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.lbl_tipo)

        self.cmb_tipo = QComboBox(self.tab_registro_edicion)
        self.cmb_tipo.addItem("")
        self.cmb_tipo.addItem("")
        self.cmb_tipo.addItem("")
        self.cmb_tipo.setObjectName(u"cmb_tipo")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.cmb_tipo)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btn_guardar = QPushButton(self.tab_registro_edicion)
        self.btn_guardar.setObjectName(u"btn_guardar")

        self.horizontalLayout_2.addWidget(self.btn_guardar)

        self.btn_limpiar = QPushButton(self.tab_registro_edicion)
        self.btn_limpiar.setObjectName(u"btn_limpiar")

        self.horizontalLayout_2.addWidget(self.btn_limpiar)

        self.btn_cancelar = QPushButton(self.tab_registro_edicion)
        self.btn_cancelar.setObjectName(u"btn_cancelar")

        self.horizontalLayout_2.addWidget(self.btn_cancelar)


        self.formLayout.setLayout(5, QFormLayout.ItemRole.FieldRole, self.horizontalLayout_2)

        self.tabWidget.addTab(self.tab_registro_edicion, "")
        self.tab_consulta = QWidget()
        self.tab_consulta.setObjectName(u"tab_consulta")
        self.verticalLayout = QVBoxLayout(self.tab_consulta)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lbl_buscar = QLabel(self.tab_consulta)
        self.lbl_buscar.setObjectName(u"lbl_buscar")

        self.horizontalLayout.addWidget(self.lbl_buscar)

        self.txt_buscar = QLineEdit(self.tab_consulta)
        self.txt_buscar.setObjectName(u"txt_buscar")

        self.horizontalLayout.addWidget(self.txt_buscar)

        self.btn_buscar = QPushButton(self.tab_consulta)
        self.btn_buscar.setObjectName(u"btn_buscar")

        self.horizontalLayout.addWidget(self.btn_buscar)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.table_espacios = QTableView(self.tab_consulta)
        self.table_espacios.setObjectName(u"table_espacios")

        self.verticalLayout.addWidget(self.table_espacios)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.btn_editar = QPushButton(self.tab_consulta)
        self.btn_editar.setObjectName(u"btn_editar")

        self.horizontalLayout_3.addWidget(self.btn_editar)

        self.btn_eliminar = QPushButton(self.tab_consulta)
        self.btn_eliminar.setObjectName(u"btn_eliminar")

        self.horizontalLayout_3.addWidget(self.btn_eliminar)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.tabWidget.addTab(self.tab_consulta, "")

        self.verticalLayout_2.addWidget(self.tabWidget)

        vtnPlataforma.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(vtnPlataforma)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 33))
        vtnPlataforma.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(vtnPlataforma)
        self.statusbar.setObjectName(u"statusbar")
        vtnPlataforma.setStatusBar(self.statusbar)

        self.retranslateUi(vtnPlataforma)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(vtnPlataforma)
    # setupUi

    def retranslateUi(self, vtnPlataforma):
        vtnPlataforma.setWindowTitle(QCoreApplication.translate("vtnPlataforma", u"Gesti\u00f3n de Espacios Universitarios", None))
        self.lbl_id.setText(QCoreApplication.translate("vtnPlataforma", u"ID (Autom\u00e1tico):", None))
        self.lbl_nombre.setText(QCoreApplication.translate("vtnPlataforma", u"Nombre:", None))
        self.txt_nombre.setPlaceholderText(QCoreApplication.translate("vtnPlataforma", u"Nombre del espacio (ej. Laboratorio A)", None))
        self.lbl_capacidad.setText(QCoreApplication.translate("vtnPlataforma", u"Capacidad:", None))
        self.lbl_horario.setText(QCoreApplication.translate("vtnPlataforma", u"Horario Disponible:", None))
        self.txt_horario.setPlaceholderText(QCoreApplication.translate("vtnPlataforma", u"Ej. 08:00 - 17:00", None))
        self.lbl_tipo.setText(QCoreApplication.translate("vtnPlataforma", u"Tipo de Espacio:", None))
        self.cmb_tipo.setItemText(0, QCoreApplication.translate("vtnPlataforma", u"Laboratorio", None))
        self.cmb_tipo.setItemText(1, QCoreApplication.translate("vtnPlataforma", u"Sala de Estudio", None))
        self.cmb_tipo.setItemText(2, QCoreApplication.translate("vtnPlataforma", u"Auditorio", None))

        self.btn_guardar.setText(QCoreApplication.translate("vtnPlataforma", u"Guardar", None))
        self.btn_limpiar.setText(QCoreApplication.translate("vtnPlataforma", u"Limpiar", None))
        self.btn_cancelar.setText(QCoreApplication.translate("vtnPlataforma", u"Cancelar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_registro_edicion), QCoreApplication.translate("vtnPlataforma", u"Registro / Edici\u00f3n", None))
        self.lbl_buscar.setText(QCoreApplication.translate("vtnPlataforma", u"Buscar por Nombre:", None))
        self.txt_buscar.setPlaceholderText(QCoreApplication.translate("vtnPlataforma", u"Ingrese nombre del espacio a buscar", None))
        self.btn_buscar.setText(QCoreApplication.translate("vtnPlataforma", u"Buscar", None))
        self.btn_editar.setText(QCoreApplication.translate("vtnPlataforma", u"Editar Seleccionado", None))
        self.btn_eliminar.setText(QCoreApplication.translate("vtnPlataforma", u"Eliminar Seleccionado", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_consulta), QCoreApplication.translate("vtnPlataforma", u"Consulta", None))
    # retranslateUi


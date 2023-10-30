# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'projeto_barcos2.ui'
##
## Created by: Qt User Interface Compiler version 6.5.3
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QStackedWidget, QTabWidget,
    QTextEdit, QToolBox, QVBoxLayout, QWidget)
import icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QSize(800, 600))
        MainWindow.setStyleSheet(u"background-color: rgb(0, 0,0);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"*{\n"
"border:None;\n"
"}\n"
"QLabel{\n"
"color:rgb(255,255,255);\n"
"}")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 9)
        self.left_container = QFrame(self.centralwidget)
        self.left_container.setObjectName(u"left_container")
        self.left_container.setMaximumSize(QSize(9, 16777215))
        self.left_container.setFrameShape(QFrame.StyledPanel)
        self.left_container.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.left_container)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(9, 9, 0, -1)
        self.frame = QFrame(self.left_container)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(-1, -1, 0, 9)
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_4.addWidget(self.label_3)


        self.verticalLayout_2.addWidget(self.frame)

        self.frame_2 = QFrame(self.left_container)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"QFrame{\n"
"background-color:rgb(65,65,65);\n"
"}\n"
"QToolBox{\n"
"text-align:left;\n"
"background-color:rgb(228,254,255);\n"
"}\n"
"QToolBox::tab{\n"
"\n"
"background-color:rgb(194,232,255);\n"
"}\n"
"")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, 0, 0, 0)
        self.toolBox = QToolBox(self.frame_2)
        self.toolBox.setObjectName(u"toolBox")
        self.toolBox.setStyleSheet(u"QPushButton{\n"
"	color:rgb(0,0,0);\n"
"	background-color:rgb(50,100,255);\n"
"	border-radius:15px;\n"
"}\n"
"QPushButton::hover{\n"
"background-color:rgb(66,66,111);\n"
"}\n"
"\n"
"")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.page.setGeometry(QRect(0, 0, 48, 498))
        self.page.setStyleSheet(u"")
        self.verticalLayout_4 = QVBoxLayout(self.page)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 10, 0, 0)
        self.btn_home = QPushButton(self.page)
        self.btn_home.setObjectName(u"btn_home")
        self.btn_home.setMinimumSize(QSize(0, 30))

        self.verticalLayout_4.addWidget(self.btn_home)

        self.btn_consulta = QPushButton(self.page)
        self.btn_consulta.setObjectName(u"btn_consulta")
        self.btn_consulta.setMinimumSize(QSize(0, 30))

        self.verticalLayout_4.addWidget(self.btn_consulta)

        self.btn_viagens = QPushButton(self.page)
        self.btn_viagens.setObjectName(u"btn_viagens")
        self.btn_viagens.setMinimumSize(QSize(0, 30))

        self.verticalLayout_4.addWidget(self.btn_viagens)

        self.btn_cadastrar = QPushButton(self.page)
        self.btn_cadastrar.setObjectName(u"btn_cadastrar")
        self.btn_cadastrar.setMinimumSize(QSize(0, 30))

        self.verticalLayout_4.addWidget(self.btn_cadastrar)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.toolBox.addItem(self.page, u"Op\u00e7\u00f5es")

        self.verticalLayout_3.addWidget(self.toolBox)


        self.verticalLayout_2.addWidget(self.frame_2)


        self.horizontalLayout.addWidget(self.left_container)

        self.main_container = QFrame(self.centralwidget)
        self.main_container.setObjectName(u"main_container")
        self.main_container.setMinimumSize(QSize(0, 600))
        self.main_container.setFrameShape(QFrame.StyledPanel)
        self.main_container.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.main_container)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, -1, -1, -1)
        self.top_frame = QFrame(self.main_container)
        self.top_frame.setObjectName(u"top_frame")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.top_frame.sizePolicy().hasHeightForWidth())
        self.top_frame.setSizePolicy(sizePolicy)
        self.top_frame.setFrameShape(QFrame.StyledPanel)
        self.top_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.top_frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btn_toggle = QPushButton(self.top_frame)
        self.btn_toggle.setObjectName(u"btn_toggle")
        icon = QIcon()
        icon.addFile(u":/Icons/menu2.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_toggle.setIcon(icon)
        self.btn_toggle.setIconSize(QSize(32, 32))

        self.horizontalLayout_2.addWidget(self.btn_toggle, 0, Qt.AlignLeft)

        self.label = QLabel(self.top_frame)
        self.label.setObjectName(u"label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label)


        self.verticalLayout.addWidget(self.top_frame)

        self.main_frame = QFrame(self.main_container)
        self.main_frame.setObjectName(u"main_frame")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.main_frame.sizePolicy().hasHeightForWidth())
        self.main_frame.setSizePolicy(sizePolicy2)
        self.main_frame.setFrameShape(QFrame.StyledPanel)
        self.main_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.main_frame)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.Pages = QStackedWidget(self.main_frame)
        self.Pages.setObjectName(u"Pages")
        self.pg_cadastrar = QWidget()
        self.pg_cadastrar.setObjectName(u"pg_cadastrar")
        self.pg_cadastrar.setStyleSheet(u"QLineEdit{\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton{\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"QTextEdit{\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.verticalLayout_6 = QVBoxLayout(self.pg_cadastrar)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.main_cadastro_pilotos = QFrame(self.pg_cadastrar)
        self.main_cadastro_pilotos.setObjectName(u"main_cadastro_pilotos")
        self.main_cadastro_pilotos.setFrameShape(QFrame.StyledPanel)
        self.main_cadastro_pilotos.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.main_cadastro_pilotos)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.titulo_cadastro_pilotos = QFrame(self.main_cadastro_pilotos)
        self.titulo_cadastro_pilotos.setObjectName(u"titulo_cadastro_pilotos")
        self.titulo_cadastro_pilotos.setMaximumSize(QSize(16777215, 40))
        self.titulo_cadastro_pilotos.setFrameShape(QFrame.StyledPanel)
        self.titulo_cadastro_pilotos.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.titulo_cadastro_pilotos)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.cadastro_pilotos_label = QLabel(self.titulo_cadastro_pilotos)
        self.cadastro_pilotos_label.setObjectName(u"cadastro_pilotos_label")
        font = QFont()
        font.setPointSize(12)
        self.cadastro_pilotos_label.setFont(font)
        self.cadastro_pilotos_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_15.addWidget(self.cadastro_pilotos_label)


        self.verticalLayout_11.addWidget(self.titulo_cadastro_pilotos)

        self.nome_frame = QFrame(self.main_cadastro_pilotos)
        self.nome_frame.setObjectName(u"nome_frame")
        self.nome_frame.setFrameShape(QFrame.StyledPanel)
        self.nome_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.nome_frame)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.nome_label = QLabel(self.nome_frame)
        self.nome_label.setObjectName(u"nome_label")
        self.nome_label.setFont(font)

        self.horizontalLayout_16.addWidget(self.nome_label)

        self.nomelineEdit = QLineEdit(self.nome_frame)
        self.nomelineEdit.setObjectName(u"nomelineEdit")
        self.nomelineEdit.setMaximumSize(QSize(300, 40))
        self.nomelineEdit.setFont(font)

        self.horizontalLayout_16.addWidget(self.nomelineEdit)


        self.verticalLayout_11.addWidget(self.nome_frame)

        self.cpf_frame = QFrame(self.main_cadastro_pilotos)
        self.cpf_frame.setObjectName(u"cpf_frame")
        self.cpf_frame.setFrameShape(QFrame.StyledPanel)
        self.cpf_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.cpf_frame)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.cpf_label = QLabel(self.cpf_frame)
        self.cpf_label.setObjectName(u"cpf_label")
        self.cpf_label.setFont(font)

        self.horizontalLayout_17.addWidget(self.cpf_label)

        self.cpf_lineEdit = QLineEdit(self.cpf_frame)
        self.cpf_lineEdit.setObjectName(u"cpf_lineEdit")
        self.cpf_lineEdit.setMaximumSize(QSize(300, 40))
        self.cpf_lineEdit.setFont(font)

        self.horizontalLayout_17.addWidget(self.cpf_lineEdit)


        self.verticalLayout_11.addWidget(self.cpf_frame)

        self.enviar_cadastro_piloto_frame = QFrame(self.main_cadastro_pilotos)
        self.enviar_cadastro_piloto_frame.setObjectName(u"enviar_cadastro_piloto_frame")
        self.enviar_cadastro_piloto_frame.setFrameShape(QFrame.StyledPanel)
        self.enviar_cadastro_piloto_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.enviar_cadastro_piloto_frame)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.btn_cadastro_piloto = QPushButton(self.enviar_cadastro_piloto_frame)
        self.btn_cadastro_piloto.setObjectName(u"btn_cadastro_piloto")
        self.btn_cadastro_piloto.setMaximumSize(QSize(200, 40))
        self.btn_cadastro_piloto.setStyleSheet(u"QPushButton{\n"
"border-radius:10px;\n"
"}\n"
"QPushButton::hover{\n"
"background-color: rgb(0, 170, 0);\n"
"}")

        self.horizontalLayout_18.addWidget(self.btn_cadastro_piloto)


        self.verticalLayout_11.addWidget(self.enviar_cadastro_piloto_frame)


        self.verticalLayout_6.addWidget(self.main_cadastro_pilotos)

        self.line = QFrame(self.pg_cadastrar)
        self.line.setObjectName(u"line")
        self.line.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_6.addWidget(self.line)

        self.main_cadastro_barcos = QFrame(self.pg_cadastrar)
        self.main_cadastro_barcos.setObjectName(u"main_cadastro_barcos")
        self.main_cadastro_barcos.setFrameShape(QFrame.StyledPanel)
        self.main_cadastro_barcos.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.main_cadastro_barcos)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.titulo_cadastr_barcos = QFrame(self.main_cadastro_barcos)
        self.titulo_cadastr_barcos.setObjectName(u"titulo_cadastr_barcos")
        self.titulo_cadastr_barcos.setFrameShape(QFrame.StyledPanel)
        self.titulo_cadastr_barcos.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.titulo_cadastr_barcos)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.cadastro_barcos_label = QLabel(self.titulo_cadastr_barcos)
        self.cadastro_barcos_label.setObjectName(u"cadastro_barcos_label")
        self.cadastro_barcos_label.setFont(font)
        self.cadastro_barcos_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_19.addWidget(self.cadastro_barcos_label)


        self.verticalLayout_12.addWidget(self.titulo_cadastr_barcos)

        self.modelo_frame = QFrame(self.main_cadastro_barcos)
        self.modelo_frame.setObjectName(u"modelo_frame")
        self.modelo_frame.setFrameShape(QFrame.StyledPanel)
        self.modelo_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.modelo_frame)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.modelo_label = QLabel(self.modelo_frame)
        self.modelo_label.setObjectName(u"modelo_label")
        self.modelo_label.setFont(font)

        self.horizontalLayout_20.addWidget(self.modelo_label)

        self.modelo_lineEdit = QLineEdit(self.modelo_frame)
        self.modelo_lineEdit.setObjectName(u"modelo_lineEdit")
        self.modelo_lineEdit.setMaximumSize(QSize(300, 40))
        self.modelo_lineEdit.setFont(font)

        self.horizontalLayout_20.addWidget(self.modelo_lineEdit)


        self.verticalLayout_12.addWidget(self.modelo_frame)

        self.motor_frame = QFrame(self.main_cadastro_barcos)
        self.motor_frame.setObjectName(u"motor_frame")
        self.motor_frame.setFrameShape(QFrame.StyledPanel)
        self.motor_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.motor_frame)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.motor_label = QLabel(self.motor_frame)
        self.motor_label.setObjectName(u"motor_label")
        self.motor_label.setFont(font)

        self.horizontalLayout_21.addWidget(self.motor_label)

        self.motor_lineEdit = QLineEdit(self.motor_frame)
        self.motor_lineEdit.setObjectName(u"motor_lineEdit")
        self.motor_lineEdit.setMaximumSize(QSize(300, 40))
        self.motor_lineEdit.setFont(font)

        self.horizontalLayout_21.addWidget(self.motor_lineEdit)


        self.verticalLayout_12.addWidget(self.motor_frame)

        self.enviar_cadastro_barco_frame = QFrame(self.main_cadastro_barcos)
        self.enviar_cadastro_barco_frame.setObjectName(u"enviar_cadastro_barco_frame")
        self.enviar_cadastro_barco_frame.setFrameShape(QFrame.StyledPanel)
        self.enviar_cadastro_barco_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.enviar_cadastro_barco_frame)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.btn_cadastro_barco = QPushButton(self.enviar_cadastro_barco_frame)
        self.btn_cadastro_barco.setObjectName(u"btn_cadastro_barco")
        self.btn_cadastro_barco.setMaximumSize(QSize(200, 40))
        self.btn_cadastro_barco.setStyleSheet(u"QPushButton{\n"
"border-radius:10px;\n"
"}\n"
"QPushButton::hover{\n"
"background-color: rgb(0, 170, 0);\n"
"}")

        self.horizontalLayout_22.addWidget(self.btn_cadastro_barco)


        self.verticalLayout_12.addWidget(self.enviar_cadastro_barco_frame)


        self.verticalLayout_6.addWidget(self.main_cadastro_barcos)

        self.Pages.addWidget(self.pg_cadastrar)
        self.pg_home = QWidget()
        self.pg_home.setObjectName(u"pg_home")
        self.pg_home.setStyleSheet(u"")
        self.horizontalLayout_6 = QHBoxLayout(self.pg_home)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.pg_home)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_6.addWidget(self.label_4)

        self.Pages.addWidget(self.pg_home)
        self.pg_viagens = QWidget()
        self.pg_viagens.setObjectName(u"pg_viagens")
        self.horizontalLayout_5 = QHBoxLayout(self.pg_viagens)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.tabWidget = QTabWidget(self.pg_viagens)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setStyleSheet(u"QLineEdit{\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"QComboBox{\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"QComboBox QAbstractItemView { background-color: lightblue; }\n"
"QPushButton{\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"QTextEdit{\n"
"background-color: rgb(255, 255, 255);"
"font-size:12pt;}")
        self.saida = QWidget()
        self.saida.setObjectName(u"saida")
        self.saida.setStyleSheet(u"")
        self.verticalLayout_7 = QVBoxLayout(self.saida)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(-1, 0, -1, 0)
        self.main_saida = QFrame(self.saida)
        self.main_saida.setObjectName(u"main_saida")
        self.main_saida.setFrameShape(QFrame.StyledPanel)
        self.main_saida.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.main_saida)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.Pilotos = QFrame(self.main_saida)
        self.Pilotos.setObjectName(u"Pilotos")
        self.Pilotos.setMinimumSize(QSize(0, 50))
        self.Pilotos.setFont(font)
        self.Pilotos.setFrameShape(QFrame.StyledPanel)
        self.Pilotos.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.Pilotos)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.pilotos_label = QLabel(self.Pilotos)
        self.pilotos_label.setObjectName(u"pilotos_label")
        self.pilotos_label.setFont(font)

        self.horizontalLayout_8.addWidget(self.pilotos_label)

        self.pilotos_comboBox = QComboBox(self.Pilotos)
        self.pilotos_comboBox.setObjectName(u"pilotos_comboBox")
        self.pilotos_comboBox.setMinimumSize(QSize(0, 40))
        self.pilotos_comboBox.setFont(font)

        self.horizontalLayout_8.addWidget(self.pilotos_comboBox)


        self.verticalLayout_9.addWidget(self.Pilotos)

        self.barcos = QFrame(self.main_saida)
        self.barcos.setObjectName(u"barcos")
        self.barcos.setMinimumSize(QSize(0, 50))
        self.barcos.setFont(font)
        self.barcos.setFrameShape(QFrame.StyledPanel)
        self.barcos.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.barcos)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.barcos_label = QLabel(self.barcos)
        self.barcos_label.setObjectName(u"barcos_label")
        self.barcos_label.setFont(font)

        self.horizontalLayout_9.addWidget(self.barcos_label)

        self.barcos_comboBox = QComboBox(self.barcos)
        self.barcos_comboBox.setObjectName(u"barcos_comboBox")
        self.barcos_comboBox.setMinimumSize(QSize(0, 40))
        self.barcos_comboBox.setFont(font)

        self.horizontalLayout_9.addWidget(self.barcos_comboBox)


        self.verticalLayout_9.addWidget(self.barcos)

        self.cliente = QFrame(self.main_saida)
        self.cliente.setObjectName(u"cliente")
        self.cliente.setMinimumSize(QSize(0, 150))
        self.cliente.setFrameShape(QFrame.StyledPanel)
        self.cliente.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_27 = QHBoxLayout(self.cliente)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.cliente_label = QLabel(self.cliente)
        self.cliente_label.setObjectName(u"cliente_label")

        self.horizontalLayout_27.addWidget(self.cliente_label)

        self.frame_4 = QFrame(self.cliente)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy1.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy1)
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_4)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.nome_cliente = QFrame(self.frame_4)
        self.nome_cliente.setObjectName(u"nome_cliente")
        self.nome_cliente.setFont(font)
        self.nome_cliente.setFrameShape(QFrame.StyledPanel)
        self.nome_cliente.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_28 = QHBoxLayout(self.nome_cliente)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.cliente_nome_label = QLabel(self.nome_cliente)
        self.cliente_nome_label.setObjectName(u"cliente_nome_label")
        sizePolicy1.setHeightForWidth(self.cliente_nome_label.sizePolicy().hasHeightForWidth())
        self.cliente_nome_label.setSizePolicy(sizePolicy1)
        self.cliente_nome_label.setFont(font)

        self.horizontalLayout_28.addWidget(self.cliente_nome_label)

        self.cliente_nome_lineEdit = QLineEdit(self.nome_cliente)
        self.cliente_nome_lineEdit.setObjectName(u"cliente_nome_lineEdit")
        self.cliente_nome_lineEdit.setEnabled(True)
        self.cliente_nome_lineEdit.setMinimumSize(QSize(0, 30))
        self.cliente_nome_lineEdit.setFont(font)

        self.horizontalLayout_28.addWidget(self.cliente_nome_lineEdit)


        self.verticalLayout_13.addWidget(self.nome_cliente)

        self.cpf_cliente = QFrame(self.frame_4)
        self.cpf_cliente.setObjectName(u"cpf_cliente")
        self.cpf_cliente.setFont(font)
        self.cpf_cliente.setFrameShape(QFrame.StyledPanel)
        self.cpf_cliente.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_29 = QHBoxLayout(self.cpf_cliente)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.cpf_cliente_label = QLabel(self.cpf_cliente)
        self.cpf_cliente_label.setObjectName(u"cpf_cliente_label")
        sizePolicy1.setHeightForWidth(self.cpf_cliente_label.sizePolicy().hasHeightForWidth())
        self.cpf_cliente_label.setSizePolicy(sizePolicy1)
        self.cpf_cliente_label.setFont(font)

        self.horizontalLayout_29.addWidget(self.cpf_cliente_label)

        self.cpf_cliente_lineEdit = QLineEdit(self.cpf_cliente)
        self.cpf_cliente_lineEdit.setObjectName(u"cpf_cliente_lineEdit")
        self.cpf_cliente_lineEdit.setMinimumSize(QSize(0, 30))
        self.cpf_cliente_lineEdit.setFont(font)

        self.horizontalLayout_29.addWidget(self.cpf_cliente_lineEdit)


        self.verticalLayout_13.addWidget(self.cpf_cliente)

        self.telefone_cliente = QFrame(self.frame_4)
        self.telefone_cliente.setObjectName(u"telefone_cliente")
        self.telefone_cliente.setFont(font)
        self.telefone_cliente.setFrameShape(QFrame.StyledPanel)
        self.telefone_cliente.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_30 = QHBoxLayout(self.telefone_cliente)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.telefone_cliente_label = QLabel(self.telefone_cliente)
        self.telefone_cliente_label.setObjectName(u"telefone_cliente_label")
        sizePolicy1.setHeightForWidth(self.telefone_cliente_label.sizePolicy().hasHeightForWidth())
        self.telefone_cliente_label.setSizePolicy(sizePolicy1)
        self.telefone_cliente_label.setFont(font)

        self.horizontalLayout_30.addWidget(self.telefone_cliente_label)

        self.telefone_cliente_lineEdit = QLineEdit(self.telefone_cliente)
        self.telefone_cliente_lineEdit.setObjectName(u"telefone_cliente_lineEdit")
        self.telefone_cliente_lineEdit.setMinimumSize(QSize(0, 30))
        self.telefone_cliente_lineEdit.setFont(font)

        self.horizontalLayout_30.addWidget(self.telefone_cliente_lineEdit)


        self.verticalLayout_13.addWidget(self.telefone_cliente)


        self.horizontalLayout_27.addWidget(self.frame_4)


        self.verticalLayout_9.addWidget(self.cliente)

        self.qtn_saida = QFrame(self.main_saida)
        self.qtn_saida.setObjectName(u"qtn_saida")
        self.qtn_saida.setMinimumSize(QSize(0, 50))
        self.qtn_saida.setFont(font)
        self.qtn_saida.setFrameShape(QFrame.StyledPanel)
        self.qtn_saida.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.qtn_saida)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.qtn_saida_label = QLabel(self.qtn_saida)
        self.qtn_saida_label.setObjectName(u"qtn_saida_label")
        self.qtn_saida_label.setFont(font)

        self.horizontalLayout_10.addWidget(self.qtn_saida_label)

        self.qtn_saida_lineEdit = QLineEdit(self.qtn_saida)
        self.qtn_saida_lineEdit.setObjectName(u"qtn_saida_lineEdit")
        self.qtn_saida_lineEdit.setMinimumSize(QSize(0, 40))
        self.qtn_saida_lineEdit.setMaximumSize(QSize(340, 40))
        self.qtn_saida_lineEdit.setFont(font)
        self.qtn_saida_lineEdit.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_10.addWidget(self.qtn_saida_lineEdit)


        self.verticalLayout_9.addWidget(self.qtn_saida)

        self.enviar = QFrame(self.main_saida)
        self.enviar.setObjectName(u"enviar")
        self.enviar.setFrameShape(QFrame.StyledPanel)
        self.enviar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.enviar)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.btn_enviar = QPushButton(self.enviar)
        self.btn_enviar.setObjectName(u"btn_enviar")
        self.btn_enviar.setMinimumSize(QSize(0, 40))
        self.btn_enviar.setMaximumSize(QSize(200, 50))
        self.btn_enviar.setFont(font)
        self.btn_enviar.setStyleSheet(u"QPushButton{\n"
"	border-radius:10px;\n"
"}\n"
"QPushButton::hover{\n"
"	\n"
"	background-color: rgb(0, 170, 0);\n"
"}")

        self.horizontalLayout_11.addWidget(self.btn_enviar)


        self.verticalLayout_9.addWidget(self.enviar)


        self.verticalLayout_7.addWidget(self.main_saida)

        self.tabWidget.addTab(self.saida, "")
        self.volta = QWidget()
        self.volta.setObjectName(u"volta")
        self.verticalLayout_8 = QVBoxLayout(self.volta)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.main_volta = QFrame(self.volta)
        self.main_volta.setObjectName(u"main_volta")
        self.main_volta.setFrameShape(QFrame.StyledPanel)
        self.main_volta.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.main_volta)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.id_viagem = QFrame(self.main_volta)
        self.id_viagem.setObjectName(u"id_viagem")
        self.id_viagem.setFrameShape(QFrame.StyledPanel)
        self.id_viagem.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.id_viagem)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.id_label = QLabel(self.id_viagem)
        self.id_label.setObjectName(u"id_label")
        self.id_label.setFont(font)

        self.horizontalLayout_12.addWidget(self.id_label)

        self.id_lineEdit = QLineEdit(self.id_viagem)
        self.id_lineEdit.setObjectName(u"id_lineEdit")
        self.id_lineEdit.setMaximumSize(QSize(300, 40))

        self.horizontalLayout_12.addWidget(self.id_lineEdit)


        self.verticalLayout_10.addWidget(self.id_viagem)

        self.qtd_volta_frame = QFrame(self.main_volta)
        self.qtd_volta_frame.setObjectName(u"qtd_volta_frame")
        self.qtd_volta_frame.setFrameShape(QFrame.StyledPanel)
        self.qtd_volta_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.qtd_volta_frame)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.qtn_volta_label = QLabel(self.qtd_volta_frame)
        self.qtn_volta_label.setObjectName(u"qtn_volta_label")
        self.qtn_volta_label.setFont(font)

        self.horizontalLayout_13.addWidget(self.qtn_volta_label)

        self.qtn_volta_lineEdit = QLineEdit(self.qtd_volta_frame)
        self.qtn_volta_lineEdit.setObjectName(u"qtn_volta_lineEdit")
        self.qtn_volta_lineEdit.setMaximumSize(QSize(300, 40))

        self.horizontalLayout_13.addWidget(self.qtn_volta_lineEdit)


        self.verticalLayout_10.addWidget(self.qtd_volta_frame)

        self.enviar_volta_frame = QFrame(self.main_volta)
        self.enviar_volta_frame.setObjectName(u"enviar_volta_frame")
        self.enviar_volta_frame.setFrameShape(QFrame.StyledPanel)
        self.enviar_volta_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.enviar_volta_frame)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.btn_enviar_volta = QPushButton(self.enviar_volta_frame)
        self.btn_enviar_volta.setObjectName(u"btn_enviar_volta")
        self.btn_enviar_volta.setMaximumSize(QSize(200, 40))
        self.btn_enviar_volta.setStyleSheet(u"QPushButton{\n"
"	border-radius:10px\n"
"}\n"
"QPushButton::hover{\n"
"	background-color: rgb(0, 170, 0);\n"
"}")

        self.horizontalLayout_14.addWidget(self.btn_enviar_volta)


        self.verticalLayout_10.addWidget(self.enviar_volta_frame)


        self.verticalLayout_8.addWidget(self.main_volta)

        self.tabWidget.addTab(self.volta, "")

        self.horizontalLayout_5.addWidget(self.tabWidget)

        self.Pages.addWidget(self.pg_viagens)
        self.pg_consulta = QWidget()
        self.pg_consulta.setObjectName(u"pg_consulta")
        self.pg_consulta.setStyleSheet(u"QTextEdit{\n"
"background-color: rgb(255, 255, 255);\n"
"font-size:12pt;}\n")
        
        self.horizontalLayout_7 = QHBoxLayout(self.pg_consulta)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.consulta_tabWidget = QTabWidget(self.pg_consulta)
        self.consulta_tabWidget.setObjectName(u"consulta_tabWidget")
        self.consulta_viagens_aba = QWidget()
        self.consulta_viagens_aba.setObjectName(u"consulta_viagens_aba")
        self.horizontalLayout_23 = QHBoxLayout(self.consulta_viagens_aba)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.consulta_viagens_frame = QFrame(self.consulta_viagens_aba)
        self.consulta_viagens_frame.setObjectName(u"consulta_viagens_frame")
        self.consulta_viagens_frame.setFrameShape(QFrame.StyledPanel)
        self.consulta_viagens_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_24 = QHBoxLayout(self.consulta_viagens_frame)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.text_consulta_viagens = QTextEdit(self.consulta_viagens_frame)
        self.text_consulta_viagens.setObjectName(u"text_consulta_viagens")

        self.horizontalLayout_24.addWidget(self.text_consulta_viagens)


        self.horizontalLayout_23.addWidget(self.consulta_viagens_frame)

        self.consulta_tabWidget.addTab(self.consulta_viagens_aba, "")
        self.consulta_barcos_aba = QWidget()
        self.consulta_barcos_aba.setObjectName(u"consulta_barcos_aba")
        self.horizontalLayout_25 = QHBoxLayout(self.consulta_barcos_aba)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.consulta_barcos_frame = QFrame(self.consulta_barcos_aba)
        self.consulta_barcos_frame.setObjectName(u"consulta_barcos_frame")
        self.consulta_barcos_frame.setFrameShape(QFrame.StyledPanel)
        self.consulta_barcos_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_26 = QHBoxLayout(self.consulta_barcos_frame)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.consulta_barcos = QTextEdit(self.consulta_barcos_frame)
        self.consulta_barcos.setObjectName(u"consulta_barcos")

        self.horizontalLayout_26.addWidget(self.consulta_barcos)


        self.horizontalLayout_25.addWidget(self.consulta_barcos_frame)

        self.consulta_tabWidget.addTab(self.consulta_barcos_aba, "")

        self.horizontalLayout_7.addWidget(self.consulta_tabWidget)

        self.Pages.addWidget(self.pg_consulta)

        self.verticalLayout_5.addWidget(self.Pages)


        self.verticalLayout.addWidget(self.main_frame)

        self.footer = QFrame(self.main_container)
        self.footer.setObjectName(u"footer")
        self.footer.setLayoutDirection(Qt.LeftToRight)
        self.footer.setFrameShape(QFrame.StyledPanel)
        self.footer.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.footer)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel(self.footer)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_3.addWidget(self.label_2)


        self.verticalLayout.addWidget(self.footer)


        self.horizontalLayout.addWidget(self.main_container)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.toolBox.setCurrentIndex(0)
        self.Pages.setCurrentIndex(1) #Altera a pagina que inicializa
        self.tabWidget.setCurrentIndex(0)
        self.consulta_tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"", None))
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.btn_consulta.setText(QCoreApplication.translate("MainWindow", u"Consulta", None))
        self.btn_viagens.setText(QCoreApplication.translate("MainWindow", u"Viagens", None))
        self.btn_cadastrar.setText(QCoreApplication.translate("MainWindow", u"Cadastrar", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), QCoreApplication.translate("MainWindow", u"Op\u00e7\u00f5es", None))
        self.btn_toggle.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Sistema de Controle", None))
        self.cadastro_pilotos_label.setText(QCoreApplication.translate("MainWindow", u"Cadastro de Pilotos", None))
        self.nome_label.setText(QCoreApplication.translate("MainWindow", u"Nome:", None))
        self.cpf_label.setText(QCoreApplication.translate("MainWindow", u"CPF:", None))
        self.btn_cadastro_piloto.setText(QCoreApplication.translate("MainWindow", u"Cadastrar Piloto", None))
        self.cadastro_barcos_label.setText(QCoreApplication.translate("MainWindow", u"Cadastro de Barcos", None))
        self.modelo_label.setText(QCoreApplication.translate("MainWindow", u"Modelo", None))
        self.motor_label.setText(QCoreApplication.translate("MainWindow", u"Motor / N\u00b0 Serie", None))
        self.btn_cadastro_barco.setText(QCoreApplication.translate("MainWindow", u"Cadastrar Barco", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">SISTEMA DE CONTROLE<br/>SEJA BEM-VNDO</span></p><p align=\"center\"><br/></p></body></html>", None))
        self.pilotos_label.setText(QCoreApplication.translate("MainWindow", u"Piloto:", None))
        self.barcos_label.setText(QCoreApplication.translate("MainWindow", u"Barcos:", None))
        self.cliente_label.setText(QCoreApplication.translate("MainWindow", u"Cliente:", None))
        self.cliente_nome_label.setText(QCoreApplication.translate("MainWindow", u"Nome:", None))
        self.cpf_cliente_label.setText(QCoreApplication.translate("MainWindow", u"CPF:", None))
        self.telefone_cliente_label.setText(QCoreApplication.translate("MainWindow", u"Telefone:", None))
        self.qtn_saida_label.setText(QCoreApplication.translate("MainWindow", u"Gasolina Saida:", None))
        self.btn_enviar.setText(QCoreApplication.translate("MainWindow", u"Enviar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.saida), QCoreApplication.translate("MainWindow", u"Saida", None))
        self.id_label.setText(QCoreApplication.translate("MainWindow", u"Digite o Codigo da Viagem", None))
        self.qtn_volta_label.setText(QCoreApplication.translate("MainWindow", u"Gasolina Volta:", None))
        self.btn_enviar_volta.setText(QCoreApplication.translate("MainWindow", u"Enviar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.volta), QCoreApplication.translate("MainWindow", u"Volta", None))
        self.consulta_tabWidget.setTabText(self.consulta_tabWidget.indexOf(self.consulta_viagens_aba), QCoreApplication.translate("MainWindow", u"Viagens", None))
        self.consulta_tabWidget.setTabText(self.consulta_tabWidget.indexOf(self.consulta_barcos_aba), QCoreApplication.translate("MainWindow", u"Barcos", None))
        self.label_2.setText("")
    # retranslateUi


# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_Login(object):
    def setupUi(self, Login):
        if not Login.objectName():
            Login.setObjectName(u"Login")
        Login.resize(500, 200)
        Login.setMaximumSize(QSize(500, 200))
        Login.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"QLabel{\n"
"color:rgb(255,255,255);\n"
"}")
        self.verticalLayout = QVBoxLayout(Login)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.usuario_frame = QFrame(Login)
        self.usuario_frame.setObjectName(u"usuario_frame")
        self.usuario_frame.setStyleSheet(u"QLabel{\n"
"color:rgb(255,255,255);\n"
"}\n"
"QLineEdit{\n"
"background:rgb(255,255,255);\n"
"}")
        self.usuario_frame.setFrameShape(QFrame.StyledPanel)
        self.usuario_frame.setFrameShadow(QFrame.Raised)
        self.usuario_label = QLabel(self.usuario_frame)
        self.usuario_label.setObjectName(u"usuario_label")
        self.usuario_label.setGeometry(QRect(90, 30, 61, 16))
        font = QFont()
        font.setPointSize(12)
        self.usuario_label.setFont(font)
        self.usuario_label.setStyleSheet(u"")
        self.usuario_lineEdit = QLineEdit(self.usuario_frame)
        self.usuario_lineEdit.setObjectName(u"usuario_lineEdit")
        self.usuario_lineEdit.setGeometry(QRect(220, 30, 200, 21))
        self.usuario_lineEdit.setMinimumSize(QSize(200, 21))

        self.verticalLayout.addWidget(self.usuario_frame)

        self.senha_frame = QFrame(Login)
        self.senha_frame.setObjectName(u"senha_frame")
        self.senha_frame.setStyleSheet(u"QLabel{\n"
"color:rgb(255,255,255);\n"
"}\n"
"QLineEdit{\n"
"background:rgb(255,255,255);\n"
"}")
        self.senha_frame.setFrameShape(QFrame.StyledPanel)
        self.senha_frame.setFrameShadow(QFrame.Raised)
        self.senha_label = QLabel(self.senha_frame)
        self.senha_label.setObjectName(u"senha_label")
        self.senha_label.setGeometry(QRect(90, 20, 51, 16))
        self.senha_label.setFont(font)
        self.senha_label.setStyleSheet(u"")
        self.senha_lineEdit = QLineEdit(self.senha_frame)
        self.senha_lineEdit.setObjectName(u"senha_lineEdit")
        self.senha_lineEdit.setGeometry(QRect(220, 20, 200, 21))
        self.senha_lineEdit.setMinimumSize(QSize(200, 21))
        self.senha_lineEdit.setEchoMode(QLineEdit.Password)

        self.verticalLayout.addWidget(self.senha_frame)

        self.login_frame = QFrame(Login)
        self.login_frame.setObjectName(u"login_frame")
        self.login_frame.setStyleSheet(u"QPushButton{\n"
"background:rgb(255,255,255);\n"
"}")
        self.login_frame.setFrameShape(QFrame.StyledPanel)
        self.login_frame.setFrameShadow(QFrame.Raised)
        self.btn_login = QPushButton(self.login_frame)
        self.btn_login.setObjectName(u"btn_login")
        self.btn_login.setGeometry(QRect(210, 10, 81, 31))
        self.btn_login.setFont(font)
        self.btn_login.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_login.setStyleSheet(u"QPushButton{	\n"
"	border-radius:10px\n"
"}\n"
"QPushButton::hover{	\n"
"	background: rgb(0, 170, 0);\n"
"}")

        self.verticalLayout.addWidget(self.login_frame)


        self.retranslateUi(Login)

        QMetaObject.connectSlotsByName(Login)
    # setupUi

    def retranslateUi(self, Login):
        Login.setWindowTitle(QCoreApplication.translate("Login", u"Form", None))
        self.usuario_label.setText(QCoreApplication.translate("Login", u"Usu\u00e1rio", None))
        self.senha_label.setText(QCoreApplication.translate("Login", u"Senha", None))
        self.btn_login.setText(QCoreApplication.translate("Login", u"Login", None))
    # retranslateUi


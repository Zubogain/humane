# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore

import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(240, 250)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(0, 0))
        self.centralwidget.setStyleSheet(u"background-color: rgba(47, 47, 59, 0.8);")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, -1, -1, -1)
        self.header = QFrame(self.centralwidget)
        self.header.setObjectName(u"header")
        self.header.setMinimumSize(QSize(0, 20))
        self.header.setMaximumSize(QSize(16777215, 20))
        self.header.setStyleSheet(u"QFrame {\n"
"	background-color: rgba(47, 47, 59, 0.9);\n"
"}")
        self.header.setFrameShape(QFrame.StyledPanel)
        self.header.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.header)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.pushButton = QPushButton(self.header)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(0, 0))
        self.pushButton.setMaximumSize(QSize(18, 16777215))
        self.pushButton.setStyleSheet(u"image: url(:/icons/logo.svg);\n"
"padding: 0;\n"
"margin: 0;\n"
"background-repeat: no-repeat;\n"
"background-color: transparent;")

        self.horizontalLayout_4.addWidget(self.pushButton, 0, Qt.AlignLeft|Qt.AlignVCenter)

        self.headerControls = QFrame(self.header)
        self.headerControls.setObjectName(u"headerControls")
        self.headerControls.setFrameShape(QFrame.StyledPanel)
        self.headerControls.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.headerControls)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.headerControlsHide = QPushButton(self.headerControls)
        self.headerControlsHide.setObjectName(u"headerControlsHide")
        self.headerControlsHide.setMinimumSize(QSize(30, 0))
        self.headerControlsHide.setMaximumSize(QSize(30, 16777215))
        self.headerControlsHide.setCursor(QCursor(Qt.PointingHandCursor))
        self.headerControlsHide.setStyleSheet(u"QPushButton {\n"
"	background-color: #929292;\n"
"	border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #c4c4c4;\n"
"}")

        self.horizontalLayout_5.addWidget(self.headerControlsHide)

        self.headerControlsExit = QPushButton(self.headerControls)
        self.headerControlsExit.setObjectName(u"headerControlsExit")
        self.headerControlsExit.setMinimumSize(QSize(45, 0))
        self.headerControlsExit.setMaximumSize(QSize(45, 16777215))
        self.headerControlsExit.setCursor(QCursor(Qt.PointingHandCursor))
        self.headerControlsExit.setStyleSheet(u"QPushButton {\n"
"	background-color: #F16969;\n"
"	border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #f28f8f;\n"
"}")

        self.horizontalLayout_5.addWidget(self.headerControlsExit)


        self.horizontalLayout_4.addWidget(self.headerControls, 0, Qt.AlignRight)


        self.verticalLayout.addWidget(self.header)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setEnabled(True)
        self.frame.setMaximumSize(QSize(16777215, 16777215))
        self.frame.setStyleSheet(u"QFrame {\n"
"	background-color: rgba(47, 47, 59, 0.9);\n"
"}\n"
"\n"
"\n"
"QPushButton {\n"
"	background: rgba(59, 59, 69, 0.5);\n"
"	border: 1px solid rgba(59, 59, 69,0.5);\n"
"	border-radius: 4px;\n"
"	font-size: 16px;\n"
"\n"
"	color: #EBEBEB;\n"
"\n"
"	padding-left:12px;\n"
"	padding-right:12px;\n"
"	padding-top: 7px;\n"
"	padding-bottom: 7px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background: #51515C;\n"
"	border: 1px solid rgba(81, 81, 92, 0.5);\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"	background: #44444d;\n"
"	border: 1px solid rgba(81, 81, 92, 0.5);\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"	background: rgba(0, 0, 0, 0.1);\n"
"	border: 1px solid rgba(0, 0, 0, 0.1);\n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setSpacing(15)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(15, 15, 15, 15)
        self.start = QPushButton(self.frame)
        self.start.setObjectName(u"start")
        self.start.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_3.addWidget(self.start)

        self.pause = QPushButton(self.frame)
        self.pause.setObjectName(u"pause")
        self.pause.setEnabled(True)
        self.pause.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_3.addWidget(self.pause)

        self.quit = QPushButton(self.frame)
        self.quit.setObjectName(u"quit")
        self.quit.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_3.addWidget(self.quit)


        self.verticalLayout.addWidget(self.frame)

        self.footer = QFrame(self.centralwidget)
        self.footer.setObjectName(u"footer")
        self.footer.setMaximumSize(QSize(16777215, 40))
        self.footer.setStyleSheet(u"QFrame {\n"
"	background-color: rgba(47, 47, 59, 0.9);\n"
"}\n"
"\n"
"QLabel  {\n"
"	border: none;\n"
"	background-color: transparent;\n"
"	padding: 0;\n"
"}")
        self.footer.setFrameShape(QFrame.StyledPanel)
        self.footer.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.footer)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.footer)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"QFrame {\n"
"	background-color: transparent;\n"
"}")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.frame_3)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"QLabel {\n"
"	font-size: 16px;;\n"
"	color: #EBEBEB;\n"
"}")

        self.horizontalLayout_2.addWidget(self.label)

        self.label_2 = QLabel(self.frame_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"QLabel {\n"
"	font-size: 14px;\n"
"	color: #d9d9d9;\n"
"}")

        self.horizontalLayout_2.addWidget(self.label_2)


        self.horizontalLayout.addWidget(self.frame_3, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout.addWidget(self.footer)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Humane", None))
        self.pushButton.setText("")
        self.headerControlsHide.setText("")
        self.headerControlsExit.setText("")
        self.start.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.pause.setText(QCoreApplication.translate("MainWindow", u"Pause", None))
        self.quit.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Humane", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"v1.0.0", None))
    # retranslateUi


import sys
import functools
from PySide6.QtCore import QPoint, QSize, Slot, QThread, Signal, QTimer
from PySide6.QtWidgets import QHBoxLayout, QApplication, QMainWindow, QWidget
from PySide6.QtGui import QIcon, QScreen, Qt, QCursor
from BlurWindow.blurWindow import blur

from ui import Ui_MainWindow


import asyncio
import qasync
from qasync import asyncSlot, asyncClose, QApplication
from random import *
import pyautogui as py


class UIMainWindow(Ui_MainWindow):
    isStarted = False
    intervalTimer = 1.2
    timer = None

    def __init__(self, qMainWindow):
        super().__init__()

        self.__qMainWindow = qMainWindow

        self.screen = self.__qMainWindow.screen()
        self.devicePixelRatio = self.screen.devicePixelRatio()
        self.screenWidth = round(
            self.screen.size().width() * self.devicePixelRatio)
        self.screenHeight = round(
            self.screen.size().height() * self.devicePixelRatio)

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)

        self.__setupWIndowControls()
        self.__setupStartButton()
        self.__setupPauseButton()
        self.pauseButtonMouseClick()

    def __setupWIndowControls(self):
        self.headerControlsHide.hide()
        self.quit.clicked.connect(self.__qMainWindow.closeAll)
        self.headerControlsExit.clicked.connect(self.__qMainWindow.closeAll)

    def __setupStartButton(self):
        self.start.clicked.connect(self.startButtonMouseClick)

    def __setupPauseButton(self):
        self.pause.clicked.connect(self.pauseButtonMouseClick)

    def __intervalMouseMoving(self):
        print("__intervalMouseMoving")
        if UIMainWindow.isStarted:
            py.moveTo(randint(0, self.screenWidth), randint(0, self.screenHeight),
                      uniform(0.6, 1.6), py.easeOutBack)

    def intervalMouseMoving(self):
        UIMainWindow.timer = QTimer()
        UIMainWindow.timer.timeout.connect(self.__intervalMouseMoving)
        UIMainWindow.timer.setInterval(randint(1620, 2000))
        UIMainWindow.timer.start()

        # py.moveTo(720, 360, uniform(0.6, 1.7), py.easeOutQuad)
        # py.moveTo(450, 900, uniform(0.6, 1.7), py.easeOutBack)
        # py.moveTo(360, 720, uniform(0.6, 1.7), py.easeInOutQuad)

    @Slot()
    def startButtonMouseClick(self):
        if not UIMainWindow.isStarted:
            UIMainWindow.isStarted = True
            self.start.setDisabled(True)
            self.pause.setDisabled(False)
            self.intervalMouseMoving()
        else:
            self.start.setDisabled(False)
            self.pause.setDisabled(True)

        print("Mouse move event")

    @Slot(str)
    def pauseButtonMouseClick(self, signal="normal"):
        UIMainWindow.isStarted = False

        if signal == 'middle':
            self.__qMainWindow.closeAll()

        if signal == 'right' or signal == 'normal':
            self.start.setDisabled(False)
            self.pause.setDisabled(True)

        print("Mouse pause event")

import sys
import functools
from PySide6.QtCore import QPoint, QSize, Signal
from PySide6.QtWidgets import QHBoxLayout, QApplication, QMainWindow, QWidget
from PySide6.QtGui import QIcon, Qt
from BlurWindow.blurWindow import blur

from UIMainWindow import UIMainWindow
from WatchMouseClick import WatchMouseClick


import asyncio
import qasync
from qasync import asyncSlot, asyncClose, QApplication


class UIMainWindowWrapper(QMainWindow):
    handleRigthButtonClick = Signal(str)

    def __init__(self):
        super().__init__()

        # Basic setup
        self.setWindowTitle("Humane")
        self.setWindowIcon(QIcon(":/icons/logo.svg"))
        self.setStyleSheet("background-color: rgba(0, 0, 0, 0)")
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        # self.setWindowFlag(Qt.Tool)
        self.setCentralWidget(QWidget(self))
        self.hbox = QHBoxLayout()
        self.centralWidget().setLayout(self.hbox)

        blur(self.winId())

        self.oldPos = None

        self.mainWindow = UIMainWindow(self)
        self.watchMouseClick = WatchMouseClick(self.handleRigthButtonClick)
        self.handleRigthButtonClick.connect(
            self.mainWindow.pauseButtonMouseClick)

    def updateWindowSize(self, width, height):
        size = QSize()
        size.setWidth(width)
        size.setHeight(height)

        self.setMinimumSize(size)
        self.setMaximumSize(size)

    # called when the mouse button is pressed
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.oldPos = event.globalPosition().toPoint()

    # called when the mouse button is released
    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.oldPos = None

    # called whenever the mouse moves
    def mouseMoveEvent(self, event):
        if not self.oldPos:
            return
        globalPos = event.globalPosition().toPoint()
        delta = QPoint(globalPos - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = globalPos

    def setupUi(self):
        self.mainWindow.setupUi(self)
        self.show()

    def closeAll(self):
        # close main window
        self.close()

    @asyncClose
    async def closeEvent(self, event):
        self.closeAll()


async def main():
    def close_future(future, loop):
        loop.call_later(10, future.cancel)
        future.cancel()

    loop = asyncio.get_event_loop()
    future = asyncio.Future()

    app = QApplication.instance()
    if hasattr(app, "aboutToQuit"):
        getattr(app, "aboutToQuit").connect(
            functools.partial(close_future, future, loop)
        )

    uiMainWindowWrapper = UIMainWindowWrapper()
    uiMainWindowWrapper.setupUi()

    await future
    return True


if __name__ == "__main__":
    try:
        qasync.run(main())
    except asyncio.exceptions.CancelledError:
        sys.exit(0)

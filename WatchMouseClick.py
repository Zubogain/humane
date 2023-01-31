from PySide6.QtCore import QObject
from pynput import mouse


class WatchMouseClick(QObject):
    def __init__(self, signalToEmit, parent=None):
        super().__init__(parent)

        self.signalToEmit = signalToEmit

        self.listener = mouse.Listener(on_click=self.mouseClickHandler)
        self.run()

    def mouseClickHandler(self, x, y, button, pressed):
        print(button)

        if button == mouse.Button.right:
            self.signalToEmit.emit('right')

        if button == mouse.Button.middle:
            self.signalToEmit.emit('middle')

    def run(self):
        self.listener.start()

    def stop(self):
        self.listener.stop()

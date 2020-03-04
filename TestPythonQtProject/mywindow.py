# This Python file uses the following encoding: utf-8
import sys
from PySide2.QtCore import QUrl
from PySide2.QtWidgets import QApplication, QMainWindow
from PySide2.QtQuickWidgets import QQuickWidget

class MyWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.map = QQuickWidget(QUrl('MapBoxGL.qml'))



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTabWidget, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton,QMessageBox
from PyQt5 import uic

## CLASES VISOR 3D
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl

## LLAMAMOS A LA INTERFACE
window_name, base_class = uic.loadUiType("Led.ui")


class MainWindow(window_name, base_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    # Enlace del diseño 3D de Fusion 360
        url = QUrl('https://a360.co/4fz2ErE')
        # Cargar el enlace en el visor web
        self.graph3d.setUrl(url)
                # Enlace del diseño 3D de Fusion 360

    def conectar(self):
        print('Conectar')
    def actualizar(self):
        print('actualizar')
    def desconectar(self):
        print('desconectar')

        
if __name__ == '__main__':
    app = QApplication([])
    form = MainWindow()
    form.show()
    sys.exit(app.exec())
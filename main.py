import sys
import ctypes
from PyQt5.QtWidgets import QApplication, QWidget, QSystemTrayIcon #QPushButton, QLabel, QVBoxLayout, QHBoxLayout, 
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon #, QFontDatabase, 
# from PyQt5.QtMultimedia import QSound
from pyautogui import size
import json
from qss_stylesheet import *

WIDTH, HEIGHT = size()

myappid = 'JFLP.MarugotoA21.0.1' 
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

def run():
    app = QApplication([])
    app.setApplicationName("Marugoto A2-1")
    app.setOrganizationName("Japanese-Freeware-learning-project") 
    app.setApplicationVersion("0.1")
    window = MainWindow()
    app.exec_()


class MainWindow(QWidget):
    def __init__(self, parent=None, flags=Qt.WindowFlags()):
        super().__init__(parent=parent, flags=flags)

        self.is_light_mode = True
        self.language = "en"
        self.notifier = QSystemTrayIcon(self)

        self.set_language()
        self.config_window()
        self.event_handler()
        self.welcome_screen()

        self.notifier.show()

        self.show()

    def config_window(self):
        main_icon = QIcon("data/local/images/logo.ico")
        self.notifier.setToolTip("Marugoto A2-1")
        self.setWindowTitle(self.title)
        self.setGeometry(0, 0, WIDTH, HEIGHT)
        if self.is_light_mode:
            self.setStyleSheet(f"background-color: rgb{WINDOW_LIGHT};")
        else:
            self.setStyleSheet(f"background-color: rgb{WINDOW_DARK};")
        self.setWindowIcon(main_icon)
        self.notifier.setIcon(main_icon)

    def set_language(self):
        language_archive = f"data/local/languages/{self.language}.json"
        
        # 1. Abrimos y cargamos el contenido del JSON
        with open(language_archive, 'r', encoding='utf-8') as archivo:
            language = json.load(archivo)
        
        # 2. Ahora sí, accedemos a los datos como un diccionario
        self.title = language["text"]["title"]
        self.description = language["text"]["description"]

        print("Language set to:", self.language, "loaded properly")

    def welcome_screen(self):
        pass
    
    def event_handler(self):
        pass

print("Starting Marugoto A2-1...")
run()

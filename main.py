import sys
import ctypes
from PyQt5.QtWidgets import QApplication, QWidget, QSystemTrayIcon, QPushButton, QLabel, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
# from PyQt5.QtMultimedia import QSound
from pyautogui import size
import json
from qss_stylesheet import *
from conjugation_func import *

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
        self.notifier = QSystemTrayIcon(self)

        self.config_file = "data/local/config.json"
        with open(self.config_file, 'r', encoding='utf-8') as archivo:
            config = json.load(archivo)
        
        self.language = config.get("language", "en")
        self.is_light_mode = config.get("is_light_mode", True)

        self.set_language()
        self.titles_style, self.text_style, self.button_style = get_stylesheet(self.is_light_mode)
        self.config_window()
        self.event_handler()
        self.welcome_screen()

        self.notifier.show()

        self.show()

    def config_window(self):
        main_icon = QIcon("data/local/images/logo.ico")
        self.notifier.setToolTip("Marugoto A2-1")
        self.setWindowTitle(self.title_tt)
        self.setGeometry(0, 0, WIDTH, HEIGHT)
        if self.is_light_mode:
            self.setStyleSheet(f"background-color: rgb{WINDOW_LIGHT};")
        else:
            self.setStyleSheet(f"background-color: rgb{WINDOW_DARK};")
        self.setWindowIcon(main_icon)
        self.notifier.setIcon(main_icon)

    def set_language(self):
        language_archive = f"data/local/languages/{self.language}.json"
        
        # Open and load the JSON file for the language here
        with open(language_archive, 'r', encoding='utf-8') as archivo:
            language = json.load(archivo)
        
        # then you set variables for the text you want to use in the GUI! completely dynamic :3
        self.title_tt = language["text"]["title"]
        self.description_txt = language["text"]["description"]

        print("Language set to:", self.language, "loaded properly")

    def welcome_screen(self):
        self.title_text = QLabel(self.title_tt, self)
        self.title_text.setStyleSheet(self.titles_style)
        self.description = QLabel(self.description_txt, self)
        self.description.setStyleSheet(self.text_style)

        main_Layout = QVBoxLayout()
        main_Layout.addWidget(self.title_text, alignment=Qt.AlignBottom)
        main_Layout.addWidget(self.description, alignment=Qt.AlignCenter)
        self.setLayout(main_Layout)

    def event_handler(self):
        pass

print("Starting Marugoto A2-1...")
run()

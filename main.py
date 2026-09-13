import sys
import ctypes
from PyQt5.QtWidgets import QApplication, QWidget, QSystemTrayIcon, QPushButton, QLabel, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
# from PyQt5.QtMultimedia import QSound
from pyautogui import size
import json
from qss_stylesheet import *
from conjugation_v import *

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
        self.main_menu()

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
        language_file = f"data/local/languages/{self.language}.json"
        
        # Open and load the JSON file for the language here
        with open(language_file, 'r', encoding='utf-8') as archivo:
            language = json.load(archivo)
        
        # then you set variables for the text you want to use in the GUI! completely dynamic :3
        self.title_tt = language["text"]["title"]
        self.description_txt = language["text"]["description"]
        self.lessons_btn = language["button"]["lessons"]
        self.dict_btn = language["button"]["dictionary"]
        self.settings_btn = language["button"]["settings"]
        self.exit_btn = language["button"]["exit"]

        print("Language set to:", self.language, "loaded properly")

    def main_menu(self):
        title_text = QLabel(self.title_tt, self)
        description = QLabel(self.description_txt, self)
        lessons_button = QPushButton(self.lessons_btn, self)
        dictionary_button = QPushButton(self.dict_btn, self)
        settings_button = QPushButton(self.settings_btn, self)
        self.exit_button = QPushButton(self.exit_btn, self)
        
        self.apply_style(title_text, self.titles_style)
        self.apply_style(description, self.text_style)
        self.apply_style(lessons_button, self.button_style)
        self.apply_style(dictionary_button, self.button_style)
        self.apply_style(settings_button, self.button_style)
        self.apply_style(self.exit_button, self.button_style)

        buttons_layout = QVBoxLayout()
        buttons_layout.setSpacing(32)
        buttons_layout.setContentsMargins(32, 0, 0, 0)
        buttons_layout.addWidget(lessons_button, alignment=Qt.AlignLeft)
        buttons_layout.addWidget(dictionary_button, alignment=Qt.AlignLeft)
        buttons_layout.addWidget(settings_button, alignment=Qt.AlignLeft)
        buttons_layout.addWidget(self.exit_button, alignment=Qt.AlignLeft)

        header = QVBoxLayout()
        header.setSpacing(0)
        header.setContentsMargins(36, 64, 64, 126)
        header.addWidget(title_text, alignment=Qt.AlignLeft)
        header.addWidget(description, alignment=Qt.AlignLeft)

        main_layout = QVBoxLayout()
        main_layout.addLayout(header)
        main_layout.addLayout(buttons_layout)
        main_layout.addStretch(0)

        self.setLayout(main_layout)

    def apply_style(self, object, style):
        object.setStyleSheet(style)
        if isinstance(object, QPushButton): ## This is very useful! it checks if an object is certain class! 
            object.setFixedSize(240, 52)

    def event_handler(self):
        pass
        #self.start_button.clicked.connect(self.start_button_clicked)

print("Starting Marugoto A2-1...")
run()

import sys
import ctypes
from PyQt5.QtWidgets import (
            QApplication, QWidget, QSystemTrayIcon, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, 
            QStackedLayout, QFrame
            )
from PyQt5.QtCore import Qt, QCoreApplication, pyqtSignal
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtMultimedia import QSound
from pyautogui import size
import json
from default_stylesheet import *
from time import sleep
# from conjugation_v import *

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

class QHoveredButton(QPushButton):
    '''
        This is a button type exclusively made to have special effects
        when a button is being hovered, it tracks a signal
        this allows you to, by example, hover a button and get a changing description
    '''

    hovered = pyqtSignal()
    unhovered = pyqtSignal()

    def enterEvent(self, event):
        self.hovered.emit()
        super().enterEvent(event)

    def leaveEvent(self, event):
        self.unhovered.emit()
        super().leaveEvent(event)


class MainWindow(QWidget):
    def __init__(self, parent=None, flags=Qt.WindowFlags()):
        super().__init__(parent=parent, flags=flags)

        self.is_light_mode = True
        self.notifier = QSystemTrayIcon(self)

        self.settings_file = "data/local/config.json"
        with open(self.settings_file, 'r', encoding='utf-8') as archivo:
            settings = json.load(archivo)
        
        self.language = settings.get("language", "en")
        self.is_light_mode = settings.get("is_light_mode", True)

        self.main_layout = QVBoxLayout()
        self.stacked_layout = QStackedLayout()
        self.main_layout.addLayout(self.stacked_layout)
        self.setLayout(self.main_layout)

        self.set_language()
        self.set_window()
        titles_style, text_style, button_style, ss_btn_style, frame_style = get_stylesheet(self.is_light_mode)
        self.titles_list = list()
        self.buttons_list = list()
        self.ss_btn_list = list()
        self.texts_list = list()
        self.frames_list = list()
        self.main_menu() ## INDEX 0
        self.settings_menu() ## INDEX 1
        self.event_handler()

        print("Applying styles...")
        self.apply_style(self.titles_list, titles_style)
        self.apply_style(self.buttons_list, button_style)
        self.apply_style(self.ss_btn_list, ss_btn_style, 1)
        self.apply_style(self.texts_list, text_style)
        self.apply_style(self.frames_list, frame_style)
        print("Styles applied successfully")

        self.notifier.show()    

        self.stacked_layout.setCurrentIndex(0)
        print("Starting Marugoto A2-1...")
        self.show()

    def set_window(self):
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

        ## MAIN MENU
        self.title_tt = language["text"]["title"]
        self.description_txt = language["text"]["description"]
        self.lessons_btn = language["button"]["lessons"]
        self.dict_btn = language["button"]["dictionary"]
        self.settings_btn = language["button"]["settings"]
        self.about_btn = language["button"]["about"]
        self.exit_btn = language["button"]["exit"]
        self.help_btn = language["button"]["help"]

        ## SETTINGS PAGE
        self.settings_tt = language["text"]["title_settings"]
        self.return_btn = language["button"]["back"]
        self.temporizer_btn = language["button"]["temporizer_SRS"]
        self.light_mode_btn = language["button"]["light_mode"]
        self.dark_mode_btn = language["button"]["dark_mode"]
        self.language_btn = language["button"]["language"]
        self.save_btn = language["button"]["save"]

        self.config_desc_txt = language["text"]["config_desc"]
        self.temporizer_txt = language["text"]["temporizer_SRS"]
        self.light_mode_txt = language["text"]["light_mode"]
        self.dark_mode_txt = language["text"]["dark_mode"]
        self.language_txt = language["text"]["language"]
        self.save_txt = language["text"]["save"]

        print("Language set to:", self.language, "loaded properly")

    def set_images(self):
        pass

    def set_sound(self):
        self.clicked_button = QSound()

    def main_menu(self):
        self.main_page = QWidget() 

        title_app = QLabel(self.title_tt)
        description = QLabel(self.description_txt)
        self.lessons_button = QPushButton(self.lessons_btn)
        self.dictionary_button = QPushButton(self.dict_btn)
        self.settings_button = QPushButton(self.settings_btn)
        self.about_button = QPushButton(self.about_btn)
        self.help_button = QPushButton(self.help_btn)
        self.exit_button = QPushButton(self.exit_btn)

        self.titles_list.append(title_app)

        self.texts_list.append(description)

        self.buttons_list.append(self.lessons_button)
        self.buttons_list.append(self.dictionary_button)
        self.buttons_list.append(self.help_button)
        self.buttons_list.append(self.exit_button)

        self.ss_btn_list.append(self.settings_button)
        self.ss_btn_list.append(self.about_button)

        buttons_layout = QVBoxLayout()
        buttons_layout.setSpacing(32)
        buttons_layout.setContentsMargins(32, 0, 0, 0)
        buttons_layout.addWidget(self.lessons_button, alignment=Qt.AlignLeft)
        buttons_layout.addWidget(self.dictionary_button, alignment=Qt.AlignLeft)
        buttons_layout.addWidget(self.help_button, alignment=Qt.AlignLeft)
        buttons_layout.addWidget(self.exit_button, alignment=Qt.AlignLeft)

        small_btn_layout = QVBoxLayout()
        small_btn_layout.addSpacing(16)
        small_btn_layout.addWidget(self.settings_button, alignment=Qt.AlignRight)
        small_btn_layout.setSpacing(12)
        small_btn_layout.addWidget(self.about_button, alignment=Qt.AlignRight)
        small_btn_layout.addStretch(0)

        title_layout = QVBoxLayout()
        title_layout.addSpacing(116)
        title_layout.addWidget(title_app, alignment=Qt.AlignLeft)
        title_layout.addWidget(description, alignment=Qt.AlignLeft)
        title_layout.setSpacing(8)

        header = QHBoxLayout()
        header.setContentsMargins(36, 24, 36, 64)
        header.addLayout(title_layout)
        header.addLayout(small_btn_layout)

        main_menu = QVBoxLayout(self.main_page)
        main_menu.addLayout(header)
        main_menu.addLayout(buttons_layout)
        main_menu.addStretch(0)

        self.stacked_layout.addWidget(self.main_page)

        print("Main Menu loaded properly")

    def settings_menu(self):
        self.settings_page = QWidget()
        
        title = QLabel(self.settings_tt)
        self.back_to_menu = QPushButton(self.return_btn)
        settings_icon = QLabel(self)
        settings_img = QPixmap("data/local/images/config.png")
        scaled_img = settings_img.scaled(128, 128, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        settings_icon.setPixmap(scaled_img)

        self.titles_list.append(title)
        self.ss_btn_list.append(self.back_to_menu)

        header = QHBoxLayout()
        header.addSpacing(128)
        header.addWidget(settings_icon, alignment=Qt.AlignCenter)
        header.addWidget(self.back_to_menu, alignment=Qt.AlignRight)
        header.addWidget(title, alignment=Qt.AlignCenter)
        header.addSpacing(64)
        header.setSpacing(16)

        settings_body = QWidget()
        self.settings_stacked = QStackedLayout()

        self.set_temporizer = QHoveredButton(self.temporizer_btn)
        self.set_light_mode = QHoveredButton(self.light_mode_btn)
        self.set_dark_mode = QHoveredButton(self.dark_mode_btn)
        self.set_app_language = QHoveredButton(self.language_btn)
        self.save_config = QHoveredButton(self.save_btn)

        self.buttons_list.append(self.set_temporizer)
        self.buttons_list.append(self.set_light_mode)
        self.buttons_list.append(self.set_dark_mode)
        self.buttons_list.append(self.set_app_language)
        self.buttons_list.append(self.save_config)

        self.config_desc = QLabel(self.config_desc_txt)
        self.temporizer_desc = QLabel(self.temporizer_txt)
        self.light_mode_desc = QLabel(self.light_mode_txt)
        self.dark_mode_desc = QLabel(self.dark_mode_txt)
        self.language_desc = QLabel(self.language_txt)
        self.language_desc.setWordWrap(True)
        self.language_desc.setMinimumWidth(640)
        self.save_desc = QLabel(self.save_txt)

        self.texts_list.append(self.config_desc)
        self.texts_list.append(self.temporizer_desc)
        self.texts_list.append(self.light_mode_desc)
        self.texts_list.append(self.dark_mode_desc)
        self.texts_list.append(self.language_desc)
        self.texts_list.append(self.save_desc)

        self.temporizer_desc.hide()
        self.light_mode_desc.hide()
        self.dark_mode_desc.hide()
        self.language_desc.hide()
        self.save_desc.hide()

        options = QVBoxLayout()
        options.addSpacing(64)
        options.setSpacing(32)
        options.addWidget(self.set_temporizer, alignment=Qt.AlignCenter)
        options.addWidget(self.set_light_mode, alignment=Qt.AlignCenter)
        options.addWidget(self.set_dark_mode, alignment=Qt.AlignCenter)
        options.addWidget(self.set_app_language, alignment=Qt.AlignCenter)
        options.addWidget(self.save_config, alignment=Qt.AlignCenter)

        descriptions = QVBoxLayout()
        descriptions.setSpacing(64)
        descriptions.addSpacing(32)
        descriptions.addWidget(self.config_desc, alignment= Qt.AlignCenter)
        descriptions.addWidget(self.temporizer_desc, alignment=Qt.AlignCenter)
        descriptions.addWidget(self.light_mode_desc, alignment=Qt.AlignCenter)
        descriptions.addWidget(self.dark_mode_desc, alignment=Qt.AlignCenter)
        descriptions.addWidget(self.language_desc, alignment=Qt.AlignCenter)
        descriptions.addWidget(self.save_desc, alignment=Qt.AlignCenter)
        descriptions.addStretch(1) 

        body = QHBoxLayout(settings_body)
        body.addLayout(descriptions)
        body.addLayout(options)

        separator = QFrame()
        separator.setFrameShape(QFrame.HLine)
        separator.setFrameShadow(QFrame.Plain)

        self.frames_list.append(separator)

        settings_menu = QVBoxLayout(self.settings_page)
        settings_menu.addLayout(header, stretch=1)
        settings_menu.addWidget(separator)
        settings_menu.addWidget(settings_body, stretch=1)
        self.stacked_layout.addWidget(self.settings_page)

        print("Settings Menu loaded properly")

    def apply_style(self, object, style, small=0):
        print("Current objects in list: ", len(object))
        for i in range(len(object)):
            object[i].setStyleSheet(style)
            if isinstance(object[i], QPushButton) or isinstance(object[i], QHoveredButton): ## This is very useful! it checks if an object is certain class! 
                if not small:
                    object[i].setFixedSize(240, 52)
                else:
                    object[i].setFixedSize(52, 52)

        print("Applied styles to: ", object)

    def change_page(self, index):

        sleep(0.25)
        self.stacked_layout.setCurrentIndex(index)

    def event_handler(self):
        self.exit_button.clicked.connect(lambda: QCoreApplication.quit())
        self.settings_button.clicked.connect(lambda: self.change_page(1))
        self.back_to_menu.clicked.connect(lambda: self.change_page(0))

        ## HOVER
        ## Keep in mind for further optimization of method
        self.set_temporizer.hovered.connect(self.temporizer_desc.show)
        self.set_light_mode.hovered.connect(self.light_mode_desc.show)
        self.set_dark_mode.hovered.connect(self.dark_mode_desc.show)
        self.set_app_language.hovered.connect(self.language_desc.show)
        self.save_config.hovered.connect(self.save_desc.show)

        self.set_temporizer.unhovered.connect(self.temporizer_desc.hide)
        self.set_light_mode.unhovered.connect(self.light_mode_desc.hide)
        self.set_dark_mode.unhovered.connect(self.dark_mode_desc.hide)
        self.set_app_language.unhovered.connect(self.language_desc.hide)
        self.save_config.unhovered.connect(self.save_desc.hide)

        print("Event Handler loaded Properly")

run()

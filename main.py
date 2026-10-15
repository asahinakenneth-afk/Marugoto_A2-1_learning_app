import sys
import ctypes
from PyQt5.QtWidgets import (
            QApplication, QWidget, QSystemTrayIcon, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, 
            QStackedLayout, QFrame
            )
from PyQt5.QtCore import Qt, QCoreApplication, pyqtSignal, QTimer, QUrl
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtMultimedia import QSoundEffect
from pyautogui import size
import json
from default_stylesheet import *

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
    #region HOVERBUTTON CLASS
    '''
        This is a button type exclusively made to have special effects
        when a button is being hovered, it tracks a signal
        this allows you to, by example, hover a button and get a changing description
    '''
    hovered = pyqtSignal()
    unhovered = pyqtSignal()

    def __init__(self, text="", parent=None):
        super().__init__(text, parent)
        self.sfx = QSoundEffect(self)
        self.sfx.setSource(QUrl.fromLocalFile("data/local/sfx/hover_button.wav"))

    def enterEvent(self, event):
            self.hovered.emit()
            self.sfx.play()
            super().enterEvent(event)

    def leaveEvent(self, event):
            self.unhovered.emit()
            super().leaveEvent(event)
    #endregion

class MainWindow(QWidget):
    def __init__(self, parent=None, flags=Qt.WindowFlags()):
        super().__init__(parent=parent, flags=flags)

    #region EXEC APP
        self.setObjectName("mainWindow")
        self.is_light_mode = True
        # self.notifier = QSystemTrayIcon(self)

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
        self.set_sound()
        self.main_menu() ## INDEX 0
        self.settings_menu() ## INDEX 1
        self.event_handler()

        print("Applying styles...")
        stylesheet = get_stylesheet(self.is_light_mode)
        self.setStyleSheet(stylesheet)
        print("Styles applied successfully")

        # self.notifier.show()    

        self.stacked_layout.setCurrentIndex(0)
    #endregion
        print("Starting Marugoto A2-1...")

        QTimer.singleShot(1000, lambda: self.show())

    def set_window(self):
        main_icon = QIcon("data/local/images/logo.ico")
        # self.notifier.setToolTip("Marugoto A2-1")
        self.setWindowTitle(self.title_tt)
        self.setGeometry(0, 0, WIDTH, HEIGHT)
        self.setWindowIcon(main_icon)
        # self.notifier.setIcon(main_icon)

    def set_sound(self):
        self.clicked_button = QSoundEffect(self)
        self.clicked_button.setSource(QUrl.fromLocalFile("data/local/sfx/click_button.wav"))

    def set_language(self):
        language_file = f"data/local/languages/{self.language}.json"
        
        # Open and load the JSON file for the language here
        with open(language_file, 'r', encoding='utf-8') as archivo:
            language = json.load(archivo)
        
        # then you set variables for the text you want to use in the GUI! completely dynamic :3

    #region MAIN MENU
        self.title_tt = language["text"]["title"]
        self.description_txt = language["text"]["description"]
        self.lessons_btn = language["button"]["lessons"]
        self.dict_btn = language["button"]["dictionary"]
        self.settings_btn = language["button"]["settings"]
        self.about_btn = language["button"]["about"]
        self.exit_btn = language["button"]["exit"]
        self.help_btn = language["button"]["help"]
    #endregion

    #region SETTINGS PAGE
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

        #region TEMPORIZER SETTINGS
        self.temporizer_tt = language["text"]["title_temporizer"]
        self.temporizer_unavailable_txt = language["text"]["temporizer_coming_soon"]
        #endregion

        #region LANGUAGE SETTINGS
        self.language_tt = language["text"]["title_language"]
        self.language_en_btn = language["button"]["set_english"]
        self.language_es_btn = language["button"]["set_spanish"]
        #endregion
    #endregion

        print("Language set to:", self.language, "loaded properly")

    def set_images(self):
        pass

    def set_sound(self):
        self.clicked_button = QSoundEffect()
        self.clicked_button.setSource(QUrl.fromLocalFile("data/local/sfx/click_button.wav"))

        print("sound set successfully")

    def main_menu(self):
        self.main_page = QWidget() 

    #region WIDGETS
        title_app = QLabel(self.title_tt)
        title_app.setObjectName("title")
        description = QLabel(self.description_txt)
        icon = QLabel()
        pixmap = QPixmap("data/local/images/logo.png")
        scaled_pixmap = pixmap.scaled(128, 128, Qt.KeepAspectRatio,Qt.SmoothTransformation)
        icon.setPixmap(scaled_pixmap)
    
        self.lessons_button = QPushButton(self.lessons_btn)
        self.dictionary_button = QPushButton(self.dict_btn)
        self.help_button = QPushButton(self.help_btn)
        self.exit_button = QPushButton(self.exit_btn)

        self.settings_button = QPushButton(self.settings_btn)
        self.settings_button.setObjectName("small")
        self.about_button = QPushButton(self.about_btn)
        self.about_button.setObjectName("small")
    #endregion

    #region LAYOUTS
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

        icon_layout = QHBoxLayout()
        icon_layout.addWidget(icon, alignment=Qt.AlignBottom)
        icon_layout.setSpacing(0)

        title_layout = QVBoxLayout()
        title_layout.addSpacing(116)
        title_layout.addWidget(title_app, alignment=Qt.AlignLeft)
        title_layout.addWidget(description, alignment=Qt.AlignLeft)
        title_layout.setSpacing(8)

        header = QHBoxLayout()
        header.setContentsMargins(36, 24, 36, 64)
        header.addLayout(icon_layout, stretch=0)
        header.addSpacing(32)
        header.addLayout(title_layout, stretch=1)
        header.addLayout(small_btn_layout)

        main_menu = QVBoxLayout(self.main_page)
        main_menu.addLayout(header)
        main_menu.addLayout(buttons_layout)
        main_menu.addStretch(0)
    #endregion

        self.stacked_layout.addWidget(self.main_page)

        print("Main Menu loaded properly")

    def settings_menu(self):
        self.settings_page = QWidget()

        title = QLabel(self.settings_tt)
        title.setObjectName("title")
        self.back_to_menu = QPushButton(self.return_btn)
        self.back_to_menu.setObjectName("small")
        settings_icon = QLabel(self)
        settings_img = QPixmap("data/local/images/config.png")
        scaled_img = settings_img.scaled(480, 128, Qt.IgnoreAspectRatio,Qt.SmoothTransformation)
        settings_icon.setPixmap(scaled_img)

        header = QHBoxLayout()
        header.addSpacing(32)
        header.addWidget(settings_icon, alignment=Qt.AlignCenter)
        header.addSpacing(16)
        header.addWidget(self.back_to_menu, alignment=Qt.AlignRight)
        header.addWidget(title, alignment=Qt.AlignCenter)
        header.addSpacing(64)
        header.setSpacing(16)

    #region SETTINGS LIST INDEX 0
        settings_body = QWidget()
        self.stacked_settings = QStackedLayout()
        self.stacked_settings.addWidget(settings_body)

        self.set_temporizer = QHoveredButton(self.temporizer_btn)
        self.set_light_mode = QHoveredButton(self.light_mode_btn)
        self.set_dark_mode = QHoveredButton(self.dark_mode_btn)
        self.set_app_language = QHoveredButton(self.language_btn)
        self.save_config = QHoveredButton(self.save_btn)

        self.config_desc = QLabel(self.config_desc_txt)
        self.temporizer_desc = QLabel(self.temporizer_txt)
        self.temporizer_desc.setWordWrap(True)
        self.temporizer_desc.setMinimumWidth(640)
        self.light_mode_desc = QLabel(self.light_mode_txt)
        self.dark_mode_desc = QLabel(self.dark_mode_txt)
        self.language_desc = QLabel(self.language_txt)
        self.language_desc.setWordWrap(True)
        self.language_desc.setMinimumWidth(640)
        self.save_desc = QLabel(self.save_txt)

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
    #endregion

    #region TEMPORIZER PAGE INDEX 1
        temporizer_page = QWidget()
        temporizer_layout = QVBoxLayout(temporizer_page)
        self.stacked_settings.addWidget(temporizer_page)

        temporizer_title = QLabel(self.temporizer_tt)
        temporizer_title.setObjectName("title")
        self.return_to_settings = QPushButton(self.return_btn)
        self.return_to_settings.setObjectName("small")

        temporizer_header = QHBoxLayout()
        temporizer_header.setSpacing(0)
        temporizer_header.addSpacing(8)
        temporizer_header.addWidget(self.return_to_settings, alignment=Qt.AlignLeft)
        temporizer_header.addSpacing(16)
        temporizer_header.addWidget(temporizer_title, stretch=1, alignment=Qt.AlignLeft)
        
        temporizer_note = QLabel(self.temporizer_unavailable_txt)
        temporizer_note.setWordWrap(True)
        temporizer_note.setMinimumWidth(768)

        temporizer_body = QVBoxLayout()
        temporizer_body.addWidget(temporizer_note, alignment=Qt.AlignCenter) ## COMING SOON

        temporizer_layout.addLayout(temporizer_header)
        temporizer_layout.addLayout(temporizer_body, stretch=2)
        #endregion

    #region LANGUAGE PAGE INDEX 2
        language_page = QWidget()
        language_layout = QVBoxLayout(language_page)
        self.stacked_settings.addWidget(language_page)

        self.language_title = QLabel(self.language_tt)

        language_header = QHBoxLayout()
        language_header.setSpacing(0)
        language_header.addSpacing(8)
        language_header.addWidget(self.language_title, stretch=1, alignment=Qt.AlignLeft)

        self.english_button = QPushButton(self.language_en_btn)
        self.spanish_button = QPushButton(self.language_es_btn)

        language_body = QVBoxLayout()
        language_body.addWidget(self.english_button, alignment=Qt.AlignCenter)
        language_body.addWidget(self.spanish_button, alignment=Qt.AlignCenter)

        language_layout.addLayout(language_header)
        language_layout.addLayout(language_body, stretch=1)
        #endregion

        body = QHBoxLayout(settings_body)
        body.addLayout(descriptions)
        body.addLayout(options)

        separator = QFrame()
        separator.setObjectName("separator")
        separator.setFrameShape(QFrame.HLine)
        separator.setFrameShadow(QFrame.Plain)

        settings_menu = QVBoxLayout(self.settings_page)
        settings_menu.addLayout(header, stretch=1)
        settings_menu.addWidget(separator)
        settings_menu.addLayout(self.stacked_settings, stretch=2)

        self.stacked_layout.addWidget(self.settings_page)

        self.stacked_settings.setCurrentIndex(0)
        print("Settings Menu loaded properly")

    def change_page(self, stacked_layout, index):
        self.clicked_button.play()
        if stacked_layout == self.stacked_layout and index == 0:
            QTimer.singleShot(450, lambda: self.stacked_settings.setCurrentIndex(0))
        QTimer.singleShot(250, lambda: stacked_layout.setCurrentIndex(index))

    def event_handler(self):
        self.exit_button.clicked.connect(lambda: QCoreApplication.quit())
        self.settings_button.clicked.connect(lambda: self.change_page(self.stacked_layout, 1))
        self.back_to_menu.clicked.connect(lambda: self.change_page(self.stacked_layout, 0))

        self.set_temporizer.clicked.connect(lambda: self.change_page(self.stacked_settings, 1))
        self.set_app_language.clicked.connect(lambda: self.change_page(self.stacked_settings, 2))
        self.return_to_settings.clicked.connect(lambda: self.change_page(self.stacked_settings, 0))

    #region HOVER
        ## Keep in mind for further optimization
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
    #endregion

        print("Event Handler loaded Properly")

run()

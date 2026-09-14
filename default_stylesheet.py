from PyQt5.QtGui import QFontDatabase

def get_stylesheet(is_light_mode):
    ## Bro I need to have a GUI running, if not, QFontDatabase will crash the program

    ## Okay I've made my research and the problem was about my procedure HAAHAHAA
    text_id = QFontDatabase.addApplicationFont("data/local/fonts/April.ttf")
    titles_id = QFontDatabase.addApplicationFont("data/local/fonts/SuperWarming.ttf")
    buttons_id = QFontDatabase.addApplicationFont("data/local/fonts/DueMining.otf")
    TEXT_FONT = QFontDatabase.applicationFontFamilies(text_id)[0] if text_id != -1 else "Arial"
    TITLES_FONT = QFontDatabase.applicationFontFamilies(titles_id)[0] if titles_id != -1 else "Arial"
    BUTTON_FONT = QFontDatabase.applicationFontFamilies(buttons_id)[0] if buttons_id != -1 else "Arial"

    print("Fonts loaded properly:", TEXT_FONT, TITLES_FONT, BUTTON_FONT)

    if is_light_mode:
        titles_style = f"""color: rgb{TITLES_COLOR_LIGHT}; font-size: 52px; font-family: "{TITLES_FONT}" """

        text_style = f"""color: rgb{TEXT_COLOR_LIGHT}; font-size: 20px; font-family: "{TEXT_FONT}" """

        button_style = f"""
                QPushButton {{
        background-color: rgb{BUTTON_LIGHT};
        color: rgb{TEXT_COLOR_LIGHT};
        font-family: "{BUTTON_FONT}";
        font-size: 32px;
        border-radius: 20px;
        border-style: dotted;
        border-width: 4px;
        border-color: #F26B87;
                    }}
                QPushButton:hover {{
        background-color: rgb{BUTTON_HOVER_LIGHT};
        border-color: #F05143;
                    }}
                QPushButton:pressed {{
        background-color: rgb{BUTTON_PRESSED_LIGHT};
        border-color: #FF857D;
                    }}
                """

    print("Stylesheet loaded successfully.")
    return titles_style, text_style, button_style

WINDOW_LIGHT = (255, 192, 184)
WINDOW_DARK = (22, 6, 3)

BUTTON_LIGHT = (255, 143, 168)
BUTTON_HOVER_LIGHT = (255, 120, 110)
BUTTON_PRESSED_LIGHT = (255, 100, 90)

TEXT_COLOR_LIGHT = (0, 0, 0)

TITLES_COLOR_LIGHT = (0, 0, 0)

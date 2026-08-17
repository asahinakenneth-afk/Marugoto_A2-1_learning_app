from PyQt5.QtGui import QFontDatabase

def get_stylesheet(is_light_mode):
    ## Bro I need to have a GUI running, if not, QFontDatabase will crash the program

    ## Okay I've made my research and the problem was about my procedure HAAHAHAA
    text_id = QFontDatabase.addApplicationFont("data/local/fonts/April.ttf")
    titles_id = QFontDatabase.addApplicationFont("data/local/fonts/SuperWarming.ttf")
    TEXT_FONT = QFontDatabase.applicationFontFamilies(text_id)[0] if text_id != -1 else "Arial"
    TITLES_FONT = QFontDatabase.applicationFontFamilies(titles_id)[0] if titles_id != -1 else "Arial"
    print("Fonts loaded properly:", TEXT_FONT, TITLES_FONT)

    if is_light_mode:
        titles_style = f"""color: rgb{TITLES_COLOR_LIGHT}; font-size: 52px; font-family: "{TITLES_FONT}" """

        text_style = f"""color: rgb{TEXT_COLOR_LIGHT}; font-size: 20px; font-family: "{TEXT_FONT}" """

        button_style = f"""
                QPushButton {{
        background-color: rgb{BUTTON_LIGHT};
        color: rgb{TEXT_COLOR_LIGHT};
        font-family: "{BUTTON_FONT}";
        font-size: 32px;
        font-weight: bold;
        border-style: solid;
        border: 4px solid #000000;
        border-top: 4px solid #ffffff;
        border-left: 4px solid #ffffff;
        border-bottom: 4px solid #FF7898;
        border-right: 4px solid #FF7898;
                    }}
                QPushButton:hover {{
        background-color: rgb{BUTTON_HOVER_LIGHT};
                    }}
                QPushButton:pressed {{
        border-top: 4px solid #FF7898;
        border-left: 4px solid #FF7898;
        border-bottom: 4px solid #ffffff;
        border-right: 4px solid #ffffff;
                    }}
                """

    print("Stylesheet loaded successfully.")
    return titles_style, text_style, button_style

WINDOW_LIGHT = (255, 192, 184)
WINDOW_DARK = (22, 6, 3)

BUTTON_LIGHT = (255, 143, 168)
BUTTON_HOVER_LIGHT = (255, 120, 110)
BUTTON_FONT = ""

TEXT_COLOR_LIGHT = (0, 0, 0)

TITLES_COLOR_LIGHT = (0, 0, 0)

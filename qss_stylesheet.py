WINDOW_LIGHT = (255, 192, 184)
WINDOW_DARK = (22, 6, 3)

BUTTON_LIGHT = (255, 143, 168)
BUTTON_HOVER_LIGHT = (255, 120, 110)
BUTTON_FONT = ""

TEXT_COLOR_LIGHT = (0, 0, 0)
TEXT_FONT = "data/local/fonts/April.ttf"

BUTTON_STYLE_LIGHT = f"""
    QPushButton {{
        background-color: rgb{BUTTON_LIGHT};
        color: rgb{TEXT_COLOR_LIGHT};
        font-family: '{BUTTON_FONT}';
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
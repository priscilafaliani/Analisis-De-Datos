import PySimpleGUI as sg
import os.path

# ------ COLOR PALETTE ------

BACKGROUND = '#ecf0f1',
LIGHT_GREY = '#34495e'
DARK_GREY = '#2c3e50'
ORANGE = '#e67e22'
WHITE = '#FFFFFF'
BLACK = '#000000'

# -------- FONTS --------

MAIN_WINDOW_TITLE_FONT = ('times', 30)
MAIN_WINDOW_SUBTITLE_FONT = ('courier', 15, 'bold')

# -------- ICONS --------

ICONS_PATH = os.path.join('resources', 'icons')

EXIT_BUTTON_ICON = os.path.join(ICONS_PATH, 'exit')
ELI5_ICON = os.path.join(ICONS_PATH, 'eli5.png')
LTP_ICON = os.path.join(ICONS_PATH, 'lpt.png')

# ------ TEXT ------

MAIN_WINDOW_TITLE = 'ANÁLISIS DE DATOS'
MAIN_WINDOW_SUBTITLE = 'SELECCIONE UN SET DE DATOS'

CARD_BUTTON_TEXT = 'LEER MÁS'


# ------ EXPLAIN LIKE I'M FIVE ------
ELI5_KEY = '-ELI5-'

ELI5_CARD_TITLE = 'EXPLAIN LIKE I\'M FIVE'
ELI5_CARD_SUBTITLE = 'EXPLICACIONES DE TEMAS COMPLETOS\nHECHOS FÁCIL'


# ------- LIFE PRO TIPS ------
LPT_KEY = '-LPT-'

LPT_CARD_TITLE = 'LIFE PRO TIPS'
LPT_CARD_SUBTITLE = 'ACCIONES ESPECÍFICAS QUE PUEDEN\nMEJORAR NUESTRA VIDA'

# ------ GLOBAL ------

sg.set_options(
    auto_size_buttons=False,
    background_color=BACKGROUND,
    element_padding=(0, 0),
    margins=(0, 0)
)
import PySimpleGUI as sg
import os.path

# ------ COLOR PALETTE ------

BACKGROUND = '#ecf0f1',
LIGHT_GRAY = '#34495e'
DARK_GRAY = '#2c3e50'
ORANGE = '#e67e22'
VIOLET = '#9b59b6'
WHITE = '#FFFFFF'
BLACK = '#000000'

# -------- FONTS --------



# -------- ICONS --------

ICONS_PATH = os.path.join('resources', 'icons')

EXIT_BUTTON_ICON = os.path.join(ICONS_PATH, 'exit.png')
TIL_ICON = os.path.join(ICONS_PATH, 'til.png')
LTP_ICON = os.path.join(ICONS_PATH, 'lpt.png')
POPUP_ICON = os.path.join(ICONS_PATH, 'chart.png')

# ------ TEXT ------

MAIN_WINDOW_TITLE = 'ANÁLISIS DE DATOS'
MAIN_WINDOW_SUBTITLE = 'SELECCIONE UN SET DE DATOS'

CARD_BUTTON_TEXT = 'LEER MÁS'

POPUP_BUTTON1_TEXT = 'ANALIZAR'
POPUP_BUTTON2_TEXT = 'VOLVER ATRÁS'

# ------ DATASETS ------

DATASETS_PATH = os.path.join('resources', 'datasets')

TIL_PATH = os.path.join(DATASETS_PATH, 'todayilearned.csv')
LPT_PATH = os.path.join(DATASETS_PATH, 'LifeProTips.csv')

# ------ EXPLAIN LIKE I'M FIVE ------

TIL_KEY = '-TIL-'

TIL_CARD_TITLE = 'TODAY I LEARNED'
TIL_CARD_SUBTITLE = 'APRENDEMOS ALGO NUEVO TODOS LOS DÍAS\n¿QUÉ APRENDISTE HOY?'

TIL_CONTENT = '¿Qué hechos interesantes aprendió la gente?\nNos puede sorprender también'

# ------- LIFE PRO TIPS ------

LPT_KEY = '-LPT-'

LPT_CARD_TITLE = 'LIFE PRO TIPS'
LPT_CARD_SUBTITLE = 'TIPS QUE MEJORAN TU VIDA DE\nUNA FORMA U OTRA'

LPT_CONTENT = 'Un \'Life Pro Tip\' es una acción específica\nque da resultados definitivos.\n\n¿De qué manera podemos mejorar nuestra vida?'

# ------ FOR FUNCTIONS ------

# used in components/menu when opening a popup
POPUP_PARAMETERS = {
    '-TIL-': [TIL_CARD_TITLE, TIL_CARD_SUBTITLE, TIL_CONTENT],
    '-LPT-': [LPT_CARD_TITLE, LPT_CARD_SUBTITLE, LPT_CONTENT]
}

# ------- EVENTS -------

EXIT_EVENT = '-EXIT-'
ANALYSE_EVENT = '-ANALIZAR-'
RETURN_EVENT = '-VOLVER ATRÁS-'

# ------ GLOBAL ------

sg.set_options(
    auto_size_buttons=False,
    background_color=BACKGROUND,
    element_padding=(0, 0),
    margins=(0, 0),
    font='helvetica'
)
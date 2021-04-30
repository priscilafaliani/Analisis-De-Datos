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

REDDIT_ICON = os.path.join(ICONS_PATH, 'reddit.png')
ST_ICON = os.path.join(ICONS_PATH, 'ST.png')
LTP_ICON = os.path.join(ICONS_PATH, 'lpt.png')
MUSEUM_ICON = os.path.join(ICONS_PATH, 'museum.png')

POPUP_ICON = os.path.join(ICONS_PATH, 'chart.png')

# ------ TEXT ------

MAIN_WINDOW_TITLE = 'ANÁLISIS DE DATOS'
MAIN_WINDOW_SUBTITLE = 'SELECCIONE UN SET DE DATOS'

CARD_BUTTON_TEXT = 'LEER MÁS'

POPUP_BUTTON1_TEXT = 'ANALIZAR'
POPUP_BUTTON1_TEXT2 = 'VER MÁS'
POPUP_BUTTON2_TEXT = 'VOLVER ATRÁS'


# ------ DATASETS ------

DATASETS_PATH = os.path.join('resources', 'datasets')

ST_PATH = os.path.join(DATASETS_PATH, 'reddit', 'Showertoughts.csv')
LPT_PATH = os.path.join(DATASETS_PATH, 'reddit', 'LifeProTips.csv')
RIJKS_PATH = os.path.join(DATASETS_PATH, 'rijksmuseum', 'rijksmuseum.csv')

# ------ REDDIT ------

REDDIT_KEY = '-R-'

REDDIT_CARD_TITLE = 'REDDIT'
REDDIT_CARD_SUBTITLE = 'UNA RED DE COMUNIDADES, BASADA\nEN LOS INTERESES DE LA GENTE'

REDDIT_CONTENT = 'Existen distintos \'subreddits\', cada uno respecto a diferentes temas\n\n¿Qué despierta más su curiosidad?'

# ------ SHOWERTHOUGHTS ------

ST_KEY = '-ST-'

ST_CARD_TITLE = 'SHOWERTHOUGHTS'
ST_CARD_SUBTITLE = 'PEQUEÑAS EPIFANÍAS QUE RESALTAN\nRAREZAS DENTRO DE LO CONOCIDO'

ST_CONTENT = 'Un \'showerthought\' es un término para referirse a los pensamientos\nque aparecen cuando hacemos cosas rutinarias\n\nSon interesantes y nos pueden hacer sentir\nidentificados.'

# ------- LIFE PRO TIPS ------

LPT_KEY = '-LPT-'

LPT_CARD_TITLE = 'LIFE PRO TIPS'
LPT_CARD_SUBTITLE = 'TIPS QUE MEJORAN TU VIDA DE\nUNA FORMA U OTRA'

LPT_CONTENT = 'Un \'Life Pro Tip\' es una acción específica\nque da resultados definitivos.\n\n¿De qué manera podemos mejorar nuestra vida?'

# ------ RIJKSMUSEUM ------

MUSEUM_KEY = '-RIJKS-'

MUSEUM_CARD_TILTE = 'RIJKSMUSEUM'
MUSEUM_CARD_SUBTITLE = 'UN MUSEO DEDICADO A EL ARTE\nY LA HISTORIA EN AMSTERDAN'

MUSEUM_CONTENT = 'El museo conserva, investiga, colecciona, \npresenta... material histórico y artístico\n\n¿Cuáles son sus obras más antiguas?'

# ------ FOR FUNCTIONS ------

# used in handlers/popups when handling a popup
POPUP_PARAMETERS = {
    REDDIT_KEY: [REDDIT_KEY, REDDIT_CARD_TITLE, REDDIT_CARD_SUBTITLE, REDDIT_CONTENT, ST_CARD_TITLE, LPT_CARD_TITLE],
    ST_KEY: [ST_KEY, ST_CARD_TITLE, ST_CARD_SUBTITLE, ST_CONTENT],
    LPT_KEY: [LPT_KEY, LPT_CARD_TITLE, LPT_CARD_SUBTITLE, LPT_CONTENT],
    MUSEUM_KEY: [MUSEUM_KEY, MUSEUM_CARD_TILTE, MUSEUM_CARD_SUBTITLE, MUSEUM_CONTENT]
}

# used in handlers/popups to decode values returned by the combobox.
# they're only needed when the selected card was 'reddit'
TEXT_TO_KEY = {
    ST_CARD_TITLE: ST_KEY,
    LPT_CARD_TITLE: LPT_KEY
}

# used in handlers/analysis to call the correct analysis method
from src.handlers import reddit, museum

ANALYSIS_FUNCTIONS = {
    ST_KEY: (reddit.analyse, ST_PATH),
    LPT_KEY: (reddit.analyse, LPT_PATH),
    MUSEUM_KEY: (museum.analyse, RIJKS_PATH)
}

# ------- EVENTS -------

EXIT_EVENT = '-EXIT-'
SEE_MORE_EVENT = '-VER MÁS-'
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
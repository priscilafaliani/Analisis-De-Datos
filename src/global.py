import PySimpleGUI as sg


# ------ COLOR PALETTE ------

BACKGROUND = '#ecf0f1',
LIGHT_GREY = '#34495e'
DARK_GREY = '#2c3e50'
ORANGE = '#e67e22'
WHITE = '#FFFFFF'
BLACK = '#000000'

# -------- FONTS --------


# -------- ICONS --------

ICONS_PATH = os.path.join('resources', 'icons')


sg.set_options(
    auto_size_buttons=False,
    background_color=BACKGROUND,
    element_padding=(0, 0),
    margins=(0, 0)
)
"""A filebrowse popup is used to obtain a filepath from the user.

    It keeps the theme of the app.
"""
import PySimpleGUI as sg

from src.globals import colors
from src.widgets import titlebar, heading, button, fillers


# window constants
HEADING_TITLE = 'CREACIÓN'
HEADING_SUBTITLE = 'INDIQUE DÓNDE GUARDAR\n\nDe estar vacío, se guardará en un path por defecto'

CONTINUE_BUTTON_TEXT = 'CONTINUAR'
CONTINUE_BUTTON_FONT = ('times', 15)
CONTINUE_BUTTON_SIZE = (50, 2)

FOLDER_INPUT_KEY = '-FOLDER-'
INPUT_SIZE = (50, 3)
INPUT_FONT = ('courier', 13)

SEARCH_BUTTON_TEXT = "Buscar"
SEARCH_BUTTON_SIZE = (15, 2)
SEARCH_BUTTON_FONT = ('times', 15)


def build():
    """Returns a window used to get the output filepath of the analysis."""
    ttitlebar = titlebar.build()

    hheading = heading.build(HEADING_TITLE, HEADING_SUBTITLE)
    inputs = build_input_field()

    ccontinue = button.build(CONTINUE_BUTTON_TEXT, '', CONTINUE_BUTTON_FONT, CONTINUE_BUTTON_SIZE)
    bottom_sep = fillers.horizontal_filler(2, colors.BACKGROUND)

    return sg.Window(
        title='',
        layout=[
            [ttitlebar],
            [hheading],
            [inputs],
            [ccontinue],
            [bottom_sep]
        ],
        element_justification='c',
        keep_on_top=True,
        no_titlebar=True
    )


def build_input_field():
    """Returns a sg.Column keeping the input + search button for the filepath."""
    input_field = sg.Input(
        key=FOLDER_INPUT_KEY,
        size=INPUT_SIZE,
        font=INPUT_FONT,
        border_width=0,
        background_color=colors.WHITE,
        readonly=True,
        disabled_readonly_background_color=colors.WHITE
    )

    button = sg.FolderBrowse(
        button_text=SEARCH_BUTTON_TEXT,
        button_color=(colors.WHITE, colors.LIGHT_GRAY),
        size=SEARCH_BUTTON_SIZE,
        font=SEARCH_BUTTON_FONT,
        target=FOLDER_INPUT_KEY
    )

    return sg.Column(
        layout=[
            [input_field, button]
        ],
        element_justification='c',
        vertical_alignment='c',
        background_color=colors.WHITE,
        pad=(20, 20)
    )
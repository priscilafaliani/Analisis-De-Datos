import PySimpleGUI as sg

from src.globals import colors
from src.widgets import titlebar, heading, button, fillers


def build():
    """Returns a window for getting the output filepath of the analysis."""
    ttitlebar = titlebar.build()

    hheading = heading.build('CREACIÓN', 'INDIQUE DÓNDE GUARDAR\n\nDe estar vacío, se guardará en un path por defecto')
    inputs = build_input_field()

    ccontinue = button.build('CONTINUAR', '', ('times', 15), (50, 2))
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
    input_field = sg.Input(
        key='-FOLDER-',
        size=(50, 3),
        font=('courier', 13),
        border_width=0,
        background_color=colors.WHITE,
        readonly=True,
        disabled_readonly_background_color=colors.WHITE
    )

    button = sg.FolderBrowse(
        button_text="Buscar",
        button_color=(colors.WHITE, colors.LIGHT_GRAY),
        size=(15, 2),
        font=('times', 15),
        target='-FOLDER-'
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
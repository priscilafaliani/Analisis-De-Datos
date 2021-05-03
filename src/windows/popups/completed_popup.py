"""A completed popup is used to indicate that an analysis was completed.


    It shows a heading indicating success, and the path
    where the analysis was saved.
"""
import PySimpleGUI as sg

from src.globals import colors
from src.widgets import titlebar, heading, button, fillers


# window constantes
HEADING_TITLE = 'ANÁLISIS COMPLETO'

MESSAGE_TEXT = 'Su archivo se guardó en\n'
MESSAGE_FONT = ('courier', 12)

BUTTON_TEXT = 'FINALIZAR'
BUTTON_FONT = ('times', 15)
BUTTON_SIZE = (25, 2)


def build(filepath):
    """Returns the window with the popup content."""
    ttitlebar = titlebar.build()
    hheading = heading.build(HEADING_TITLE)

    top_txt_filler = fillers.horizontal_filler(2, colors.BACKGROUND)

    message = sg.Text(
        text=MESSAGE_TEXT + filepath,
        font=MESSAGE_FONT,
        text_color=colors.BLACK,
        background_color=colors.BACKGROUND,
        justification='c',
        pad=(10, None) # adds space between l/r borders.
    )

    # adds space between message and button
    bottom_txt_filler = fillers.horizontal_filler(1, colors.BACKGROUND)

    # the key is not needed
    done = button.build(BUTTON_TEXT, '', BUTTON_FONT, BUTTON_SIZE)
    bottom_sep = fillers.horizontal_filler(2, colors.BACKGROUND)

    return sg.Window(
        title='',
        no_titlebar=True,
        keep_on_top=True,
        layout=[
            [ttitlebar],
            [hheading],
            [top_txt_filler],
            [message],
            [bottom_txt_filler],
            [done],
            [bottom_sep]
        ],
        element_justification='c'
    )

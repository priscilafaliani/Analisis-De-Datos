"""The base for all the card menus in the app.

    Is a menu used for selecting a dataset,
    each 'dataset' is represented by a card widget.

    The menu receives an sg.Column object, containing
    all the cards.

    These menus will all have the same colors & theme.
    They vary in the heading content, see: src/widgets/heading.py
    and the cards inside.
"""
import PySimpleGUI as sg

from src.globals import colors
from src.widgets import titlebar, heading, button, fillers


# constants for the menus
BUTTON_FONT = ('times', 15)

MAIN_WINDOW_TITLE = 'ANÁLISIS DE DATOS'
MAIN_WINDOW_SUBTITLE = 'SELECCIONE UN SET DE DATOS'


def build(cards, exit_button_text, key, button_size):
    """Builds a menu with the given cards and a button."""
    ttitlebar = titlebar.build()
    hheading = heading.build(MAIN_WINDOW_TITLE, MAIN_WINDOW_SUBTITLE)
    exit_button = button.build(exit_button_text, key, BUTTON_FONT, button_size)

    # adds space between button and bottom border
    bottom_sep = fillers.horizontal_filler(1, colors.BACKGROUND)

    window = sg.Window(
        title='',
        layout=[
            [ttitlebar],
            [hheading],
            [cards],
            [exit_button],
            [bottom_sep]
        ],
        no_titlebar=True,
        keep_on_top=True,
        element_justification='c'
    )

    return window
"""Builds a custom cards menu window."""
import PySimpleGUI as sg

from src.globals.texts import menu_texts
from src.globals import colors

from src.widgets import titlebar, heading, button, fillers


def build(cards, exit_button_text, key, size):
    """Builds a menu with the given cards and an optional return button."""
    ttitlebar = titlebar.build()
    hheading = heading.build(menu_texts.MAIN_WINDOW_TITLE, menu_texts.MAIN_WINDOW_SUBTITLE)
    exit_button = button.build(exit_button_text, key, ('times', 15), size)

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
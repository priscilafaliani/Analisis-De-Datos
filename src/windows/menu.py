"""Builds a custom cards menu window."""
import PySimpleGUI as sg

from src.globals.texts import menu_texts

from src.widgets import titlebar, heading


def build(cards, titlebar_return=False):
    """Builds a menu with the given cards and an optional return button."""
    ttitlebar = titlebar.build(titlebar_return)
    hheading = heading.build(menu_texts.MAIN_WINDOW_TITLE, menu_texts.MAIN_WINDOW_SUBTITLE)

    window = sg.Window(
        title='',
        layout=[
            [ttitlebar],
            [hheading],
            [cards]
        ],
        no_titlebar=True,
        keep_on_top=True
    )

    return window
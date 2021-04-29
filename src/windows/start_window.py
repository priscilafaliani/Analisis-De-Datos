import PySimpleGUI as sg

import src.globals as g

from src.widgets.titlebar import titlebar
from src.widgets.heading import heading
from src.widgets.card import card

def build():
    ttitlebar = titlebar()
    hheading = heading(g.MAIN_WINDOW_TITLE, g.MAIN_WINDOW_SUBTITLE)

    eli5 = card(
        g.ELI5_ICON, 
        g.ELI5_CARD_TITLE, 
        g.ELI5_CARD_SUBTITLE, 
        g.ELI5_KEY
    )

    lpt = card(
        g.LTP_ICON, 
        g.LPT_CARD_TITLE, 
        g.LPT_CARD_SUBTITLE, 
        g.LPT_KEY
    )

    cards_container = sg.Column(
        layout=[
            [eli5, lpt]
        ],
        background_color=g.WHITE,
        element_justification='c',
        vertical_alignment='c'
    )

    window = sg.Window(
        title='',
        layout=[
            [ttitlebar],
            [hheading],
            [cards_container]
        ],
        no_titlebar=True,
        keep_on_top=True
    )

    return window
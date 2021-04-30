import PySimpleGUI as sg

import src.globals as g

from src.widgets.titlebar import titlebar
from src.widgets.heading import heading
from src.widgets.card import card

def build():
    ttitlebar = titlebar()
    hheading = heading(g.MAIN_WINDOW_TITLE, g.MAIN_WINDOW_SUBTITLE)

    reddit = card(
        g.REDDIT_ICON,
        g.REDDIT_CARD_TITLE,
        g.REDDIT_CARD_SUBTITLE,
        g.REDDIT_KEY
    )

    museum = card(
        g.MUSEUM_ICON, 
        g.MUSEUM_CARD_TILTE, 
        g.MUSEUM_CARD_SUBTITLE, 
        g.MUSEUM_KEY
    )

    cards_container = sg.Column(
        layout=[
            [reddit, museum]
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
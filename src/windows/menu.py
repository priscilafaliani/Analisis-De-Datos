import PySimpleGUI as sg

import src.globals.keys as k
import src.globals.paths as p
import src.globals.color_palette as c
import src.globals.texts.menu_texts as menu_texts
import src.globals.texts.reddit_texts as reddit_texts
import src.globals.texts.museum_texts as museum_texts

from src.widgets.titlebar import titlebar
from src.widgets.heading import heading
from src.widgets.card import card

def build():
    ttitlebar = titlebar()
    hheading = heading(menu_texts.MAIN_WINDOW_TITLE, menu_texts.MAIN_WINDOW_SUBTITLE)

    reddit = card(
        p.REDDIT_ICON,
        reddit_texts.REDDIT_CARD_TITLE,
        reddit_texts.REDDIT_CARD_SUBTITLE,
        k.REDDIT_KEY
    )

    museum = card(
        p.MUSEUM_ICON, 
        museum_texts.MUSEUM_CARD_TILTE, 
        museum_texts.MUSEUM_CARD_SUBTITLE, 
        k.MUSEUM_KEY
    )

    cards_container = sg.Column(
        layout=[
            [reddit, museum]
        ],
        background_color=c.WHITE,
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
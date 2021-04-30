import PySimpleGUI as sg

import src.globals.keys as k
import src.globals.paths as p
import src.globals.color_palette as c
import src.globals.texts.hw_texts as hw_texts
import src.globals.texts.gs_texts as gs_texts
import src.globals.texts.menu_texts as menu_texts
import src.globals.texts.reddit_texts as reddit_texts

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
    
    hello_world = card(
        p.HW_ICON,
        hw_texts.HW_CARD_TITLE,
        hw_texts.HW_CARD_SUBTITLE,
        k.HW_KEY
    )
    
    games_sales = card(
        p.GAMES_ICON,
        gs_texts.GS_CARD_TITLE,
        gs_texts.GS_CARD_SUBTITLE,
        k.GS_KEY    
    )
    
    cards_container = sg.Column(
        layout=[
            [reddit, hello_world, games_sales]
        ],
        background_color=c.BACKGROUND,
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
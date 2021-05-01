import PySimpleGUI as sg

from src.globals import keys, paths, colors
from src.globals.texts import menu_texts, reddit_texts, hw_texts, gs_texts

from src.widgets import titlebar, heading, card


def build():
    ttitlebar = titlebar.build()
    hheading = heading.build(menu_texts.MAIN_WINDOW_TITLE, menu_texts.MAIN_WINDOW_SUBTITLE)

    reddit = card.build(
        paths.REDDIT_ICON,
        reddit_texts.REDDIT_CARD_TITLE,
        reddit_texts.REDDIT_CARD_SUBTITLE,
        keys.REDDIT_KEY
    )
    
    hello_world = card.build(
        paths.HW_ICON,
        hw_texts.HW_CARD_TITLE,
        hw_texts.HW_CARD_SUBTITLE,
        keys.HW_KEY
    )
    
    games_sales = card.build(
        paths.GAMES_ICON,
        gs_texts.GS_CARD_TITLE,
        gs_texts.GS_CARD_SUBTITLE,
        keys.GS_KEY    
    )
    
    cards_container = sg.Column(
        layout=[
            [reddit, hello_world, games_sales]
        ],
        background_color=colors.BACKGROUND,
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
"""The first window shown in the program."""
import PySimpleGUI as sg

from src.windows import menu

from src.globals import keys, paths, colors
from src.globals.texts import reddit_texts, hw_texts, gs_texts

from src.widgets import card


def build():
    return menu.build(build_card_section(), 'SALIR', keys.EXIT_EVENT, (50, 2))


def build_card_section():
    """Returns a container with a row of cards for the menu."""
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
    
    return cards_container
"""The first window shown in the program.

    Is a card menu, see -> src/windows/card_menu.py.
"""
import PySimpleGUI as sg

from src.windows.menus import card_menu

from src.widgets import card

from src.globals import keys, paths

# the texts for the cards
from src.globals.texts import reddit_texts, music_texts, gs_texts


# constants for this menu
BUTTON_MESSAGE = 'SALIR'
BUTTON_SIZE = (50, 2)


def build():
    """Builds menu with the cards from the build_card_section function."""
    return card_menu.build(
        build_card_section(), 
        BUTTON_MESSAGE, 
        keys.EXIT_EVENT, 
        BUTTON_SIZE
    )


def build_card_section():
    """Builds a row with the cards of reddit, music and games sales."""
    reddit = card.build(
        paths.REDDIT_ICON,
        reddit_texts.REDDIT_CARD_TITLE,
        reddit_texts.REDDIT_CARD_SUBTITLE,
        keys.REDDIT_KEY
    )
    
    music = card.build(
        paths.MUSIC_ICON,
        music_texts.MUSIC_CARD_TITLE,
        music_texts.MUSIC_CARD_SUBTITLE,
        keys.MUSIC_KEY
    )
    
    games_sales = card.build(
        paths.GAMES_ICON,
        gs_texts.GS_CARD_TITLE,
        gs_texts.GS_CARD_SUBTITLE,
        keys.GS_KEY    
    )
    
    cards_container = sg.Column(
        layout=[
            [reddit, music, games_sales]
        ],
        element_justification='c',
        vertical_alignment='c'
    )
    
    return cards_container
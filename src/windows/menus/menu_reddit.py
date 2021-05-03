"""Window shown when the option "reddit" is choosen in menu.py

    Is a card menu, see -> src/windows/card_menu.py
"""
import PySimpleGUI as sg

from src.windows.menus import card_menu

from src.globals import keys, paths, colors
from src.globals.texts import datasets_descriptions_texts

from src.widgets import titlebar, heading, card


# menu constants
BUTTON_MESSAGE = 'VOLVER ATRÁS'
BUTTON_SIZE = (50, 2)


def build():
    """Builds menu with the cards from the build_card_section function."""
    return card_menu.build(
        build_card_section(), 
        BUTTON_MESSAGE, 
        keys.RETURN_EVENT, 
        BUTTON_SIZE
    )


def build_card_section():
    """Returns a container with a row of cards for the menu."""
    lpt = card.build(
        paths.LTP_ICON,
        datasets_descriptions_texts.LPT_CARD_TITLE,
        datasets_descriptions_texts.LPT_CARD_SUBTITLE,
        keys.LPT_KEY
    )
    
    ph = card.build(
        paths.PH_ICON,
        datasets_descriptions_texts.PH_CARD_TITLE,
        datasets_descriptions_texts.PH_CARD_SUBTITLE,
        keys.PH_KEY
    )

    cards_container = sg.Column(
        layout=[
            [lpt, ph]
        ],
        background_color=colors.BACKGROUND,
        element_justification='c',
        vertical_alignment='c'
    )
    
    return cards_container
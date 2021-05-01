"""Window shown when the option "reddit" is choosen in menu.py"""
import PySimpleGUI as sg

from src.globals import keys, paths, colors
from src.globals.texts import menu_texts, lpt_texts, st_texts

from src.widgets import titlebar, heading, card


def build():
    ttitlebar = titlebar.build()
    hheading = heading.build(menu_texts.MAIN_WINDOW_TITLE, menu_texts.MAIN_WINDOW_SUBTITLE)
    cards = build_card_section()

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


def build_card_section():
    """Returns a container with a row of cards for the menu."""
    lpt = card.build(
        paths.LTP_ICON,
        lpt_texts.LPT_CARD_TITLE,
        lpt_texts.LPT_CARD_SUBTITLE,
        keys.LPT_KEY
    )
    
    st = card.build(
        paths.ST_ICON,
        st_texts.ST_CARD_TITLE,
        st_texts.ST_CARD_SUBTITLE,
        keys.ST_KEY
    )

    cards_container = sg.Column(
        layout=[
            [lpt, st]
        ],
        background_color=colors.BACKGROUND,
        element_justification='c',
        vertical_alignment='c'
    )
    
    return cards_container
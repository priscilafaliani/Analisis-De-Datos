"""Builds the type of card used on the menus."""
import PySimpleGUI as sg

from src.globals import colors
from src.globals.texts import general

from src.widgets import fillers, button


CARD_BUTTON_SIZE = (25, 2)
# defines the width of the card
SUBTITLE_SIZE = (35, None)

CARD_TITLE_FONT = ('times', '20')
CARD_SUBTITLE_FONT = ('courier', 12, 'bold')
CARD_BUTTON_FONT = ('times', 15)

CARD_SPACE_AROUND = (10, 10)

def build(icon_path, title, subtitle, key):
    # space between icon and top border
    TOP_SEP = fillers.horizontal_filler(2, colors.WHITE)
    
    icon = sg.Image(
        filename=icon_path,
        background_color=colors.WHITE,
    )

    content = build_card_content(title, subtitle)
    
    # space between content and button
    CONTENT_SEP = fillers.horizontal_filler(2, colors.WHITE)
    
    read_more = button.build(
        general.CARD_BUTTON_TEXT,
        key,
        CARD_BUTTON_FONT,
        CARD_BUTTON_SIZE
    )

    # space between the button and the bottom border
    BOTTOM_SEP = fillers.horizontal_filler(2, colors.WHITE)

    return sg.Column(
        layout=[
            [TOP_SEP],
            [icon],
            [content],
            [CONTENT_SEP],
            [read_more],
            [BOTTOM_SEP]
        ],
        background_color=colors.WHITE,
        element_justification='c',
        vertical_alignment='c',
        pad=CARD_SPACE_AROUND
    )


def build_card_content(title, subtitle):
    """Returns a container with the texts of the card."""
    title = sg.Text(
        text=title,
        background_color=colors.WHITE,
        text_color=colors.ORANGE,
        justification='c',
        font=CARD_TITLE_FONT
    )

    subtitle = sg.Text(
        text=subtitle,
        background_color=colors.WHITE,
        text_color=colors.BLACK,
        justification='c',
        font=CARD_SUBTITLE_FONT,
        size=SUBTITLE_SIZE
    )
    
    return sg.Column(
        layout=[
            [title],
            [subtitle],
        ],
        background_color=colors.WHITE,
        element_justification='c',
        vertical_alignment='c'
    )


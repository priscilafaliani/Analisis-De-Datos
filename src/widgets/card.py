import PySimpleGUI as sg

from src.globals import colors
from src.globals.texts import general

from src.widgets import fillers


# defines the width of the card & space between sub and button
SUBTITLE_SIZE = (35, 5)
BUTTON_SIZE = (25, 2)
# space between the button and the bottom border
BUTTON_BOTTOM_SEP = ((0, 0), (0, 20))

CARD_TITLE_FONT = ('times', '20')
CARD_SUBTITLE_FONT = ('courier', 12, 'bold')
CARD_BUTTON_FONT = ('times', 15)

def build(icon_path, title, subtitle, key):
    # space between icon and top border
    IMAGE_TOP_SEP = fillers.horizontal_filler(2, colors.WHITE)
    
    icon = sg.Image(
        filename=icon_path,
        background_color=colors.WHITE,
    )

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

    button = sg.Button(
        button_text=general.CARD_BUTTON_TEXT,
        button_color=(colors.WHITE, colors.LIGHT_GRAY),
        mouseover_colors=(colors.WHITE, colors.ORANGE),
        key=key,
        font=CARD_BUTTON_FONT,
        size=BUTTON_SIZE,
        pad=BUTTON_BOTTOM_SEP
    )

    container = sg.Column(
        layout=[
            [IMAGE_TOP_SEP],
            [icon],
            [title],
            [subtitle],
            [button]
        ],
        background_color=colors.WHITE,
        element_justification='c',
        vertical_alignment='c',
        pad=(10, 10)
    )

    return container
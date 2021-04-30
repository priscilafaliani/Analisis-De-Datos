import PySimpleGUI as sg

import src.globals.color_palette as c
import src.globals.texts.general as g


# space between icon and top border
IMAGE_TOP_SEP = ((0, 0), (15, 0))
# defines the width of the card & space between sub and button
SUBTITLE_SIZE = (35, 5)
BUTTON_SIZE = (25, 2)
# space between the button and the bottom border
BUTTON_BOTTOM_SEP = ((0, 0), (0, 20))

CARD_TITLE_FONT = ('times', '20')
CARD_SUBTITLE_FONT = ('courier', 12, 'bold')
CARD_BUTTON_FONT = ('times', 15)

def card(icon_path, title, subtitle, key):
    icon = sg.Image(
        filename=icon_path,
        background_color=c.WHITE,
        pad=IMAGE_TOP_SEP
    )

    title = sg.Text(
        text=title,
        background_color=c.WHITE,
        text_color=c.ORANGE,
        justification='c',
        font=CARD_TITLE_FONT
    )

    subtitle = sg.Text(
        text=subtitle,
        background_color=c.WHITE,
        text_color=c.BLACK,
        justification='c',
        font=CARD_SUBTITLE_FONT,
        size=SUBTITLE_SIZE
    )

    button = sg.Button(
        button_text=g.CARD_BUTTON_TEXT,
        button_color=(c.WHITE, c.LIGHT_GRAY),
        mouseover_colors=(c.WHITE, c.ORANGE),
        key=key,
        font=CARD_BUTTON_FONT,
        size=BUTTON_SIZE,
        pad=BUTTON_BOTTOM_SEP
    )

    container = sg.Column(
        layout=[
            [icon],
            [title],
            [subtitle],
            [button]
        ],
        background_color=c.WHITE,
        element_justification='c',
        vertical_alignment='c',
        pad=(10, 10)
    )

    return container
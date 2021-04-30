import PySimpleGUI as sg

import src.globals.color_palette as c
import src.globals.texts.general as g


def card(icon_path, title, subtitle, key):
    icon = sg.Image(
        filename=icon_path,
        background_color=c.WHITE
    )

    title = sg.Text(
        text=title,
        background_color=c.WHITE,
        text_color=c.ORANGE,
        justification='c'
    )

    subtitle = sg.Text(
        text=subtitle,
        background_color=c.WHITE,
        text_color=c.BLACK,
        justification='c'
    )

    button = sg.Button(
        button_text=g.CARD_BUTTON_TEXT,
        button_color=(c.WHITE, c.DARK_GRAY),
        mouseover_colors=(c.WHITE, c.ORANGE),
        key=key
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
        vertical_alignment='c'
    )

    return container
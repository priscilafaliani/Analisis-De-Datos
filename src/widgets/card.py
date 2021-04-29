import PySimpleGUI as sg

import src.globals as g


def card(icon_path, title, subtitle, key):
    icon = sg.Image(
        filename=icon_path,
        background_color=g.WHITE
    )

    title = sg.Text(
        text=title,
        background_color=g.WHITE,
        text_color=g.ORANGE,
        justification='c'
    )

    subtitle = sg.Text(
        text=subtitle,
        background_color=g.WHITE,
        text_color=g.BLACK,
        justification='c'
    )

    button = sg.Button(
        button_text=g.CARD_BUTTON_TEXT,
        button_color=(g.WHITE, g.DARK_GRAY),
        mouseover_colors=(g.WHITE, g.ORANGE),
        key=key
    )

    container = sg.Column(
        layout=[
            [icon],
            [title],
            [subtitle],
            [button]
        ],
        background_color=g.WHITE,
        element_justification='c',
        vertical_alignment='c'
    )

    return container
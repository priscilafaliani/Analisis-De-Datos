import PySimpleGUI as sg

import src.globals as g

from src.widgets.titlebar import titlebar

def build(title, subtitle, content):
    ttitlebar = titlebar()

    icon = sg.Image(
        filename=g.POPUP_ICON,
        background_color=g.WHITE
    )

    title = sg.Text(
        text=title,
        background_color=g.WHITE,
        text_color=g.BLUE,
        justification='c'
    )

    subtitle = sg.Text(
        text=subtitle,
        background_color=g.WHITE,
        text_color=g.BLACK,
        justification='c'
    )

    content = sg.Text(
        text=content,
        background_color=g.WHITE,
        text_color=g.BLACK,
        justification='c'
    )

    analyse_button = sg.Button(
        button_text=g.POPUP_BUTTON1_TEXT,
        button_color=(g.WHITE, g.DARK_GREY),
        mouseover_colors=(g.WHITE, g.ORANGE)
    )

    cancel_button = sg.Button(
        button_text=g.POPUP_BUTTON2_TEXT,
        button_color=(g.WHITE, g.DARK_GREY),
        mouseover_colors=(g.WHITE, g.ORANGE)
    )

    container = sg.Column(
        layout=[
            [ttitlebar],
            [icon],
            [title],
            [subtitle],
            [content],
            [analyse_button],
            [cancel_button]
        ],
        background_color=g.WHITE,
        element_justification='c',
        vertical_alignment='c',
    )

    window = sg.Window(
        title='',
        layout=[
            [container]
        ],
        no_titlebar=True,
        keep_on_top=True,
    )

    return window
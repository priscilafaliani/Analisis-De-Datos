import PySimpleGUI as sg

import src.globals as g


def heading(title, subtitle=''):
    """Heading with a title & maybe a subtitle"""
    title = sg.Text(
        text=title,
        background_color=g.DARK_GREY,
        text_color=g.WHITE,
        justification='c',
        grab=True
    )

    subtitle = sg.Text(
        text=subtitle,
        background_color=g.DARK_GREY,
        text_color=g.WHITE,
        justification='c',
        grab=True
    )

    container = sg.Column(
        layout=[[title], [subtitle]],
        background_color=g.DARK_GREY,
        expand_x=True,
        element_justification='c',
        vertical_alignment='c',
        grab=True
    )

    return container
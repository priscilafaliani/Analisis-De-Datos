import PySimpleGUI as sg

import src.globals.paths as p
import src.globals.texts.general as g
import src.globals.keys as k
import src.globals.color_palette as c

from src.widgets.titlebar import titlebar

def build(key, title, subtitle, content, choices):
    """Builds a pop up which shows information about the selected card.

        OPTIONAL: a list of choices to show.
    """
    ttitlebar = titlebar()

    icon = sg.Image(
        filename=p.POPUP_ICON,
        background_color=c.WHITE
    )

    title = sg.Text(
        text=title,
        background_color=c.WHITE,
        text_color=c.VIOLET,
        justification='c'
    )

    subtitle = sg.Text(
        text=subtitle,
        background_color=c.WHITE,
        text_color=c.BLACK,
        justification='c'
    )

    content = sg.Text(
        text=content,
        background_color=c.WHITE,
        text_color=c.BLACK,
        justification='c'
    )

    container = sg.Column(
        layout=[
            [ttitlebar],
            [icon],
            [title],
            [subtitle],
            [content]
        ],
        background_color=c.WHITE,
        element_justification='c',
        vertical_alignment='c',
    )

    if choices:
        popup = add_choices(container, choices)
        continue_button_text = g.POPUP_BUTTON1_TEXT2
    else:
        continue_button_text = g.POPUP_BUTTON1_TEXT

    continue_button = sg.Button(
        button_text=continue_button_text,
        button_color=(c.WHITE, c.DARK_GRAY),
        mouseover_colors=(c.WHITE, c.ORANGE),
        key=key
    )

    cancel_button = sg.Button(
        button_text=g.POPUP_BUTTON2_TEXT,
        button_color=(c.WHITE, c.DARK_GRAY),
        mouseover_colors=(c.WHITE, c.ORANGE),
        key=k.RETURN_EVENT
    )

    container.add_row(continue_button),
    container.add_row(cancel_button)

    window = sg.Window(
        title='',
        layout=[
            [container]
        ],
        no_titlebar=True,
        keep_on_top=True,
    )

    return window


def add_choices(popup, choices):
    """Receives a popup and adds a list of choices."""
    options_list = sg.Combo(
        values=choices,
        default_value=choices[0],
        size=(18, None),
        background_color=c.WHITE,
        text_color=c.BLACK
    )

    popup.add_row(options_list)
    return popup
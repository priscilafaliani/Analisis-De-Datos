import PySimpleGUI as sg

import src.globals.color_palette as c
import src.globals.paths as p
import src.globals.keys as k


def titlebar():
    """Title bar with an exit button."""
    exit_button = sg.Button(
        image_filename=p.EXIT_BUTTON_ICON,
        image_size=(18, 18),
        image_subsample=4,
        button_color=(c.LIGHT_GRAY, c.LIGHT_GRAY),
        border_width=0,
        key=k.EXIT_EVENT,
        pad=(10, 10)
    )

    container = sg.Column(
        layout=[[exit_button]],
        vertical_alignment='c',
        element_justification='r',
        expand_x=True,
        background_color=c.LIGHT_GRAY,
        grab=True
    )

    return container
import PySimpleGUI as sg

import src.globals as g


def titlebar():
    """Title bar with an exit button."""
    exit_button = sg.Button(
        image_filename=g.EXIT_BUTTON_ICON,
        image_size=(20, 20),
        image_subsample=(2),
        button_color=(g.LIGHT_GRAY, g.LIGHT_GRAY),
        border_width=0
    )

    container = sg.Column(
        layout=[[exit_button]],
        vertical_alignment='c',
        element_justification='r',
        expand_x=True,
        background_color=g.LIGHT_GRAY,
        grab=True
    )

    return container
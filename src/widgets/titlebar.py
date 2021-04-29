import PySimpleGUI as sg

import src.globals as g


def titlebar():
    """Title bar with an exit button."""
    exit_button = sg.Button(
        image_filename=g.EXIT_BUTTON_ICON,
        image_size=(20, 20),
        image_subsample=(2),
        button_color=(g.LIGHT_GREY, g.LIGHT_GREY)
    )

    container = sg.Column(
        layout=[[exit_button]],
        vertical_alignment='c',
        element_justification='c',
        expand_x=True,
        background_color=g.LIGHT_GREY,
        grab=True
    )

    return container
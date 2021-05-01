import PySimpleGUI as sg

from src.globals import colors, paths, keys

def build():
    """Title bar with an exit button."""
    exit_button = sg.Button(
        image_filename=paths.EXIT_BUTTON_ICON,
        image_size=(18, 18),
        image_subsample=4,
        button_color=(colors.LIGHT_GRAY, colors.LIGHT_GRAY),
        border_width=0,
        key=keys.EXIT_EVENT,
        pad=(10, 10)
    )

    container = sg.Column(
        layout=[[exit_button]],
        vertical_alignment='c',
        element_justification='r',
        expand_x=True,
        background_color=colors.LIGHT_GRAY,
        grab=True
    )

    return container
import PySimpleGUI as sg

from src.globals import colors, paths, keys
from src.widgets import fillers

def build():
    """A pseudo title bar, with no buttons."""
    container = sg.Column(
        layout=[[fillers.horizontal_filler(1, colors.LIGHT_GRAY)]],
        vertical_alignment='c',
        element_justification='r',
        expand_x=True,
        background_color=colors.LIGHT_GRAY,
        grab=True
    )

    return container
import PySimpleGUI as sg

from src.globals import colors
from src.components import menu


def start():
    # set global configurations
    sg.set_options(
        auto_size_buttons=False,
        background_color=colors.BACKGROUND,
        element_padding=(0, 0),
        margins=(0, 0),
        font='helvetica'
    )

    menu.start()
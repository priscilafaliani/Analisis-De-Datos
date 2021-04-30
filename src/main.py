import PySimpleGUI as sg
import src.globals.color_palette as c

from src.components import menu

def start():
    # set global configurations
    sg.set_options(
        auto_size_buttons=False,
        background_color=c.BACKGROUND,
        element_padding=(0, 0),
        margins=(0, 0),
        font='helvetica'
    )

    menu.start()
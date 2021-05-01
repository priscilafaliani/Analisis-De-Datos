import PySimpleGUI as sg

from src.globals import colors


def build(text, key, font, size):
    """Returns a button with the current theme"""   
    button = sg.Button(
        button_text=text,
        button_color=(colors.WHITE, colors.LIGHT_GRAY),
        mouseover_colors=(colors.WHITE, colors.ORANGE),
        key=key,
        font=font,
        size=size,
    )
    
    return button
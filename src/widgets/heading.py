import PySimpleGUI as sg

from src.globals import colors

HEADING_TITLE_FONT = ('times', 30, 'bold')
HEADING_SUBTITLE_FONT = ('courier', 15)

def build(title, subtitle=''):
    """Heading with a title & maybe a subtitle"""
    title = sg.Text(
        text=title,
        background_color=colors.DARK_GRAY,
        text_color=colors.WHITE,
        justification='c',
        grab=True,
        font=HEADING_TITLE_FONT
    )

    subtitle = sg.Text(
        text=subtitle,
        background_color=colors.DARK_GRAY,
        text_color=colors.WHITE,
        justification='c',
        grab=True,
        font=HEADING_SUBTITLE_FONT
    )

    container = sg.Column(
        layout=[[title], [subtitle]],
        background_color=colors.DARK_GRAY,
        expand_x=True,
        element_justification='c',
        vertical_alignment='c',
        grab=True
    )

    return container
import PySimpleGUI as sg
import src.globals.color_palette as c

HEADING_TITLE_FONT = ('times', 30, 'bold')
HEADING_SUBTITLE_FONT = ('courier', 15)

def heading(title, subtitle=''):
    """Heading with a title & maybe a subtitle"""
    title = sg.Text(
        text=title,
        background_color=c.DARK_GRAY,
        text_color=c.WHITE,
        justification='c',
        grab=True,
        font=HEADING_TITLE_FONT
    )

    subtitle = sg.Text(
        text=subtitle,
        background_color=c.DARK_GRAY,
        text_color=c.WHITE,
        justification='c',
        grab=True,
        font=HEADING_SUBTITLE_FONT
    )

    container = sg.Column(
        layout=[[title], [subtitle]],
        background_color=c.DARK_GRAY,
        expand_x=True,
        element_justification='c',
        vertical_alignment='c',
        grab=True
    )

    return container
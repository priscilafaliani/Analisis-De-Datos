import PySimpleGUI as sg

from src.globals import colors
from src.widgets import titlebar, heading, button, fillers

def build(filepath):
    ttitlebar = titlebar.build()
    hheading = heading.build('ANÁLISIS COMPLETO')

    top_txt_filler = fillers.horizontal_filler(2, colors.BACKGROUND)

    message = sg.Text(
        text=f'Su archivo se guardó en\n{filepath}',
        font=('courier', 12),
        text_color=colors.BLACK,
        background_color=colors.BACKGROUND,
        justification='c',
        pad=(10, None)
    )

    bottom_txt_filler = fillers.horizontal_filler(1, colors.BACKGROUND)

    done = button.build('FINALIZAR', '', ('times', 15), (25, 2))
    bottom_sep = fillers.horizontal_filler(2, colors.BACKGROUND)

    return sg.Window(
        title='',
        no_titlebar=True,
        keep_on_top=True,
        layout=[
            [ttitlebar],
            [hheading],
            [top_txt_filler],
            [message],
            [bottom_txt_filler],
            [done],
            [bottom_sep]
        ],
        element_justification='c'
    )

import PySimpleGUI as sg

import src.globals.paths as p
import src.globals.texts.general as g
import src.globals.keys as k
import src.globals.color_palette as c

from src.widgets.titlebar import titlebar


# space between icon and top border
IMAGE_TOP_SEP = ((0, 0), (20, 0))
# defines the width of the card & space between sub and button
SUBTITLE_SIZE = (50, 4)
BUTTON_SIZE = (35, 2)
# separates content from buttons/combobox
CONTENT_SIZE = (None, 4)
# space between the button and the bottom border
BUTTON_BOTTOM_SEP = ((0, 0), (0, 20))

CARD_TITLE_FONT = ('times', '20', 'bold')
CARD_SUBTITLE_FONT = ('courier', 12, 'bold')
CARD_BUTTON_FONT = ('times', 15)
CONTENT_FONT = ('courier', '12')


def build(key, title, subtitle, content, choices):
    """Builds a pop up which shows information about the selected card.

        OPTIONAL: a list of choices to show.
    """
    ttitlebar = titlebar()

    icon = sg.Image(
        filename=p.POPUP_ICON,
        background_color=c.WHITE,
        pad=IMAGE_TOP_SEP
    )

    title = sg.Text(
        text=title,
        background_color=c.WHITE,
        text_color=c.VIOLET,
        justification='c',
        font=CARD_TITLE_FONT
    )

    subtitle = sg.Text(
        text=subtitle,
        background_color=c.WHITE,
        text_color=c.BLACK,
        justification='c',
        font=CARD_SUBTITLE_FONT,
        size=SUBTITLE_SIZE
    )

    content = sg.Text(
        text=content,
        background_color=c.WHITE,
        text_color=c.BLACK,
        justification='c',
        size=CONTENT_SIZE,
        font=CONTENT_FONT,
        pad=((0, 0), (0, 20))
    )

    container = sg.Column(
        layout=[
            [icon],
            [title],
            [subtitle],
            [content]
        ],
        background_color=c.WHITE,
        element_justification='c',
        vertical_alignment='c',
        pad=(10, 10)
    )

    if choices:
        popup = add_choices(container, choices)
        continue_button_text = g.POPUP_BUTTON1_TEXT2
    else:
        continue_button_text = g.POPUP_BUTTON1_TEXT

    continue_button = sg.Button(
        button_text=continue_button_text,
        button_color=(c.WHITE, c.DARK_GRAY),
        mouseover_colors=(c.WHITE, c.ORANGE),
        key=key,
        size=BUTTON_SIZE,
        pad=BUTTON_BOTTOM_SEP,
        font=CARD_BUTTON_FONT
    )

    cancel_button = sg.Button(
        button_text=g.POPUP_BUTTON2_TEXT,
        button_color=(c.WHITE, c.DARK_GRAY),
        mouseover_colors=(c.WHITE, c.ORANGE),
        key=k.RETURN_EVENT,
        size=BUTTON_SIZE,
        pad=BUTTON_BOTTOM_SEP,
        font=CARD_BUTTON_FONT
    )

    container.add_row(continue_button),
    container.add_row(cancel_button)

    window = sg.Window(
        title='',
        layout=[
            [ttitlebar],
            [container]
        ],
        no_titlebar=True,
        keep_on_top=True,
        element_justification='c'
    )

    return window


def add_choices(popup, choices):
    """Receives a popup and adds a list of choices."""
    options_list = sg.Combo(
        values=choices,
        default_value=choices[0],
        size=(35, None),
        background_color=c.WHITE,
        text_color=c.BLACK,
        pad=(20, 20)
    )

    popup.add_row(options_list)
    return popup
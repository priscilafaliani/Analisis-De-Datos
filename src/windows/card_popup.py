import PySimpleGUI as sg

from src.globals.texts import general
from src.globals import paths, keys, colors

from src.widgets import titlebar


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


def build_popup_content(title, subtitle, content):
    """Returns a container with the content for this popup.
    
        This is the part that changes between popups.
    """
    title = sg.Text(
        text=title,
        background_color=colors.WHITE,
        text_color=colors.VIOLET,
        justification='c',
        font=CARD_TITLE_FONT
    )

    subtitle = sg.Text(
        text=subtitle,
        background_color=colors.WHITE,
        text_color=colors.BLACK,
        justification='c',
        font=CARD_SUBTITLE_FONT,
        size=SUBTITLE_SIZE
    )

    content = sg.Text(
        text=content,
        background_color=colors.WHITE,
        text_color=colors.BLACK,
        justification='c',
        size=CONTENT_SIZE,
        font=CONTENT_FONT,
        pad=((0, 0), (0, 20))
    )

    container = sg.Column(
        layout=[
            [title],
            [subtitle],
            [content]
        ],
        background_color=colors.WHITE,
        element_justification='c',
        vertical_alignment='c',
        pad=(10, 10)
    )
    
    return container


def build(key, title, subtitle, content):
    """Builds a pop up which shows information about the selected card.

        OPTIONAL: a list of choices to show.
    """
    ttitlebar = titlebar.build()

    icon = sg.Image(
        filename=paths.POPUP_ICON,
        background_color=colors.WHITE,
        pad=IMAGE_TOP_SEP
    )
    
    popup_content = build_popup_content(title, subtitle, content)

    continue_button = sg.Button(
        button_text=general.POPUP_BUTTON1_TEXT,
        button_color=(colors.WHITE, colors.DARK_GRAY),
        mouseover_colors=(colors.WHITE, colors.ORANGE),
        key=key,
        size=BUTTON_SIZE,
        pad=BUTTON_BOTTOM_SEP,
        font=CARD_BUTTON_FONT
    )

    cancel_button = sg.Button(
        button_text=general.POPUP_BUTTON2_TEXT,
        button_color=(colors.WHITE, colors.DARK_GRAY),
        mouseover_colors=(colors.WHITE, colors.ORANGE),
        key=keys.RETURN_EVENT,
        size=BUTTON_SIZE,
        pad=BUTTON_BOTTOM_SEP,
        font=CARD_BUTTON_FONT
    )

    window = sg.Window(
        title='',
        layout=[
            [ttitlebar],
            [icon],
            [popup_content],
            [continue_button],
            [cancel_button]
        ],
        no_titlebar=True,
        keep_on_top=True,
        element_justification='c'
    )

    return window
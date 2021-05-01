import PySimpleGUI as sg

from src.globals.texts import general
from src.globals import paths, keys, colors

from src.widgets import titlebar, fillers


BUTTON_SIZE = (35, 2)
# defines the width of the card 
SUBTITLE_SIZE = (50, None)

POPUP_TITLE_FONT = ('times', '20', 'bold')
POPUP_SUBTITLE_FONT = ('courier', 12, 'bold')
POPUP_CONTENT_FONT = ('courier', '12')
POPUP_BUTTON_FONT = ('times', 15)


def build(key, title, subtitle, content):
    """Builds a pop up which shows information about the selected card.

        OPTIONAL: a list of choices to show.
    """
    ttitlebar = titlebar.build()
    
    # space between icon and top border
    IMAGE_TOP_SEP = fillers.horizontal_filler(2, colors.WHITE)

    icon = sg.Image(
        filename=paths.POPUP_ICON,
        background_color=colors.WHITE,
    )
    
    popup_content = build_popup_content(title, subtitle, content)
    buttons = build_buttons_section(key)   

    window = sg.Window(
        title='',
        layout=[
            [ttitlebar],
            [IMAGE_TOP_SEP],
            [icon],
            [popup_content],
            [buttons]
        ],
        no_titlebar=True,
        keep_on_top=True,
        element_justification='c',
        background_color=colors.WHITE
    )

    return window


def build_popup_content(title, subtitle, content):
    """Returns a container with the content for this popup.
    
        This is the part that changes between popups.
    """
    title = sg.Text(
        text=title,
        background_color=colors.WHITE,
        text_color=colors.VIOLET,
        justification='c',
        font=POPUP_TITLE_FONT
    )

    subtitle = sg.Text(
        text=subtitle,
        background_color=colors.WHITE,
        text_color=colors.BLACK,
        justification='c',
        font=POPUP_SUBTITLE_FONT,
        size=SUBTITLE_SIZE
    )

    # adds space between content and the bottom border
    CONTENT_BOTTOM_SEP = fillers.horizontal_filler(2, colors.WHITE)
    
    content = sg.Text(
        text=content,
        background_color=colors.WHITE,
        text_color=colors.BLACK,
        justification='c',
        font=POPUP_CONTENT_FONT,
    )

    container = sg.Column(
        layout=[
            [title],
            [subtitle],
            [content],
            [CONTENT_BOTTOM_SEP]
        ],
        background_color=colors.WHITE,
        element_justification='c',
        vertical_alignment='c',
    )
    
    return container


def build_buttons_section(key):
    """Returns a container with the two buttons in a popup"""
    # space between this button and the next
    BUTTON_BOTTOM_SEP1 = fillers.horizontal_filler(1, colors.WHITE)
    
    continue_button = sg.Button(
        button_text=general.POPUP_BUTTON1_TEXT,
        button_color=(colors.WHITE, colors.DARK_GRAY),
        mouseover_colors=(colors.WHITE, colors.ORANGE),
        key=key,
        size=BUTTON_SIZE,
        font=POPUP_BUTTON_FONT
    )

    # space between this button and the bottom border
    BUTTON_BOTTOM_SEP2 = fillers.horizontal_filler(1, colors.WHITE)
    
    cancel_button = sg.Button(
        button_text=general.POPUP_BUTTON2_TEXT,
        button_color=(colors.WHITE, colors.DARK_GRAY),
        mouseover_colors=(colors.WHITE, colors.ORANGE),
        key=keys.RETURN_EVENT,
        size=BUTTON_SIZE,
        font=POPUP_BUTTON_FONT
    )
    
    container = sg.Column(
        layout=[
            [continue_button],
            [BUTTON_BOTTOM_SEP1],
            [cancel_button],
            [BUTTON_BOTTOM_SEP2]
        ],
        background_color=colors.WHITE,
        expand_x=True,
        element_justification='c'
    )
    
    return container
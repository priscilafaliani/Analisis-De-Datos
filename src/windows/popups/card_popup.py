"""A card pop up is built to show information about a card.

    It has 2 selection buttons, 'analyse' or 'cancel'.
    The windows is make in 3 sections:
        - The one that changes: 
        the content, the information. 
        - The one that doesn't. The icon, the theme.
        - The buttons, one of them has a given key,
        to recognize the result from this popup.
"""
import PySimpleGUI as sg

from src.globals import paths, keys, colors
from src.widgets import titlebar, fillers, button


# window constants
POPUP_BUTTON_SIZE = (35, 2)
POPUP_BUTTON1_TEXT = 'ANALIZAR'
POPUP_BUTTON2_TEXT = 'VOLVER ATRÁS'

# defines the width of the card 
SUBTITLE_SIZE = (50, None)

POPUP_TITLE_FONT = ('times', '20', 'bold')
POPUP_SUBTITLE_FONT = ('courier', 12, 'bold')
POPUP_CONTENT_FONT = ('courier', '12')
POPUP_BUTTON_FONT = ('times', 15)


def build(key, title, subtitle, content):
    """Returns a popup with the information given."""
    ttitlebar = titlebar.build()
    
    # space between icon and top border
    TOP_SEP = fillers.horizontal_filler(2, colors.WHITE)

    icon = sg.Image(
        filename=paths.POPUP_ICON,
        background_color=colors.WHITE,
    )
        
    popup_content = build_popup_content(title, subtitle, content)
    
    # space between content and buttons
    BOTTOM_CONTENT_SEP = fillers.horizontal_filler(2, colors.WHITE)
    
    buttons = build_buttons_section(key)
    
    # space between buttons and the bottom border
    BOTTOM_SEP = fillers.horizontal_filler(1, colors.WHITE)

    return sg.Window(
        title='',
        layout=[
            [ttitlebar],
            [TOP_SEP],
            [icon],
            [popup_content],
            [BOTTOM_CONTENT_SEP],
            [buttons],
            [BOTTOM_SEP]
        ],
        no_titlebar=True,
        keep_on_top=True,
        element_justification='c',
        background_color=colors.WHITE
    )


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
    
    # space between subtitle and content
    TOP_CONTENT_SEP = fillers.horizontal_filler(1, colors.WHITE)
    
    content = sg.Text(
        text=content,
        background_color=colors.WHITE,
        text_color=colors.BLACK,
        justification='c',
        font=POPUP_CONTENT_FONT,
    )
    
    return sg.Column(
        layout=[
            [title],
            [subtitle],
            [TOP_CONTENT_SEP],
            [content]
        ],
        background_color=colors.WHITE,
        element_justification='c',
        vertical_alignment='c',
    )


def build_buttons_section(key):
    """Returns a container with the two buttons in a popup"""
    
    analyse = button.build(
        POPUP_BUTTON1_TEXT,
        key,
        POPUP_BUTTON_FONT,
        POPUP_BUTTON_SIZE
    )
    
    # space between this buttons
    BUTTON_BOTTOM_SEP = fillers.horizontal_filler(1, colors.WHITE)
    
    cancel = button.build(
        POPUP_BUTTON2_TEXT,
        keys.RETURN_EVENT,
        POPUP_BUTTON_FONT,
        POPUP_BUTTON_SIZE
    )
    
    return sg.Column(
        layout=[
            [analyse],
            [BUTTON_BOTTOM_SEP],
            [cancel]
        ],
        background_color=colors.WHITE,
        expand_x=True,
        element_justification='c'
    )
import PySimpleGUI as sg

from src.globals import colors, paths, keys

def build(has_return=False):
    """Title bar with an exit button.
    
        Optional:
            has_return : boolean
            Adds a return button to the titlebar
    """
    return_button = None
    if has_return:
        return_button = sg.Column(
            layout=[
                [image_button(paths.RETURN_BUTTON_ICON, keys.RETURN_EVENT, 'Volver al menú anterior')]
            ], 
            background_color=colors.LIGHT_GRAY,
            element_justification='l',
            expand_x=True,
            grab=True
        )
        
    exit_button = sg.Column(
        layout=[
            [image_button(paths.EXIT_BUTTON_ICON, keys.EXIT_EVENT, 'Salir de la aplicación')]
        ], 
        background_color=colors.LIGHT_GRAY,
        element_justification='r',
        expand_x=True,
        grab=True
    )
    
    layout = []
    if return_button:
        layout.append(return_button)
    layout.append(exit_button)

    container = sg.Column(
        layout=[layout],
        vertical_alignment='c',
        element_justification='r',
        expand_x=True,
        background_color=colors.LIGHT_GRAY,
        grab=True
    )

    return container


def image_button(filepath, key, tooltip):
    """Returns a button with an icon for the titlebar.
    
        This button is only needed in this widget.
    """
    return sg.Button(
        image_filename=filepath,
        image_size=(18, 18),
        image_subsample=4,
        button_color=(colors.LIGHT_GRAY, colors.LIGHT_GRAY),
        border_width=0,
        key=key,
        pad=(10, 10),
        tooltip=tooltip
    )
from src.components import popup
import src.globals as g


def handle_popup(key):
    event, values = popup.pop(*g.POPUP_PARAMETERS[key])

    # the popup was for reddit, we need to decode
    # the value returned from the combobox and
    # show another popup
    if values and event != g.RETURN_EVENT:
        event = handle_popup(g.TEXT_TO_KEY[values[1]])

    return event
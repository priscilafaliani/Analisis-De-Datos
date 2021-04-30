import src.globals.keys as k
import src.globals.mappers as m

from src.components import popup


def handle_popup(key):
    event, values = popup.pop(*m.POPUP_PARAMETERS[key])

    # the popup was for reddit, we need to decode
    # the value returned from the combobox and
    # show another popup
    if values and event not in (k.RETURN_EVENT, k.EXIT_EVENT):
        event = handle_popup(m.TEXT_TO_KEY[values[1]])

    return event
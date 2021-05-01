from src.components import popup
from src.globals import keys, mappers


def handle_popup(key):
    event, values = popup.pop(*mappers.POPUP_PARAMETERS[key])

    # the popup was for reddit, we need to decode
    # the value returned from the combobox and
    # show another popup
    if values and event not in (keys.RETURN_EVENT, keys.EXIT_EVENT):
        event = handle_popup(mappers.TEXT_TO_KEY[values[1]])

    return event
from src.components import popup
from src.globals import keys, mappers


def handle_popup(key):
    event, values = popup.pop(*mappers.POPUP_PARAMETERS[key])

    if event in (keys.RETURN_EVENT, keys.EXIT_EVENT):
        return event

    # the popup was for reddit, we need to decode
    # the value returned from the combobox and
    # show another popup
    if values:
        event = handle_popup(mappers.TEXT_TO_KEY[values[1]])

    return event
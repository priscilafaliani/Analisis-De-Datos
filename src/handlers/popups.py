from src.components import popup
from src.globals import keys, mappers
from src.handlers.analysis import handle_analysis


def handle_popup(key):
    """Opens a popup based on a key and operates with results from it."""
    event, _values = popup.pop(*mappers.POPUP_PARAMETERS[key])

    # the user didn't wanted to make the analysis
    if event == keys.RETURN_EVENT:
        return
            
    # the user picked 'analyse'
    handle_analysis(event)

    return event
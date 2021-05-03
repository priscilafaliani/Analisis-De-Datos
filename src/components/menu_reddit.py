from src.globals import keys, mappers

from src.windows.menus import menu_reddit

from src.components import card_popup

from src.handlers.analysis import handle_analysis


def start():
    window = loop()
    window.close()
    
    
def loop():
    window = menu_reddit.build()
    
    while True:
        event, values = window.read()
        
        if event == keys.RETURN_EVENT:
            break
        
        window.hide()
    
        # tell the user about the option choosen
        event, _values = card_popup.pop(*mappers.POPUP_PARAMETERS[event])

        # the user didn't wanted to make the analysis
        if event != keys.RETURN_EVENT:
            handle_analysis(event)    
        
        window.un_hide()
        
    return window
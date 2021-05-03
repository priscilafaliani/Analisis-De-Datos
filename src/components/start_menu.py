from src.globals import keys, mappers

from src.windows.menus import start_menu

from src.components import card_popup
from src.components import menu_reddit

from src.handlers.analysis import handle_analysis


def start():
    window = loop()
    window.close()
    
    
def loop():
    window = start_menu.build()
    
    while True:
        event, _values = window.read()
        
        if event == keys.EXIT_EVENT:
            break
        
        window.hide()
        
        # if 'reddit' is choosen
        # menu_reddit window has to be shown
        if event == keys.REDDIT_KEY:
            menu_reddit.start()
        else:
            # tell the user about the option choosen
            event, _values = card_popup.start(*mappers.POPUP_PARAMETERS[event])

            # the user didn't wanted to make the analysis
            if event != keys.RETURN_EVENT:
                handle_analysis(event)            
            
        window.un_hide()
        
    return window
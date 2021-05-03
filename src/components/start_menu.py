from src.windows.menus import start_menu
from src.globals import keys

from src.components import card_popup
from src.components import menu_reddit

from src.handlers.popups import handle_popup
from src.handlers.analysis import handle_analysis


def start():
    window = loop()
    window.close()
    
    
def loop():
    window = start_menu.build()
    
    while True:
        event, values = window.read()
        
        if event == keys.EXIT_EVENT:
            break
        
        window.hide()
        
        # if 'reddit' is choosen
        # menu_reddit window has to be shown
        if event == keys.REDDIT_KEY:
            menu_reddit.start()
        else:
            # the others don't show a menu
            handle_popup(event)
            
        window.un_hide()
        
        
    return window
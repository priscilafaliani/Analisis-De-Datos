from src.windows import menu_reddit
from src.globals import keys

from src.handlers.popups import handle_popup
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
    
        handle_popup(event)
        
        window.un_hide()
        
    return window
from src.windows import menu
from src.globals import keys
from src.components import popup

from src.handlers.popups import handle_popup
from src.handlers.analysis import handle_analysis


def start():
    window = loop()
    window.close()
    
    
def loop():
    window = menu.build()
    
    while True:
        event, values = window.read()
        
        if event == keys.EXIT_EVENT:
            break
        
        window.hide()
        dataset_key = handle_popup(event)
        window.un_hide()
        
        if dataset_key not in (keys.RETURN_EVENT, keys.EXIT_EVENT):
            handle_analysis(dataset_key)
        
    return window
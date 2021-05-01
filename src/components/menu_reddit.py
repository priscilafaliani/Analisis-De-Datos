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
        
        if event in (keys.EXIT_EVENT, keys.RETURN_EVENT):
            break
        
        window.hide()
    
        # show the information popup
        dataset_key = handle_popup(event)
        
        if dataset_key == keys.EXIT_EVENT:
            break
        
        window.un_hide()
        
        # if the user selected 'analyse' then, make the analysis
        if dataset_key != keys.RETURN_EVENT:
            handle_analysis(dataset_key)
        
    return window
from src.windows import menu
from src.globals import keys

from src.components import popup
from src.components import menu_reddit

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
        
        # if 'reddit' is choosen
        # menu_reddit window has to be shown
        if event == keys.REDDIT_KEY:
            menu_reddit.start()
        else:
            # show the explanation popup
            dataset_key = handle_popup(event)
            
            # if the user selected 'analyse' then, make the analysis
            if dataset_key not in (keys.RETURN_EVENT, keys.EXIT_EVENT):
                handle_analysis(dataset_key)
        
        window.un_hide()
        
        
    return window
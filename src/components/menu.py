from src import globals as g

from src.windows import menu

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
        
        if event == g.EXIT_EVENT:
            break
        
        if (dataset_key := handle_popup(event)) not in (g.RETURN_EVENT, g.EXIT_EVENT):
            handle_analysis(dataset_key)
        
    return window
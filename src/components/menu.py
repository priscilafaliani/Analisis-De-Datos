from src import globals as g

from src.windows import menu

from src.components import popup

from src.handlers import life_pro_tips
from src.handlers import today_i_learned


def start():
    window = loop()
    window.close()
    
    
def loop():
    window = menu.build()
    
    while True:
        event, _values = window.read()
        
        if event == g.EXIT_EVENT:
            break
        
        if wants_to_analyse(event):
            start_analysis(event)
        
    return window


def wants_to_analyse(event):
    return popup.pop(*g.POPUP_PARAMETERS[event])


def start_analysis(event):
    if event == g.LPT_KEY:
        life_pro_tips.analyse()
    else:
        today_i_learned.analyse()
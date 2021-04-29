import src.globals as g
from src.windows import popup


def pop(title, subtitle, content):
    window = popup.build(title, subtitle, content)
    event, _values = window.read(close=True)
    return event == g.ANALYSE_EVENT
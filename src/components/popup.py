import src.globals as g
from src.windows import popup


def pop(key, title, subtitle, content, *choices):
    window = popup.build(key, title, subtitle, content, choices)
    return window.read(close=True)
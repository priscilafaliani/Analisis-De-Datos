from src.windows import card_popup


def pop(key, title, subtitle, content, *choices):
    window = card_popup.build(key, title, subtitle, content, choices)
    return window.read(close=True)
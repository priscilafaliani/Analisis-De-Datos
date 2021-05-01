from src.windows import card_popup


def pop(key, title, subtitle, content):
    window = card_popup.build(key, title, subtitle, content)
    return window.read(close=True)
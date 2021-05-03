from src.windows.popups import card_popup


def pop(key, title, subtitle, content):
    """Show the popup and return the values read."""
    return card_popup.build(key, title, subtitle, content).read(close=True)
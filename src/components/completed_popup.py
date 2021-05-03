from src.windows.popups import completed_popup


def start(filepath):
    """Show the popup and return the values read."""
    return completed_popup.build(filepath).read(close=True)
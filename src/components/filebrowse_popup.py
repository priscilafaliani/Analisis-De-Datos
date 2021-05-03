from src.windows.popups import filebrowse_popup


def start():
    """Show the popup and return the filepath entered."""
    event, values = filebrowse_popup.build().read(close=True)
    return values['-FOLDER-']
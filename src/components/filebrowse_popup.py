from src.windows.popups import filebrowse_popup


def start():
    window = filebrowse_popup.build()
    event, values = window.read(close=True)
    return values['-FOLDER-']
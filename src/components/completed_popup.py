from src.windows.popups import completed_popup


def start(filepath):
    return completed_popup.build(filepath).read(close=True)
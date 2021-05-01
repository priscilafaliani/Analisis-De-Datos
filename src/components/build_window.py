from src.windows import build_window


def start():
    window = build_window.build()
    event, values = window.read(close=True)
    return values['-FOLDER-']
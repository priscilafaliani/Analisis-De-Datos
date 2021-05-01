from src.windows import completed


def start(filepath):
    return completed.build(filepath).read(close=True)
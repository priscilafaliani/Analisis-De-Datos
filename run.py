from src.windows import start_window
from src.windows import popup
import src.globals as g


start_window.build().read(close=True)
popup.build(g.ELI5_CARD_TITLE, g.ELI5_CARD_SUBTITLE, g.ELI5_CONTENT).read(close=True)
popup.build(g.LPT_CARD_TITLE, g.LPT_CARD_SUBTITLE, g.LPT_CONTENT).read(close=True)

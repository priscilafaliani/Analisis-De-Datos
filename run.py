from src.windows import menu
from src.windows import popup
import src.globals as g


menu.build().read(close=True)
popup.build(g.TIL_CARD_TITLE, g.TIL_CARD_SUBTITLE, g.TIL_CONTENT).read(close=True)
popup.build(g.LPT_CARD_TITLE, g.LPT_CARD_SUBTITLE, g.LPT_CONTENT).read(close=True)

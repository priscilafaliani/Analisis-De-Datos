"""Used for mapping keys to their corresponding values.

    Watch the comments in each one to see when they are used.
    They basically help reducing code repetition.
"""
import src.globals.keys as k
import src.globals.paths as p
import src.globals.texts.hw_texts as hw_texts
import src.globals.texts.gs_texts as gs_texts
import src.globals.texts.st_texts as st_texts
import src.globals.texts.lpt_texts as lpt_texts
import src.globals.texts.reddit_texts as reddit_texts

from src.handlers import reddit, hello_world, game_sales


# used in handlers/popups when handling a popup
POPUP_PARAMETERS = {
    k.REDDIT_KEY: [k.REDDIT_KEY, reddit_texts.REDDIT_CARD_TITLE, reddit_texts.REDDIT_CARD_SUBTITLE, reddit_texts.REDDIT_CONTENT, st_texts.ST_CARD_TITLE, lpt_texts.LPT_CARD_TITLE],
    k.ST_KEY: [k.ST_KEY, st_texts.ST_CARD_TITLE, st_texts.ST_CARD_SUBTITLE, st_texts.ST_CONTENT],
    k.LPT_KEY: [k.LPT_KEY, lpt_texts.LPT_CARD_TITLE, lpt_texts.LPT_CARD_SUBTITLE, lpt_texts.LPT_CONTENT],
    k.HW_KEY: [k.HW_KEY, hw_texts.HW_CARD_TITLE, hw_texts.HW_CARD_SUBTITLE, hw_texts.HW_CONTENT],
    k.GS_KEY: [k.GS_KEY, gs_texts.GS_CARD_TITLE, gs_texts.GS_CARD_SUBTITLE, gs_texts.GS_CARD_CONTENT]
}

# used in handlers/popups to decode values returned by the combobox.
# they're only needed when the selected card was 'reddit'
TEXT_TO_KEY = {
    st_texts.ST_CARD_TITLE: k.ST_KEY,
    lpt_texts.LPT_CARD_TITLE: k.LPT_KEY
}

# used in handlers/analysis to call the correct analysis method
ANALYSIS_FUNCTIONS = {
    k.ST_KEY: (reddit.analyse, p.ST_PATH),
    k.LPT_KEY: (reddit.analyse, p.LPT_PATH),
    k.HW_KEY: (hello_world.analyse, p.HW_PATH),
    k.GS_KEY: (game_sales.analyse, p.GS_PATH)
}
"""Used for mapping keys to their corresponding values.

    Watch the comments in each one to see when they are used.
    They basically help reducing code repetition.
"""
import src.globals.keys as k
import src.globals.paths as p
import src.globals.texts.st_texts as st_texts
import src.globals.texts.lpt_texts as lpt_texts
import src.globals.texts.reddit_texts as reddit_texts
import src.globals.texts.museum_texts as museum_texts

from src.handlers import reddit, museum


# used in handlers/popups when handling a popup
POPUP_PARAMETERS = {
    k.REDDIT_KEY: [k.REDDIT_KEY, reddit_texts.REDDIT_CARD_TITLE, reddit_texts.REDDIT_CARD_SUBTITLE, reddit_texts.REDDIT_CONTENT, st_texts.ST_CARD_TITLE, lpt_texts.LPT_CARD_TITLE],
    k.ST_KEY: [k.ST_KEY, st_texts.ST_CARD_TITLE, st_texts.ST_CARD_SUBTITLE, st_texts.ST_CONTENT],
    k.LPT_KEY: [k.LPT_KEY, lpt_texts.LPT_CARD_TITLE, lpt_texts.LPT_CARD_SUBTITLE, lpt_texts.LPT_CONTENT],
    k.MUSEUM_KEY: [k.MUSEUM_KEY, museum_texts.MUSEUM_CARD_TILTE, museum_texts.MUSEUM_CARD_SUBTITLE, museum_texts.MUSEUM_CONTENT]
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
    k.MUSEUM_KEY: (museum.analyse, p.RIJKS_PATH)
}
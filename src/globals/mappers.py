"""Used for mapping keys to their corresponding values.

    Watch the comments in each one to see when they are used.
    They basically help reducing code repetition.
"""

from src.globals import keys, paths
from src.globals.texts import hw_texts, gs_texts
from src.globals.texts import reddit_texts, st_texts, lpt_texts

from src.handlers import reddit, hello_world, game_sales


# These are the parameters sent to create a popup
# when a button in a card, with one of these keys, is
# pressed.
POPUP_PARAMETERS = {
    keys.REDDIT_KEY: [
        keys.REDDIT_KEY, 
        reddit_texts.REDDIT_CARD_TITLE, 
        reddit_texts.REDDIT_CARD_SUBTITLE, 
        reddit_texts.REDDIT_CONTENT, 
        st_texts.ST_CARD_TITLE, 
        lpt_texts.LPT_CARD_TITLE
    ],
    keys.ST_KEY: [
        keys.ST_KEY, 
        st_texts.ST_CARD_TITLE, 
        st_texts.ST_CARD_SUBTITLE, 
        st_texts.ST_CONTENT
    ],
    keys.LPT_KEY: [
        keys.LPT_KEY, 
        lpt_texts.LPT_CARD_TITLE,
        lpt_texts.LPT_CARD_SUBTITLE, 
        lpt_texts.LPT_CONTENT
    ],
    keys.HW_KEY: [
        keys.HW_KEY, 
        hw_texts.HW_CARD_TITLE, 
        hw_texts.HW_CARD_SUBTITLE, 
        hw_texts.HW_CONTENT
    ],
    keys.GS_KEY: [
        keys.GS_KEY, 
        gs_texts.GS_CARD_TITLE, 
        gs_texts.GS_CARD_SUBTITLE, 
        gs_texts.GS_CARD_CONTENT
    ]
}


# Used in handlers/popups to decode values in the case
# where a popup has a combobox.
# The values returned by the combobox are the titles
# of the other popup which has to be opened.
TEXT_TO_KEY = {
    st_texts.ST_CARD_TITLE: keys.ST_KEY,
    lpt_texts.LPT_CARD_TITLE: keys.LPT_KEY
}


# Used in handlers/analysis to call the correct analysis function
# The 1st element in the tuple is the function and
# and the 2nd is the parameter needed.
# In this case: the path of the dataset to analyse.
ANALYSIS_FUNCTIONS = {
    keys.ST_KEY: (reddit.analyse, paths.ST_PATH),
    keys.LPT_KEY: (reddit.analyse, paths.LPT_PATH),
    keys.HW_KEY: (hello_world.analyse, paths.HW_PATH),
    keys.GS_KEY: (game_sales.analyse, paths.GS_PATH)
}
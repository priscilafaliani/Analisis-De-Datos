"""Used for mapping keys to their corresponding values.

    Watch the comments in each one to see when they are used.
    They basically help reducing code repetition.
"""

from src.globals import keys, paths
from src.globals import datasets_descriptions_texts

from src.handlers import lifeprotips, music, game_sales, programmer_humor


# These are the parameters sent to create a popup
# when a button in a card, with one of these keys, is
# pressed.
POPUP_PARAMETERS = {
    keys.REDDIT_KEY: [
        keys.REDDIT_KEY, 
        datasets_descriptions_texts.REDDIT_CARD_TITLE, 
        datasets_descriptions_texts.REDDIT_CARD_SUBTITLE, 
        datasets_descriptions_texts.REDDIT_CONTENT, 
        datasets_descriptions_texts.PH_CARD_TITLE, 
        datasets_descriptions_texts.LPT_CARD_TITLE
    ],
    keys.PH_KEY: [
        keys.PH_KEY, 
        datasets_descriptions_texts.PH_CARD_TITLE, 
        datasets_descriptions_texts.PH_CARD_SUBTITLE, 
        datasets_descriptions_texts.PH_CONTENT
    ],
    keys.LPT_KEY: [
        keys.LPT_KEY, 
        datasets_descriptions_texts.LPT_CARD_TITLE,
        datasets_descriptions_texts.LPT_CARD_SUBTITLE, 
        datasets_descriptions_texts.LPT_CONTENT
    ],
    keys.MUSIC_KEY: [
        keys.MUSIC_KEY, 
        datasets_descriptions_texts.MUSIC_CARD_TITLE, 
        datasets_descriptions_texts.MUSIC_CARD_SUBTITLE, 
        datasets_descriptions_texts.MUSIC_CONTENT
    ],
    keys.GS_KEY: [
        keys.GS_KEY, 
        datasets_descriptions_texts.GS_CARD_TITLE, 
        datasets_descriptions_texts.GS_CARD_SUBTITLE, 
        datasets_descriptions_texts.GS_CARD_CONTENT
    ]
}


# Used in handlers/analysis to call the correct analysis function
# The 1st element in the tuple is the function and
# and the 2nd is the parameter needed.
# In this case: the path of the dataset to analyse.
ANALYSIS_FUNCTIONS = {
    keys.PH_KEY: (programmer_humor.make_analysis),
    keys.LPT_KEY: (lifeprotips.make_analysis),
    keys.MUSIC_KEY: (music.make_analysis),
    keys.GS_KEY: (game_sales.make_analysis)
}
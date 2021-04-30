"""Contains all the paths used trought the app."""

import os.path

# ------ ICONS ------
ICONS_PATH = os.path.join('resources', 'icons')

POPUP_ICON = os.path.join(ICONS_PATH, 'chart.png')
EXIT_BUTTON_ICON = os.path.join(ICONS_PATH, 'exit.png')

ST_ICON = os.path.join(ICONS_PATH, 'ST.png')
LTP_ICON = os.path.join(ICONS_PATH, 'lpt.png')
REDDIT_ICON = os.path.join(ICONS_PATH, 'reddit.png')
HW_ICON = os.path.join(ICONS_PATH, 'programming.png')
GAMES_ICON = os.path.join(ICONS_PATH, 'games.png')

# ------ DATASETS ------
DATASETS_PATH = os.path.join('resources', 'datasets')

ST_PATH = os.path.join(DATASETS_PATH, 'reddit', 'Showerthoughts.csv')
LPT_PATH = os.path.join(DATASETS_PATH, 'reddit', 'LifeProTips.csv')
HW_PATH = os.path.join(DATASETS_PATH, 'programming languages', 'hello_world_in_all_languages.csv')
GS_PATH = os.path.join(DATASETS_PATH, 'games', 'vgsales.csv')
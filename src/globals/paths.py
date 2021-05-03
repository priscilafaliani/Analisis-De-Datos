"""Contains all the paths used trought the app."""

import os.path

# ------ ICONS ------
ICONS_PATH = os.path.join('resources', 'icons')

POPUP_ICON = os.path.join(ICONS_PATH, 'chart.png')

PH_ICON = os.path.join(ICONS_PATH, 'coding.png')
LTP_ICON = os.path.join(ICONS_PATH, 'lpt.png')
REDDIT_ICON = os.path.join(ICONS_PATH, 'reddit.png')

MUSIC_ICON = os.path.join(ICONS_PATH, 'music.png')

GAMES_ICON = os.path.join(ICONS_PATH, 'games.png')

# ------ DATASETS ------
DATASETS_PATH = os.path.join('resources', 'datasets')

PH_PATH = os.path.join(DATASETS_PATH, 'reddit', 'ProgrammerHumor.csv')
LPT_PATH = os.path.join(DATASETS_PATH, 'reddit', 'LifeProTips.csv')

MUSIC_PATH = os.path.join(DATASETS_PATH, 'music', 'music.csv')

GS_PATH = os.path.join(DATASETS_PATH, 'games', 'vgsales.csv')
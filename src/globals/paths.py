"""Contains all the paths used trought the app."""

import os.path

# ------ ICONS ------
ICONS_PATH = os.path.join('resources', 'icons')

POPUP_ICON = os.path.join(ICONS_PATH, 'chart.png')
EXIT_BUTTON_ICON = os.path.join(ICONS_PATH, 'exit.png')

ST_ICON = os.path.join(ICONS_PATH, 'ST.png')
LTP_ICON = os.path.join(ICONS_PATH, 'lpt.png')
REDDIT_ICON = os.path.join(ICONS_PATH, 'reddit.png')
MUSEUM_ICON = os.path.join(ICONS_PATH, 'museum.png')

# ------ DATASETS ------
DATASETS_PATH = os.path.join('resources', 'datasets')

ST_PATH = os.path.join(DATASETS_PATH, 'reddit', 'Showerthoughts.csv')
LPT_PATH = os.path.join(DATASETS_PATH, 'reddit', 'LifeProTips.csv')
RIJKS_PATH = os.path.join(DATASETS_PATH, 'rijksmuseum', 'rijksmuseum.csv')

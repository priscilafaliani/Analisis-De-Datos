import csv

from src.globals.paths import MUSIC_PATH
from src.handlers.writer import write_to_json

COMPOSER_INDEX = 1
COMPOSITION_INDEX = 2
MOVEMENT_INDEX = 3
SECONDS_INDEX = 8


def make_analysis(output_filepath):
    """Does all the work needed to complete the analysis.
    
        In this case, it makes one thing:
            - Writes to a json file.

    """
    analysis_results = analyse()
    write_to_json(analysis_results, output_filepath)


def analyse():
    """Obtains the top 10 shortest Beethoven compositions"""
    with open(file=MUSIC_PATH, mode='r', encoding='utf-8') as f:
        reader = csv.reader(f)

        print(next(reader))
        bach = filter(lambda composition: composition[COMPOSER_INDEX] == 'Bach', reader)

        ordered = sorted(bach, key=lambda composition: composition[SECONDS_INDEX])
    
    return [
        {
            'Composicion': ordered[i][COMPOSITION_INDEX],
            'Movimiento': ordered[i][MOVEMENT_INDEX],
            'Segundos': ordered[i][SECONDS_INDEX]
        }
        for i in range(10)
    ]
import csv

from src.globals.paths import GS_PATH
from src.handlers.writer import write_to_json

NAME_INDEX = 1
YEAR_INDEX = 3
GENRE_INDEX = 4
SALES_INDEX = -1


def make_analysis(output_filepath):
    """Does all the work needed to complete the analysis.
    
        In this case, it makes one thing:
            - Writes to a json file.

    """
    analysis_results = analyse()
    write_to_json(analysis_results, output_filepath)


def analyse():
    """Obtains the top 10 sales games from the 2000 or less."""
    with open(file=GS_PATH, mode='r', encoding='utf-8') as f:
        reader = csv.reader(f)

        # Header.
        print(next(reader))
        
        # get the games published in 2000 or less and order them by sales
        # some games don't have a year
        filtered_games = sorted(
            filter(lambda game: game[YEAR_INDEX] != 'N/A' and int(game[YEAR_INDEX]) <= 2000, reader), 
            key=lambda game: float(game[SALES_INDEX]),
            reverse=True
        )

    return [
        {
            'Nombre': filtered_games[i][NAME_INDEX], 
            'Genero': filtered_games[i][GENRE_INDEX], 
            'Ventas': filtered_games[i][SALES_INDEX], 
            'Anio': filtered_games[i][YEAR_INDEX]
        } for i in range(10)
    ]
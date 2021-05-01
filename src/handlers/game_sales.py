import csv


NAME_INDEX = 1
YEAR_INDEX = 3
GENRE_INDEX = 4
SALES_INDEX = -1

def analyse(filepath):
    """Obtains the top 10 sales games from the 2000 or less."""
    with open(file=filepath, mode='r', encoding='utf-8') as f:
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
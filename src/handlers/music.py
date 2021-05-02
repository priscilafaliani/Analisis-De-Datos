import csv

COMPOSER_INDEX = 1
COMPOSITION_INDEX = 2
MOVEMENT_INDEX = 3
SECONDS_INDEX = 8

def analyse(filepath):
    """Obtains the top 10 shortest Beethoven compositions"""
    with open(file=filepath, mode='r', encoding='utf-8') as f:
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
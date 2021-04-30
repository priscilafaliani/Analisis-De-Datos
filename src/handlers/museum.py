import csv
import os.path
import collections
import requests


OBJECT_TITLE_INDEX = 2
OBJECT_TYPE_INDEX = 3
OBJECT_ARTIST_INDEX = 4
OBJECT_CREATION_DATE_INDEX = 5
OBJECT_IMAGE_INDEX = 6


def analyse(filepath):
    """Obtains the 10 oldest paintings in this museum."""
    with open(file=filepath, mode='r', encoding='utf-8') as f:
        reader = csv.reader(f)

        print(next(reader))

        # prent -> print, painting
        # some paintings come without date and image
        # i don't want those :(
        paintings = sorted(
            filter(
                lambda p: p[OBJECT_TYPE_INDEX] == 'prent' and p[OBJECT_CREATION_DATE_INDEX] and p[OBJECT_IMAGE_INDEX], 
                reader
            ), 
            key=lambda painting: painting[OBJECT_CREATION_DATE_INDEX]
        )

    paintings = [paintings[i] for i in range(15)]
    
    # gets the img files.
    get_images(paintings)

    # returns for json writing
    return paintings


def get_images(paintings):
    print(len(paintings))
    for painting in paintings:
        try:
            img = requests.get(painting[OBJECT_IMAGE_INDEX])

            with open(file=f'{os.path.join("resources", "output", painting[OBJECT_TITLE_INDEX].replace(" ", ""))}.jpg', mode='wb') as f:
                f.write(img.content)
        except requests.exceptions.RequestException as e:
            print('Invalid URL.')
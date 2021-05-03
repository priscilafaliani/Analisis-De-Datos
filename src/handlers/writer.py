"""Module used to write analysis results to files."""
import requests
import json


def write_to_json(results, output_filepath):
    """Writes the result of an analysis to a json file."""
    with open(file=output_filepath + '.json', mode='w', encoding='utf-8') as f:
        json.dump(results, f)


def write_images(url_list, output_filepath):
    """Receives a list with images url, and saves them to files."""
    img_number = 0
    for url in url_list:
        try:
            image = requests.get(url)
            # get the file extension
            extension = url[-3:]
            write_image(f'{output_filepath}{img_number}.{extension}', image.content)
            img_number += 1
        except requests.exceptions.RequestException:
            print('Invalid request')


def write_image(filepath, image):
    with open(file=filepath, mode='wb') as f:
        f.write(image)
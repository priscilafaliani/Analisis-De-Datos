import csv
import requests

from src.globals.paths import PH_PATH
from src.handlers.writer import write_to_json, write_images

TITLE_COLUMN_INDEX = 2
UPVOTES_COLUMN_INDEX = 7
ULR_INDEX = 6

VALID_EXTENSIONS = ('png', 'jpg')


def make_analysis(output_filepath):
    """Does all the work needed to complete the analysis.
    
        In this case, it makes two things:
            - Writes to a json file.
            - Saves image.
    """
    analysis_results = analyse()
    write_to_json(analysis_results, output_filepath)
    write_images(get_images_urls(analysis_results), output_filepath)


def analyse():
    """Returns the images of the top 10 posts from the subreddit.

        Only cares about the posts with images.
    """
    with open(file=PH_PATH, mode='r', encoding='utf-8') as f:
        reader = csv.reader(f)
        
        # Header.
        print(next(reader))
        
        posts_with_images = filter(lambda post: post[ULR_INDEX].endswith(VALID_EXTENSIONS), reader)

        sorted_posts = sorted(posts_with_images, key=lambda post: post[UPVOTES_COLUMN_INDEX], reverse=True)

    # now get the top 10
    return [
        {
            'Titulo': sorted_posts[i][TITLE_COLUMN_INDEX],
            'Upvotes': sorted_posts[i][UPVOTES_COLUMN_INDEX],
            'URL': sorted_posts[i][ULR_INDEX]
        } 
        for i in range(10)
    ]


def get_images_urls(posts):
    """Returns a list of all the urls in the list of posts."""
    return [post['URL'] for post in posts]
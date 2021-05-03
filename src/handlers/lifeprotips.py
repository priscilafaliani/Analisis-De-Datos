import csv

from src.globals.paths import LPT_PATH
from src.handlers.writer import write_to_json


TITLE_INDEX = 2
FLAIR_INDEX = 3
TEXT_INDEX = 4
UPVOTES_INDEX = 7


def make_analysis(output_filepath):
    """Does all the work needed to complete the analysis.
    
        In this case, it makes one thing:
            - Writes to a json file.

    """
    analysis_results = analyse()
    write_to_json(analysis_results, output_filepath)


def analyse():
    """Returns the 10 most upvoted subreddit posts with the flair 'computers'."""
    with open(file=LPT_PATH, mode='r', encoding='utf-8') as f:
        reader = csv.reader(f)
        
        # Header.
        print(next(reader))
        
        computer_posts = filter(lambda post: post[FLAIR_INDEX] == 'Computers', reader)
        ordered_posts = sorted(computer_posts, key=lambda post: post[UPVOTES_INDEX], reverse=True)

    return [
        {
            'Titulo': ordered_posts[i][TITLE_INDEX],
            'Upvotes': ordered_posts[i][UPVOTES_INDEX],
            'Contenido': ordered_posts[i][TEXT_INDEX]
        } 
        for i in range(10)
    ]


def clear_format(posts):
    """Receives the list of data analyzed and
        prepares it to be written to a json file.
    """
    return list(map(lambda post: {'Title': post[0][0], 'Content': post[0][1], 'Score': post[1]}, posts))
import csv
import collections
import src.globals as g


TITLE_COLUMN_INDEX = 2
TEXT_COLUMN_INDEX = 4
UPVOTES_COLUMN_INDEX = 7


def analyse(filepath):
    """Returns the 10 most upvoted subreddit posts."""
    with open(file=filepath, mode='r', encoding='utf-8') as f:
        reader = csv.reader(f)
        
        # Header.
        print(next(reader))
        
        posts = collections.Counter()
        for post in reader:
            key = (post[TITLE_COLUMN_INDEX], post[TEXT_COLUMN_INDEX])
            posts[key] = int(post[UPVOTES_COLUMN_INDEX])
        
    return clear_format(posts.most_common(10))


def clear_format(posts):
    """Receives the list of data analyzed and
        prepares it to be written to a json file.
    """
    return list(map(lambda post: {'Title': post[0][0], 'Content': post[0][1], 'Score': post[1]}, posts))
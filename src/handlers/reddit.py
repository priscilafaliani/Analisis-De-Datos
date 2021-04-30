import csv
import collections
import src.globals as g


DOMAIN_COLUMN_INDEX = 2
TITLE_COLUMN_INDEX = 4
UPVOTES_COLUMN_INDEX = 5
TEXT_COLUMN_INDEX = 9


def analyse(filepath):
    """Returns the 10 most upvoted subreddit posts."""
    # with open(file=filepath, mode='r', encoding='utf-8') as f:
    #     reader = csv.reader(f)
        
    #     # Header.
    #     next(reader)
        
    #     posts = collections.Counter()
    #     for post in reader:
    #         key = (post[TITLE_COLUMN_INDEX], post[TEXT_COLUMN_INDEX])
    #         posts[key] = int(post[UPVOTES_COLUMN_INDEX])
        
    # return posts.most_common(10)

    print(filepath)
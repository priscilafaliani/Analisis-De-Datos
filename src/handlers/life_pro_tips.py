import csv
import collections
import src.globals as g


DOMAIN_COLUMN_INDEX = 2
TITLE_COLUMN_INDEX = 4
UPVOTES_COLUMN_INDEX = 5
TEXT_COLUMN_INDEX = 9


def analyse():
    """Returns the 10 (sort of) most upvoted tips."""
    
    
    with open(file=g.LPT_PATH, mode='r', encoding='utf-8') as lpt:
        reader = csv.reader(lpt)
        print(next(reader))
        
        posts = collections.Counter()
        for post in reader:
            key = (post[TITLE_COLUMN_INDEX], post[TEXT_COLUMN_INDEX])
            posts[key] = int(post[UPVOTES_COLUMN_INDEX])
        
        print(posts.most_common(10))
        
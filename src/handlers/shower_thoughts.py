import csv
import src.globals as g


def analyse():
    with open(file=g.TIL_PATH, mode='r', encoding='utf-8') as til:
        reader = csv.reader(til)
        
        print(next(reader))
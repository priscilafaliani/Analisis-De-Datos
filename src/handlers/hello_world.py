import csv
import os.path
import collections

EXT_INDEX = 2
NAME_INDEX = 1
PROG_INDEX = 3

def analyse(filepath):
    """Obtains 'hello world' for languanges with extension .c, .py o .asm"""
    with open(file=filepath, mode='r', encoding='utf-8') as f:
        reader = csv.reader(f)

        print(next(reader))
        
        filtered_ext = [
            {
                'Language Name': program[NAME_INDEX], 
                'Program': program[PROG_INDEX], 
                'ext': program[EXT_INDEX]
            } 
            for program in filter(lambda lang: lang[EXT_INDEX] in ('asm', 'c', 'py'), reader)
        ]
        
    return filtered_ext
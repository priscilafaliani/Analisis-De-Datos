import os
import os.path
import json
import src.globals.mappers as m

from src.components import build_window, completed

def handle_analysis(key):
    """Executes an analysis in a dataset.
    
        The dataset and the analysis to make are mapped
        in another file, to the key received.

        The mapping returns the function to execute and
        the paremeters it needs.

        Finally, writes the results to a json file with
        name '<key>_analysis.json'
    """
    func, params = m.ANALYSIS_FUNCTIONS[key]

    # get filepath to save the file
    filepath = build_window.start()
    if not filepath:
        filepath = os.getcwd()
    filepath = os.path.normpath(f'{os.path.join(filepath, key.replace("-", ""))}_analysis.json')

    # make the analysis
    results = func(params)

    # write to file
    write_to_json(results, filepath)

    # show the "completed" message
    completed.start(filepath)


def write_to_json(results, output_filepath):
    with open(file=output_filepath, mode='w', encoding='utf-8') as f:
        json.dump(results, f)
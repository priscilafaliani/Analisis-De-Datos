import json
import src.globals.mappers as m


def handle_analysis(key):
    """Executes an analysis in a dataset.
    
        The dataset and the analysis to make is mapped
        in another file, to the dataset key received.

        The mapping returns the function to execute and
        the paremeters it needs.

        Finally, writes the results to a json file with
        a name '<key>_analysis.json'
    """
    func, params = m.ANALYSIS_FUNCTIONS[key]
    results = func(params)
    write_to_json(results, f'{key.replace("-", "")}_analysis.json')


def write_to_json(results, output_filepath):
    with open(file=output_filepath, mode='w', encoding='utf-8') as f:
        json.dump(results, f)
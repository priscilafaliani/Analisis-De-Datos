import os.path

from src.globals import mappers
from src.components import filebrowse_popup, completed_popup


def handle_analysis(key):
    """Manages all the functions calls to make an analysis.
    
        The dataset and the analysis to make are mapped
        in another file, to the key received.

        The mapping returns the function to execute.

        This handler gives the function the filename
        where to save the analysis.
    """
    make_analysis = mappers.ANALYSIS_FUNCTIONS[key]
    filepath = get_filepath_to_write(key)
    make_analysis(filepath)
    completed_popup.start(filepath)


def get_filepath_to_write(key):
    """Returns the filepath where the analysis is to be saved."""
    filepath = filebrowse_popup.start()

    # get the default ouput folder
    if not filepath:
        filepath = os.path.join(os.getcwd(), 'output')

    # join the path with the filename
    filepath = f'{os.path.join(filepath, key.replace("-", ""))}_analysis'
    
    # has to be normalized bc os.getcwd() scares me
    return os.path.normpath(filepath)

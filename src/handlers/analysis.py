import src.globals.mappers as m


def handle_analysis(key):
    func, params = m.ANALYSIS_FUNCTIONS[key]
    func(params)
import src.globals as g


def handle_analysis(key):
    func, params = g.ANALYSIS_FUNCTIONS[key]
    func(params)
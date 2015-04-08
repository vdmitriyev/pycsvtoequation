# coding: utf-8
#!/usr/bin/env python

__credits__ = ['Viktor Dmitriyev']
__license__ = '?'
__version__ = '1.1.0'
__status__  = 'dev'
__date__    = '08.04.2015'
__description__ = 'CSV to LaTeX converter'

import config as config
from helper import save_equation, read_csv

def csv_to_latex(csv_data):
    """
        (str) -> None

        Continuesly interating csv data and saving as LaTeX or MathML
    """
    #context = config.LATEX_CSV_DATA_PATTERN
    #context = config.MATHML_CSV_DATA_PATTERN
    context = config.MATHJAX_CSV_DATA_PATTERN
    
    for index, row in enumerate(csv_data):
        save_equation(row, index, context, separate_equations=True)

def main():
    # processing data
    csv_data = read_csv(config.DATA_FOLDER + '//' + config.CSV_FILE)
    csv_to_latex(csv_data)

if __name__ == '__main__':
    main()
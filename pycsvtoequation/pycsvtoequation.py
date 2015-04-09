# coding: utf-8
#!/usr/bin/env python

__credits__ = ['Viktor Dmitriyev']
__license__ = '?'
__version__ = '1.2.0'
__status__  = 'dev'
__date__    = '08.04.2015'
__description__ = 'CSV to Equation converter'

import config as config
from helper import save_equation, read_csv

def main():
    """
        (Nonen) -> None

        Converting math equation from CSV to human readble following formats:
            -   LaTeX
            -   MathML
            -   MathJax
    """

    # slecting proper contex
    # for more details check config.py

    #context = config.LATEX_CONTEXT
    #context = config.MATHML_CONTEXT
    context = config.MATHJAX_CONTEXT
    csv_file = context['MapppingCSVToLatex']['CSVFileName']['value']

    # reading data from CSV
    csv_data = read_csv(config.DATA_FOLDER + '//' + csv_file)

    # conveting to human readable equation
    #csv_to_equation(csv_data, context)


    for index, row in enumerate(csv_data):
        save_equation(row, index, context)
 
if __name__ == '__main__':
    main()
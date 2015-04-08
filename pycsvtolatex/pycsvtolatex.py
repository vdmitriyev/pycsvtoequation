# coding: utf-8
#!/usr/bin/env python

__credits__ = ['Viktor Dmitriyev']
__license__ = '?'
__version__ = '1.0.0'
__status__  = 'dev'
__date__    = '08.04.2015'
__description__ = 'CSV to LaTeX converter'

from helper import save_tex, read_csv

def csv_to_latex(csv_data):

    # setting the row number 
    csv_data_pattern = {
                        'TargetNamePrefix' : 'OriginalTests',
                        'PathToTemplate': 'template.tex',
                        'OutputType': 'latex',
                         'MapppingCSVToLatex': {
                            'OriginalEquation' : 0, 
                            'CustomSolution' : 1, 
                            'IsCorrectCustomSolution': 3,
                            'SympySolution' : 4, 
                            'IsCorrectSympySolution' : 5,
                            'expected': 6,
                            'IsEqualCustomToSympy': 7,
                            }
                        }

    # csv_data_pattern = {
    #                     'TargetNamePrefix' : 'OriginalTests',
    #                     'PathToTemplate': 'template.html',
    #                     'OutputType': 'mathml',
    #                      'MapppingCSVToLatex': {
    #                         'OriginalEquation' : 0, 
    #                         'CustomSolution' : 1, 
    #                         'IsCorrectCustomSolution': 3,
    #                         'SympySolution' : 4, 
    #                         'IsCorrectSympySolution' : 5,
    #                         'expected': 6,
    #                         'IsEqualCustomToSympy': 7,
    #                         }
    #                     }


    for index, row in enumerate(csv_data):
        save_tex(row, index, csv_data_pattern, separate_equations=True)

def main():

    # processing data
    csv_data = read_csv('data/sympy-tests - Original tests.csv')
    csv_to_latex(csv_data)

if __name__ == '__main__':
    main()
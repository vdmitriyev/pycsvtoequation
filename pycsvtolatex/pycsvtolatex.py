# coding: utf-8
#!/usr/bin/env python

__credits__ = ['Viktor Dmitriyev']
__license__ = '?'
__version__ = '1.0.0'
__status__  = 'dev'
__date__    = '08.04.2015'
__description__ = 'CSV to LaTeX converter'


import csv
from helper_dir import save_tex

def read_csv(csv_file, delimiter=',', quotechar='"'):
    """
        (str, str, str) -> (list)

        Reading CSV data from specified file
    """

    data = list()
    with open(csv_file, 'rb') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=delimiter, quotechar=quotechar)
        for row in csvreader:
            data.append(row)

    return data

def csv_to_latex(csv_data):

    # setting the row number 
    csv_data_pattern = {
                        'TargetNamePrefix' : 'OriginalTests',
                        'PathToTemplate': 'template.tex',
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

    for index, row in enumerate(csv_data):
        save_tex(row, index, csv_data_pattern, separate_equations=True)

def main():

    # processing data
    csv_data = read_csv('data/sympy-tests - Original tests.csv')
    csv_to_latex(csv_data)

if __name__ == '__main__':
    main()
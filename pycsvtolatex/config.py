# coding: utf-8

# setting path to sympy
# it's enough if you just git clone it and set the path to git's folder
SYMPY_PATH = 'c:\\github\\mathapp\\master\\'

# setting configs for CSV to Latex
LATEX_CSV_DATA_PATTERN = {
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

# setting configs for CSV to MathML
MATHML_CSV_DATA_PATTERN = {
                    'TargetNamePrefix' : 'OriginalTests',
                    'PathToTemplate': 'template.html',
                    'OutputType': 'mathml',
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
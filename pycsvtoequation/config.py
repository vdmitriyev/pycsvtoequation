# coding: utf-8

# data configs
DATA_FOLDER = 'data'
CSV_FILE = 'sympy-tests - diff-2015-04-09.csv'

# setting path to sympy
# it's enough if you just git clone it and set the path to git's folder
SYMPY_PATH = 'c:\\github\\mathapp\\master\\'

# Mapping CSV fields for processing
MAPPING_CSV  = {
                'CSVFileName' : {
                    'value': CSV_FILE,
                    'type': 'path'
                },
                'OriginalEquation' : {
                    'index': 0,
                    'type': 'equation'
                },
                'CustomSolution' : {
                        'index': 1, 
                        'type': 'equation'
                },
                'IsCorrectCustomSolution': {
                    'index': 3,
                    'type' : 'text'
                    },
                'SympySolution' : {
                    'index': 4, 
                    'type': 'equation'
                },
                'IsCorrectSympySolution' : {
                    'index' : 5,
                    'type': 'text'
                },
                'expected': {
                    'index' : 6,
                    'type': 'text'
                },
                'IsEqualCustomToSympy': {
                    'index' :   7,
                    'type': 'text'
                    }
                }

#################
# CONTEXTS
#################

# setting configs for CSV to Latex
LATEX_CONTEXT = {
                'TargetNamePrefix' : 'OriginalTests',
                'PathToTemplate': 'template-latex.tex',
                'OutputType': 'latex',
                'MapppingCSVToLatex': MAPPING_CSV
                }


# setting configs for MathML
MATHML_CONTEXT = {
                    'TargetNamePrefix' : 'OriginalTests',
                    'PathToTemplate': 'template-mathml.html',
                    'OutputType': 'mathml',
                    'MapppingCSVToLatex': MAPPING_CSV
                    }

# setting configs for MathML
MATHJAX_CONTEXT = {
                    'TargetNamePrefix' : 'OriginalTests',
                    'PathToTemplate': 'template-mathjax.html',
                    'OutputType': 'mathjax',
                    'MapppingCSVToLatex': MAPPING_CSV
                    }
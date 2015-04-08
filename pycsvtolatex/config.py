# coding: utf-8

# data configs
DATA_FOLDER = 'data'
CSV_FILE = 'sympy-tests - Original tests.csv'

# setting path to sympy
# it's enough if you just git clone it and set the path to git's folder
SYMPY_PATH = 'c:\\github\\mathapp\\master\\'

# setting configs for CSV to Latex
LATEX_CSV_DATA_PATTERN = {
                    'TargetNamePrefix' : 'OriginalTests',
                    'PathToTemplate': 'template-latex.tex',
                    'OutputType': 'latex',
                    'MapppingCSVToLatex': {
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
                    }

# setting configs for CSV to MathML
MATHML_CSV_DATA_PATTERN = {
                    'TargetNamePrefix' : 'OriginalTests',
                    'PathToTemplate': 'template-mathml.html',
                    'OutputType': 'mathml',
                    'MapppingCSVToLatex': {
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
                    }

# setting configs for CSV to MathML
MATHJAX_CSV_DATA_PATTERN = {
                    'TargetNamePrefix' : 'OriginalTests',
                    'PathToTemplate': 'template-mathjax.html',
                    'OutputType': 'mathjax',
                    'MapppingCSVToLatex': {
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
                    }
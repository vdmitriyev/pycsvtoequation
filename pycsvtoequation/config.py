# coding: utf-8

# data configs
DATA_FOLDER = 'data'
CSV_FILE = 'sympy-tests - diff-2015-04-09.csv'
TEMPLATES_FOLDER = 'templates'

# setting path to sympy
# it's enough if you just git clone it and set the path to git's folder
SYMPY_PATH = 'c:\\github\\mathapp\\master\\'

# Mapping CSV fields for processing
MAPPING_CSV_DIFF  = {
                'CSVFileName' : {
                    'value': CSV_FILE,
                    'type': 'config'
                },
                'TargetNamePrefix' : {
                    'value': 'diff',
                    'type': 'config'
                },
                'TemplatePrefix' : {
                    'value': 'diff',
                    'type': 'config'
                },
                'OriginalEquation' : {
                    'index': 0,
                    'type': 'equation'
                },
                'CustomSolution' : {
                        'index': 4, 
                        'type': 'equation'
                },
                'IsCorrectSolutionCustom': {
                    'index': 5,
                    'type' : 'text'
                    },
                'SympySolution' : {
                    'index': 2, 
                    'type': 'equation'
                },
                'IsCorrectSolutionSympy' : {
                    'index' : 3,
                    'type': 'text'
                },
                'expected': {
                    'index' : 1,
                    'type': 'equation'
                }
                # ,
                # 'IsEqualCustomToSympy': {
                #     'index' :   7,
                #     'type': 'text'
                #     }
                }

##########################################
#
# CONTEXTS 
# note - just change above values properly
#
##########################################

# setting configs for CSV to Latex
LATEX_CONTEXT = {
                'PathToTemplate': '{0}/{1}-template-latex.tex'.format(TEMPLATES_FOLDER,
                                                                      MAPPING_CSV_DIFF['TemplatePrefix']['value']),
                'OutputType': 'latex',
                'MapppingCSVToLatex': MAPPING_CSV_DIFF
                }

# setting configs for MathML
MATHML_CONTEXT = {
                'PathToTemplate': 
                    '{0}/{1}-template-mathml.html'.format(TEMPLATES_FOLDER,
                                                          MAPPING_CSV_DIFF['TemplatePrefix']['value']),
                'OutputType': 'mathml',
                'MapppingCSVToLatex': MAPPING_CSV_DIFF
                }

# setting configs for MathML
MATHJAX_CONTEXT = {
                'PathToTemplate': 
                    '{0}/{1}-template-mathjax.html'.format(TEMPLATES_FOLDER, 
                                                           MAPPING_CSV_DIFF['TemplatePrefix']['value']),
                'OutputType': 'mathjax',
                'MapppingCSVToLatex': MAPPING_CSV_DIFF
                }
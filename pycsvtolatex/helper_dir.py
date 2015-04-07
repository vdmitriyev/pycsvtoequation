# coding: utf-8
#!/usr/bin/env python

__credits__ = ['Viktor Dmitriyev']
__license__ = '?'
__version__ = '1.3.0'
__status__  = 'dev'
__date__    = '08.04.2015'
__description__ = 'Directory helper to manage folder for TEX'

import os
import codecs
import imp

# importing sympy module located in parent folder
# NOTE that the original sympy should be removed from system
# if othet sympy won't be removed, they will be used instead
import sys
sys.path.insert(0, 'c:\\github\\mathapp\\master\\')

# sympy package
from sympy import *
from sympy.utilities.solution import *

x = Symbol('x')
y = Symbol('y')

# constants
TEX_BAT_FILE_NAME = '_latex.bat'
PY_BAT_FILE_NAME = 'run-solver.bat'

def to_template(solution, csv_data_pattern):
    """
    (list, dict) -> str

        Reading LaTeX template and replacing values inside from ones send.

    """

    _template = read_file(csv_data_pattern['PathToTemplate'])

    for mapping in csv_data_pattern['MapppingCSVToLatex']:
        index_field = csv_data_pattern['MapppingCSVToLatex'][mapping]
        value = solution[index_field]

        # some work arround to execute fetched formula for proper conversion
        try:
            code_to_execute = 'expression = {0}'.format(value)
            exec code_to_execute
            value = latex(expression)
        except:
            value = solution[index_field]
            pass

        # replacing template's default value with fetched one
        _template = _template.replace(mapping, value)
    
    return _template

def save_tex(solutions, index, csv_data_pattern, separate_equations=False):
    """
        (list, str) -> None

        Saving solution as TEX file
    """

    # identifying the name of current python file
    #equation_name = os.path.basename(py_file_name)[:-3]
    equation_name = csv_data_pattern['TargetNamePrefix']

    # creating the folder for tex file
    create_directory(equation_name)
    tex_file_name = '{0}/{1}.tex'.format(equation_name, equation_name + '-' + str(adjust(index)))
    save_file(tex_file_name, to_template(solutions, csv_data_pattern))

    # some info output
    print '[i] tex saved into "{}"'.format(tex_file_name)


def create_directory(directory):
    """
        (str) -> None

        Creating following artifacts on demand:
            - directory;
            - windows bat script for compiling latex;
            - windows bat script for running particular solution test;
    """

    if not os.path.exists(directory):
        os.makedirs(directory)
        print '[i] created folder "{}"'.format(directory)

        create_tex_bat(directory + '\\' + TEX_BAT_FILE_NAME, directory)
        print '[i] created bat "{0}/{1}"'.format(directory, TEX_BAT_FILE_NAME)

        # create_py_bat(directory + '\\' + PY_BAT_FILE_NAME, directory)
        # print '[i] created bat "{0}/{1}"'.format(directory, PY_BAT_FILE_NAME)
    # else:
    #     print '[i] already existing folder "{}"'.format(directory)

def create_tex_bat(file_name, tex_name):
    """
        (str) -> None

        Creating windows bat file with commands TEX
    """

    output = '@echo off\n'
    output += 'echo "Removing old PDF"\n'
    output += 'rm {}.pdf\n'.format(tex_name)

    output += '\necho "Compiling LaTex to PDF. Please, wait ..."\n'

    # output += 'pdflatex {}.tex\n'.format(tex_name)
    # output += 'pdflatex {}.tex\n'.format(tex_name)

    output += 'for %%t in (*.tex) do (\n'
    output += '\t\techo "Compiling file " %%t\n'
    output += '\t\tpdflatex %%t\n'
    output += '\t\tpdflatex %%t\n'
    output += ')\n'

    output += '\necho "Deleting unnecessary files ..."\n'
    output += 'del *.log\n'
    output += 'del *.aux\n'

    output += '\necho "Opening generated PDF\n'
    output += 'call {}.pdf\n'.format(tex_name)

    save_file(file_name, output)

def create_py_bat(file_name, tex_name):
    """
        (str) -> None

        Creating windows bat file with commands for python
    """

    output = '@echo off\n'
    output += 'cd ..\n'
    output += 'popd .\n'
    output += 'python {0}.py > {0}/run-solver-output.txt\n'.format(tex_name)
    output += 'pushd .\n'
    output += '\necho "Check run-solver-output.txt for output details\n"'

    save_file(file_name, output)

def save_file(file_name, text, encoding='utf-8'):
    """
        (obj, str, str, str) -> None

        Save to 'file_name' given 'text'.
    """

    _file = codecs.open(file_name, 'w', encoding)
    _file.write(text)
    _file.close()

def read_file(file_name):
    """
        (str) -> (str)

        Reads text from 'file_name' and return it
    """

    with open(file_name, 'r') as file_input:
        file_content = file_input.read()
    return file_content

def adjust(number, max_len=3):
    """
        (int, int) -> (str)

        Adjusting number
    """
    return  (max_len - len(str(number))) * '0' + str(number)



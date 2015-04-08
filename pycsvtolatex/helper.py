# coding: utf-8
#!/usr/bin/env python

__credits__ = ['Viktor Dmitriyev']
__license__ = '?'
__version__ = '1.5.0'
__status__  = 'dev'
__date__    = '08.04.2015'
__description__ = 'Directory helper to manage folder for TEX'

import os
import csv
import codecs

# importing sympy module located in parent folder
# NOTE that the original sympy should be removed from system
# if the sympy won't be removed, they will be used instead
import sys
import config as config
sys.path.insert(0, config.SYMPY_PATH)

# printers
from sympy.printing.latex import LatexPrinter
from sympy.printing.mathml import MathMLPrinter, mathml
from sympy.utilities.mathml import *

# sympy package
from sympy import *
from sympy.utilities.solution import *

x = Symbol('x')
y = Symbol('y')
z = Symbol('z')


# constants
TEX_BAT_FILE_NAME = '_latex.bat'
PY_BAT_FILE_NAME = 'run-solver.bat'

def to_template(row, context, printer):
    """
    (list, dict) -> str

        Reading template and replacing values inside from ones send.

    """

    result = read_file(context['PathToTemplate'])

    for mapping in context['MapppingCSVToLatex']:
        field = context['MapppingCSVToLatex'][mapping]
        value_index = field['index']
        value_type = field['type']
        value = row[value_index]

        # some work arround to execute fetched formula for proper conversion
        if value_type == 'equation':
            try:
                code_to_execute = 'expression_own = {0}'.format(str(value))
                exec code_to_execute
                value = printer._print(expression_own)

                # when context points to mathml
                if context['OutputType'] == 'mathml':
                    value = value.toprettyxml()
                    value = c2p(value, simple=True)
            except Exception, ex:
                print '[x] exception: {0}'.format(str(ex))
                print '[i] exception at value: {0}'.format(str(value))
                value = row[value_index]

        # replacing template's default value with fetched one
        result = result.replace(mapping, str(value))
    
    return result

def save_equation(solutions, index, context, separate_equations=False):
    """
        (list, str) -> None

        Saving solution as LaTex or MathML file
    """

    # identifying the name of current python file
    #equation_name = os.path.basename(py_file_name)[:-3]
    equation_name = context['TargetNamePrefix']

    # creating the folder for tex file
    create_directory(equation_name)

    if context['OutputType'] in ('latex'):
        printer = LatexPrinter()
        extension = '.tex'
    elif context['OutputType'] == 'mathml':
        printer = MathMLPrinter()
        extension = '.html'
    elif context['OutputType'] == 'mathjax':
        printer = LatexPrinter()
        extension = '.html'
    else:
        print '[e] UNKNOWN type of output, set "latex", "mathml" or "mathjax"'
        return

    _file_name = '{0}/{1}{2}'.format(equation_name, equation_name + '-' + str(adjust_number(index)), extension)
    
    
    save_file(_file_name, to_template(solutions, context, printer))

    # some info output
    print '[i] {0} saved into "{1}"'.format(context['OutputType'], _file_name)


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


def adjust_number(number, max_len=3):
    """
        (int, int) -> (str)

        Adjusting number
    """

    return  (max_len - len(str(number))) * '0' + str(number)



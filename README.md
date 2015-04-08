### About

Simple python script that converts list of equations from csv file to separate latex file with further compilation to pdfs.

### Dependencies

* [Python 2.7](https://www.python.org/download/releases/2.7/)
* [Miktex](http://miktex.org/) or other LaTeX package
* [Sympy](https://github.com/sympy/sympy)

### Usage

Check ```config.py```, ```csvtolatex.py``` files and apply your own configurations. For changin templates check ```template.tex``` and ```template.html```. Change path to your 'Sympy' package in ```config.py``` (it's used for generating proper LaTeX, MathML or MathJax). Put your data into data folder in csv format. Run main script:
```
python csvtolatex.py
```
Naviagate to the create folder and compile all LaTeX file to the pdfs.

### Problems
Note that [MathML](http://www.w3.org/Math/) will not work in [Google Chrome](http://www.cnet.com/news/google-subtracts-mathml-from-chrome-and-anger-multiplies/).

### Credits
* Viktor Dmitriyev
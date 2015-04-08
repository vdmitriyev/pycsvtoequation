### About

Simple python script that converts list of equations from csv file to separate latex file with further compilation to pdfs.

### Dependencies

* Python 2.7
* Miktex

### Usage

Check ```csvtolatex.py``` and ```template.tex``` files and apply your own configurations. Change path to your 'Sympy' package in ```helper_dir.py``` (it's used for generating proper LaTeX). Put your data into data folder in csv format. Run main script:
```
python csvtolatex.py
```
Naviagate to the create folder and compile all LaTeX file to the pdfs.

### Problems
Note that [MathML](http://www.w3.org/Math/) will not work in [Google Chrome](http://www.cnet.com/news/google-subtracts-mathml-from-chrome-and-anger-multiplies/).

### Credits
* Viktor Dmtiriyeb


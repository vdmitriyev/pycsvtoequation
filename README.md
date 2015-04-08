### About

Simple python script that converts list of equations from csv file into separate LaTeX, MathML or MathJax files. The best working option for now is MathJax.

### Dependencies

* [Python 2.7](https://www.python.org/download/releases/2.7/)
* [Miktex](http://miktex.org/) or other LaTeX package
* [Sympy](https://github.com/sympy/sympy)

### Usage

Check ```config.py```, ```csvtolatex.py``` files and apply your own configurations. For changing templates check ```template.tex``` and ```template.html```. Change path to your 'Sympy' package in ```config.py``` (it's used for generating proper LaTeX, MathML or MathJax). Put your data into data folder in csv format. Run main script:
```
python csvtolatex.py
```
or 
```
python csvtolatex.py > output-log.txt
```
Naviagate to the create folder, if necessary compile all LaTeX file into pdfs and view them, or just use browser to view generated html with MathML or MathJax.

### Known Problems

* Note that [MathML](http://www.w3.org/Math/) will not work in [Google Chrome](http://www.cnet.com/news/google-subtracts-mathml-from-chrome-and-anger-multiplies/).
* While using MathML, the processing can be stopped unexpectedly due to some internal error. 
* While rendering pdf from Latex with batch script, note that the script can stop unexpectedly due to some LaTeX formatting error, just press enter and go on. Note that rendering can last for a while.

### Credits

* Viktor Dmitriyev
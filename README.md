### About

Simple python script that converts list of equations from CSV file into separate human-readable equations by meand of LaTeX, MathML or MathJax. The best working option currently is MathJax.

### Dependencies

* [Python 2.7](https://www.python.org/download/releases/2.7/)
* [Miktex](http://miktex.org/) or other LaTeX package
* [Sympy](https://github.com/sympy/sympy)

### Usage

Check ```config.py```, ```pycsvtoequation.py``` files and apply your own configurations. For changing templates check ```template-latex.tex```, ```template-mathjax.html``` or ```template-mathml.html```. Change path to your 'Sympy' package in ```config.py``` (it's used for generating proper LaTeX, MathML or MathJax). Put your data into data folder in csv format. Run main script:
```
python pycsvtoequation.py
```
or 
```
python pycsvtoequation.py > output-log.txt
```
Naviagate to the create folder, if necessary compile all LaTeX file into pdfs and view them, or just use browser to view generated html with MathML or MathJax.

### Known Problems

* Note that [MathML](http://www.w3.org/Math/) will not work in [Google Chrome](http://www.cnet.com/news/google-subtracts-mathml-from-chrome-and-anger-multiplies/).
* While using MathML, the processing can be stopped unexpectedly due to some internal error. 
* While rendering pdf from Latex with batch script, note that the script can stop unexpectedly due to some LaTeX formatting error, just press enter and go on. Note that rendering can last for a while.
* During the rendefing process, the equation that are in form of **'a = x**(1 / 4)'** are interpreted by Sympy or Python wrongly. Division is applied and **x** is ommited completely, such behaviour results in having only **1** as equation to render.

### Credits

* Viktor Dmitriyev
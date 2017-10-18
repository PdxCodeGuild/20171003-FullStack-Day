
# Docstrings

Docstrings are used to provide documentation of source code. Docstrings help those reading the code to better understand what each part means.

Docstrings are defined by triple-quoted strings, you can use single- or double-quoted strings. Check out [PEP 257](https://www.python.org/dev/peps/pep-0257/) for docstring conventions. Docstrings always immediately follow the part of code to which they pretain.

```python
"""this is the module's docstring"""

x = 5
"""this is a variable's docstring"""

def add(a, b):
    """this is a function's docstring"""
    return a + b

class MyClass(object):
    """this is the class's docstring"""

    def my_method(self):
        """this is the method's docstring"""
```

**Variable** docstrings should describe what the variable represents and how it should be used.

**Module** docstrings should start at the very top of the file, and should list all variables, functions, and classes within the module, with a brief summary for each.

**Package** docstrings (`__init__.py`) should contain a list of modules contained in it.

**Function** and **method** docstrings should provide a brief explanation of what operation the function performs. It should list all the parameters and what each parameter represents. It should also describe what it returns.


```python
def add(a, b):
    """ 
    add two numbers and return the result
    :param a: the first number to add
    :param b: the second number to add
    :return: the sum of the first number and the second number
    """
```

**Class** docstrings should describe what the class represents and list all attributes and methods of the class. 






### `help()`, `__doc__` and `pydoc`

Docstrings can be used with the built-in function `help()`. Pass whatever python variable, function, module, class, etc, into `help` to see its docstring. You can read more about the help function in the [official docs](https://docs.python.org/3.6/library/functions.html#help). You can then access the docstring using the object's `__doc__` attribute.

```python
help(add)
print(add.__doc__)

import os
help(os)
```

`pydoc` is a documentation-buidling package built into the core python library.
 
 
- View documentation in the terminal:  `python -m pydoc <module name>`

- Generate HTML: `python -m pydoc -w <module name>`

For example, try running `python -m pydoc -w os`. You can read more about pydoc in the [official docs](https://docs.python.org/3.6/library/pydoc.html).

### Doctests



### Sphinx

[Sphinx](http://www.sphinx-doc.org/en/stable/index.html) is a program which can generate documentation in HTML and PDFs from Python source code. You can find a tutorial [here](http://www.sphinx-doc.org/en/stable/tutorial.html). Sphinx allows for two ways of formatting docstrings: [google-style](http://www.sphinx-doc.org/en/stable/ext/example_google.html) and [numpy-style](http://www.sphinx-doc.org/en/stable/ext/example_numpy.html#example-numpy).



### Epydoc

[Epydoc](http://epydoc.sourceforge.net/) is another documentation-generator. It uses [Epytext](http://epydoc.sourceforge.net/epytextintro.html) which is a simple markup language for formatting docstring text.

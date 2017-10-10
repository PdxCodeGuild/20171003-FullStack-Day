
# Python Overview

For more information, check out the [Python Language Reference](https://docs.python.org/3/reference/index.html#reference-index) and [Python Standard Library](https://docs.python.org/3/library/index.html). The [wikipedia article](https://en.wikipedia.org/wiki/Python_(programming_language)) offers a decent overview.



## Keywords

- if, elif, else
- for, while
- continue, break
- is
- in
- def, return, lambda
- class
- import, from, as
- raise, try, except, finally
- with
- pass
- del
- global
- assert


## Common Built-in Types

For all the built-in types, check the [official docs](https://docs.python.org/3.2/library/stdtypes.html).

- int: integer number
- float: floating-point number
- string: text
- boolean: true or false
- list: an ordered list of elements
- set: an unordered collection of unique elements
- dictionary: a collection of name-value pairs
- None: represents a variable without a value


## Common Built-in Functions

For all the built-in functions, check the [official docs](https://docs.python.org/3/library/functions.html)


- I/O
    - input() prompts the user for input on the terminal
    - print() displays text to the user on the terminal
- Arithmetic Functions
    - abs() returns the absolute value of a number
    - round() rounds a number, an optional second argument can specify how many decimal places the output should have
    - min() returns the minimum of the values passed to it
    - max() returns the maximum of the values passed to it
    - sum() returns the sum of the values passed to it
- Type Conversion
    - int() converts a value to an int
    - float() converts a value to a float
    - str() converts a value to a string
    - chr() converts an int to a string containing the character with that unicode value, for example `chr(97)` returns the string 'a'
    - bool() converts a value to a boolean
    - list() converts a value to a list
    - tuple() converts a value to a tuple
    - set() converts a value to a set
    - dict() converts a value to a dict
- List Operations
    - len() returns the length of a list
    - sorted() sorts a list
    - reversed() reverses a list



## Common Built-in modules

- math: additional math functions like cos, sin, 
- decimal: more advanced floating point arithmetic
- random: generate random numbers
- datetime, time, calendar: working with dates and times
- re: regular expressions
- os, os.path: file operations
- itertools, functools: advanced operations on iterables and functions
- collections: data structures
- csv: csv file parsing



## Common Non-built-in Modules

These can be installed using `pip install <module>`.

- [Pillow](https://python-pillow.org/): image manipulation
- [Requests](http://requests.readthedocs.io/en/master/): http requests
- [Twisted](http://twistedmatrix.com/trac/): networking engine
- [Scrapy](https://scrapy.org/), [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/): web scraping
- [nltk](http://www.nltk.org/): natural language processing
- [NumPy](http://www.numpy.org/): advanced mathematics
- [SciPy](https://www.scipy.org/): scientific computing
- [PyGame](http://www.pygame.org/news.html): game framework
- [matplotlib](http://matplotlib.org/): 2D/3D plotting
- [TkInter](https://wiki.python.org/moin/TkInter), [wxPython](https://www.wxpython.org/), [PyQT](https://sourceforge.net/projects/pyqt/), [PyGTK](https://wiki.python.org/moin/PyGtk): GUI

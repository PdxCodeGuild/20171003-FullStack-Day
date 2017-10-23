
# Using Functions

Functions are isolated pieces of code that take input, perform some operation, and return a result. Functions we've used so far include `input()`, `print()`, `len()`, etc. Python provides many built-in functions for you to use. For all the built-in functions, check the [official docs](https://docs.python.org/3/library/functions.html)


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

## Parameters and Return-Values

Parameters are the values passed to a function, enclosed inside the parantheses. Some functions take no parameters, some like `min` and `print` take an arbitrary number of parameters. Functions may also take **named parameters**. For example, the `print` function can take a named parameter `end`. When not specified, `end` will default to `\n`. This is useful if you want to print multiple things on the same line.

```python
print('hello ', end='')
print('there')
```

Functions may or may not return anything. If they don't return anything, any variables they're assigned to will be `None`.

```python
x = print('hello!')
print(x)
>>> None
```

Generally, if they do not return anything, they'll edit the object that they're called on, or the parameters they're passed.

```python
fruits = ['apple', 'banana', 'pear']
x = fruits.append('cherry')
print(x)
print(fruits)
>>> None
>>> ['apple', 'banana', 'pear', 'cherry']
```

Functions on classes are called methods. Methods are a special type of function: all methods are functions, not all functions are methods. Some examples of methods include `list.append()` and `string.split()`. Note that you also have a `.` before a function if it's contained in a module. For example `random.randint()` and `math.sin()`, however these are not methods.

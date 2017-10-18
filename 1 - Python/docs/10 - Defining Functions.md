
# Defining Functions

We can define our own functions using the `def` keyword. This allows us to execute sections of code repeatedly.

```python
def say_hello():
    print('hello!')

say_hello()
say_hello()
say_hello()

>>> hello!
>>> hello!
>>> hello!
```

The function above takes no parameters and returns no values. You can specify parameters by listing variables in the parantheses of the function definition.


## Parameters

```python
def say_hello(first_name, last_name):
    print('Hello ' + first_name + ' ' + last_name)

fn = input('what is your first name? ')
ln = input('what is your last name? ')
say_hello(fn, ln)
```

Notice that the variable names outside the function don't have to match the variable names inside the function. When the values are passed as parameters, they take on new names, local only to the function.

### Passing by Position

Thus far, we’ve been passing arguments to functions **by position.** The values at the call site are bound to the variables in the function signature _in order._

```python
def subtract(a, b):
  return a - b

subtract(5, 8)  #> -3
# a = 5; b = 8
```

### Optional Arguments

Most positional arguments are like the above, **required arguments.** But it’s also possible to have functions that take **optional arguments.** If they are specified when the function is called, then the caller’s value is used. Otherwise, the default value from the function definition is used.

```python
def subtract(a, b=1):
  return a - b

subtract(5)  #> 4
# a = 5; b = 1

subtract(5, 8)  #> -3
# a = 5; b = 8
```

### Passing by Keyword

Optional arguments may also be passed **by keyword** _in any order,_ as long as they come after all positional arguments.

```python
def subtract(a, b=1, c=0):
  return a - b - c

subtract(5, b=8)  #> -3
# a = 5; b = 8; c = 1

subtract(5, c=9)  #> -5
# a = 5; b = 1; c = 9

subtract(5, c=9, b=8)  #> -12
# a = 5; b = 8; c = 9
```

### \*args & \*\*kwargs

When reading more advanced Python code, you might see functions written like the following:

```python
def print_movie_ratings(username, *args, **kwargs):
    """Update the user’s ratings for movies.
    Update movies from *args that are keys in **kwargs.
    """
    for arg in args:  # Loop through the tuple `args`
        if arg in kwargs:  # Loop through keys of the `kwargs` dictionary
            print(arg, kwargs[arg])

print_movie_ratings('segdeha', 'Sharknado', 'Frozen', 'Transformers', Sharknado=3, Frozen=2, Fargo=5)

""" Output is:
Sharknado 3
Frozen 2
"""
```

This syntax is used to create functions that can take a varying number of arguments.

_Note: The special thing about these variable names isn’t `args` and `kwargs`. It’s the `*` and `**`. You can name these arguments anything that’s a legal variable name, but by convention they’re named `*args` and `**kwargs`._

Within the function above, `*args` is defined as a tuple of the positional arguments passed to the function that don’t have explicit names in our function signature. `**kwargs` is defined as a dictionary of any keyword arguments passed to the function that don’t match keywords in the function signature. You can find more information about both [here](http://www.saltycrane.com/blog/2008/01/how-to-use-args-and-kwargs-in-python/).



## Returning

We can also return values from a function, which is often the result of some computation or operation. The code below returns the lesser of two values.

```python
def min(a, b):
    if a < b:
        return a
    return b
x = min(5, 2)
print(x)
>>> 2
```

Notice we don't need an `else`, once a the interpreter reaches a `return`, it immediately exits a function.

```python
if condition:
    return a
else:
    return b

#better written as...
if condition:
    return a
return b
```

### Returning Multiple Values

You can return multiple values using **automatic tuple packing and unpacking**.


```python
def get_dimensions():
    return 500, 200

width, height = get_dimensions()
print(width)
print(height)

>>> 500
>>> 200
```

## Recursion

Functions can call other functions, producing a chain of invocation. Functions can even call themselves, this is called **recursion**. It's important to have a 'stop condition', otherwise this results in infinite recursion and you'll get a 'stack overflow'.

```python
def factioral(n):
    if n == 0:
        return 1
    return n*factorial(n-1)
```



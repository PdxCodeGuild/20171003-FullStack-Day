# Exception Handling

Exceptions are 'thrown' by Python when it can't interpret what your program is trying to do. You can read more about exeptions in the [official docs](https://docs.python.org/3.6/tutorial/errors.html).

For example, the following occurs when we attempt to concatenate a string an an int (e.g. `print('your age is: ' + 23)`)

    Traceback (most recent call last):
        MORE FUNCTIONS...
        File "test.py", line 1, in <module>
    TypeError: cannot concatenate 'str' and 'int' objects

Python supports the following 5 types of errors (by default, you can create your own!):

* `NameError` — no variable or function known by that name
* `ValueError` — a value you’re using doesn’t make sense in the context
* `TypeError` — you're using the wrong type
* `SyntaxError` — your Python is written incorrectly
* `KeyError` — the key you’re trying to access is not present in the dictionary

An elegant way to make your program more robust is to ‘catch’ thrown errors using what’s called a `try`/`except` block.

```python
try:
    this_wont_work = 1 + 'hello'
except TypeError:
    print('That didn’t work!')
```

A common exception you might want to handle is when you try to access a key that doesn’t exist in a dictionary.

```python
my_dict = {'foo':'bar'}
try:
    my_value = my_dict['baz']
except KeyError:
    print('Try again!')
```

Another use-case is checking if the user entered a valid integer:

```python
while True:
    try:
        x = int(input('enter a number: '))
        break
    except ValueError:
        print('try again')
print(x)
```


You can also leave the type of exception absent, which will catch all exceptions.

```python
try:
    # some stuff
except: # catch anything!
    # handle error
```


If you want to catch multiple exceptions, use a tuple.

```python

```
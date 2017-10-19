
# Running Python via the CLI

## Common Python Commands

You can find more info in the [official docs](https://docs.python.org/3/using/cmdline.html).


- `python` start the interactive interpreter
- `python <file>` execute the python source code in the given file
- `python --help` print out all command-line options
- `python --version` show which version of python you're using

## Using the Python Interactive Interpreter

When you download and install Python, what you are getting is a Python interpreter. This interpreter is what reads and performs the code that you will write. There are two ways to use the interpreter: by running it on its own as an interactive shell, or by having it run a file that has python code in it.

Let's start with the interpreter, as that allows us to run code one line at a time. This way we can see what happens every step of the way

Open a terminal and type `python`, you should see a welcome message, and be left with `>>>`. This is Python's interactive shell. So long as we type in valid Python code, it will execute every line of code we give it. Try using it as a calculator, as seen in the example below, and see what you get.

```
>>> 5 + 3
8
>>> 4*(5+1)+8
32
```

## Expressions

Both `5 + 3` and `4*(5+1)+8` are examples of Python expressions. Expressions can be defined as any statement (or piece of code) that can be evaluated by Python into a single value. In this case `5 + 3` evaluates to `8`, and `4*(5+1)+8` to `32`.

Even just `4` can be an expression, as it can be evaluated to... `4`. In this way, expressions can be very simple, or *very* complicated, so long as it can be resolved to a single value.

## Data types

But what is meant by a *single value*? Values can take many different forms, called data types, and not all of them are numbers as we got above.

Here is a non-exhaustive list of the more common data types:

1. Integers:

   Integers (ints) are simply whole numbers like `2` or `-39`. In some programming languages there is a limit as to how large integers can be, but in Python they can be as large as we'd like. `238401283873042950840985739749218436542355` is a perfectly valid int.

2. Floating-point:

   Floating-point values (floats) are numbers with a decimal point, such as `2.6` or `-6.948202`. Floats can also be as large as we like, but there is a limit to its precision.

3. Strings:

   Strings are any string of text, like so: `"Hello there!"`. Strings are denoted and will be kept separate from the rest of your code with either single `'` or double `"` quotes. Empty strings can be created by not putting anything between the quotes like `''` or `""`

   Try adding strings together in the interpreter just like you would add numbers. `'Good' + 'morning'` is a valid expression just like `2 + 2` is.

4. Booleans:

   Probably the most simple type, they can be either `True` or `False`. Booleans are used for comparing values and logic. For instance, typing the expression `3 > 2` into the interpreter would evaluate into the boolean `True`

5. Lists:

   Lists are values that can contain multiple values within them. They denoted with square brackets like this `[2, 2.5, "Hello again!", 2]`. As shown, they can not only contain multiple values, but multiple types of values as well. Any kind of data type can be used inside a list, even another list! `["A list inside a list!", [1, 3, 5], "Its quite strange"]`

   Lists are a bit more complicated to use than the other types above, but we'll get into that later.

Before we continue we should note that, from Python's point of view, integers are a different kind of value than floats. Even if they look like the same kind of thing to us, computers have to store these two things in its memory in different ways.

Similarly, `'2'` is not the same as `2`. One of these is stored as a string, the other as a number. We can convert between the two, but until we convert them they will be treated differently by the interpreter.

## Variables

We can let names stand for values, like in algebra.

```
>>> x = 5
>>> x = x + 3
>>> x
8
```

To exit the python interpreter, type `exit()` or `quit()`


## Executing Python Source Files

You can execute python code saved in a plain text file by typing `python filename`. Create a new file `temp.py` with the following contents:

```
x = 5
x = x + 3
print(x)
```

Execute this file by opening a terminal, and type `python temp.py`. You should see `8` as the output. Every time you edit the source file, you then run it by typing `python filename` again.


### Passing Command-Line Arguments

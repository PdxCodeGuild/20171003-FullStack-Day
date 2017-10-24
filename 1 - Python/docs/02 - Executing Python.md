
# Running Python via the CLI

## Common Python Commands

You can find more info in the [official docs](https://docs.python.org/3/using/cmdline.html).


- `python` start the interactive interpreter
- `python <file>` execute the python source code in the given file
- `python --help` print out all command-line options
- `python --version` show which version of python you're using

## Using the Python Interactive Interpreter

When you download and install Python, what you are getting is a Python interpreter. This interpreter is what reads and performs the code that you will write. There are two ways to use the interpreter: by running it on its own as an interactive shell, or by having it run a file that has Python code in it.

Let's start with the interactive interpreter, as that allows us to run code one line at a time. This way we can see what happens every step of the way

Open a terminal and type `python`, you should see a welcome message, and be left with `>>>`. This is Python's interactive shell. So long as we type in valid Python code, it will execute every line of code we give it. Try using it as a calculator, as seen in the example below, and see what you get. To exit the python interpreter at any point, type `exit()` or `quit()`

```
>>> 5 + 3
8
>>> 4*(5+1)+8
32
```

## Expressions

Both `5 + 3` and `4*(5+1)+8` are examples of Python expressions. Expressions are any statement (or piece of code) that can be evaluated by Python into a single value. In this case `5 + 3` evaluates to `8`, and `4*(5+1)+8` to `32`.

Even just `4` can be an expression, as it can be evaluated to... `4`. In this way, expressions can be very simple, or *very* complicated, so long as it can be successfully resolved to a single value.

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

   Lists are values that can contain multiple values within them. They denoted with square brackets like this `[2, 2.5, "Hello again!", 2]`. As shown, they can not only contain multiple values, but multiple types of values as well. Any kind of data type can be used inside a list, even another list! `["A list inside a list!", [1, 3, 5], "Its quite miraculous"]`

   Lists are a bit more complicated to use than the other types above, but we'll get into that later.

Before we continue we should note that, from Python's point of view, integers are a different kind of value than floats. Even if they look like the same kind of thing to us, computers have to store these two things in its memory in different ways.

Similarly, `'2'` is not the same as `2`. One of these is stored as a string, the other as a number. We can convert between the two, but until we convert them they will be treated differently by the interpreter.

## Variables

Just like algebra, we can create variables to stand in for values. The syntax for this is `[variable_name] = [expression]`. The interpreter will create a variable with the name you give it, evaluate the expression, then set that variable to whatever the expression evaluated to. You can use almost any combinations of numbers and letters for the name, but variable names must start with a letter or an underscore, and are case sensitive.

Here is a simple example of working with variables. Try typing it into your interpreter to see what happens, then try creating and using your own variables.

```
>>> x = 5
>>> x = x + 3
>>> x
8
```

So, in the first line we are creating a variable named `x` which is being set to `5`. In the second line, we are setting the value of x again, this time to `x + 3`. The interpreter will evaluate that statement by first retrieving the value of `x` at that moment, which is still `5`, then adds `3` to that. Thus, `x + 3` becomes `5 + 3`, and `x` is now set to that value. To confirm, typing in just `x` in the last line gives us back `8`, the value that is now in `x`


## Executing Python Source Files

As our programs become more complex, it is going to be more and more of a hassle to put everything line by line into the interpreter. Let's look at another method of running Python code. Start by creating a text file named `temp.py` and put this code inside it:

```
x = 5
x = x + 3
print(x)
```

You can now run the contents of the file from the terminal by navigating to where your file was saved and typing in `python temp.py`. You should then see `8` printed to your terminal. Try changing the code in your file, saving it, and running it in your terminal again. This is how you can save, edit, and run code contained in files on your computer.

To run a different file, just give python a different file name to run, like so `python [file_name]`


# Variables and I/O

Variables are names given to pieces of data. These allow us to specify the operations we'd like to perform on that data in our source code.

## Literals

The easiest way to enter data in your problem is through 'literals', which are called as such because they're *literally* written in the source code.

- int literals: `3`, `-20`, `294927`
- float literals: `3.2`, `3.14e-10`
- bool literals: `True` and `False`
- string literals: `'hello'` and `"world"`


## Mutability

Certain datatypes in Python are **immutable** meaning their values **cannot** be changed. Immutable types include ints, floats, strings, and tuples. This is why string methods like `lower`, `replace` and `strip` return **copies** of the string rather than the original. 


```python
x = 5
y = x
y += 2
print(x) # 5
print(y) # 7

x = ['apples', 'bananas', 'pears']
y = x
y.append('cherries')
print(x) # ['apples', 'bananas', 'pears', 'cherries']
print(y) # ['apples', 'bananas', 'pears', 'cherries']
```


## I/O

### Print

Print is a function in python that allows us to print text to the terminal. Each call to `print` results in a new-line.

```python
print('hello')
print('world')
>>> hello
>>> world
```
You can specify a different terminating character, if you don't want it to print a new-line.

```python
print('hello', end=' ')
print('world')
>>> hello world
```

If you pass multiple arguments (separated by commas), it'll print them on a single line.
```python
print("Total score for", name, "is", score)
```

If you want to specify a different separator character (space is default), you can write something like:

```python
print("Total score for ", name, " is ", score, sep='')
```


### Input

The `input` function allows us to prompt the user for input on the terminal. The string that's passed to it determines what's displayed with the prompt.

```python
name = input('what is your name? ')
print('Hello', name, '!')
>>> what is your name? Joe
>>> Hello Joe!
```






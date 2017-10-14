
# Strings

Strings represent text in Python. Strings in Python are encoded in Unicode, which means their reach extends far beyond ASCII. You can use Chinese characters, Arabic characters, and more. For more information about unicode support, look [here](https://docs.python.org/3.6/howto/unicode.html).

To define a string literal, you can enclose text in either single-quotes or double-quotes, but you should stay consistent. You can use single-quotes inside a string enclosed in double-quotes and vice-versa. According to the Pep8 specification, you should use single-quotes.

```python
s = 'hello world!'
print(s)
```

### Escape Sequences

Escape sequences allow us to define special characters within strings.

- `\'` allows you to have a single quote inside a string enclosed in single quotes
- `\"` allows you to have a double-quote inside a string enclosed in double-quotes
- `\n` represents a new-line
- `\t` represents a tab
- `\\` represents a backslash
- `\xhhhh` represents a unicode character with id 'hhhh', e.g. `\u0394`


### String Operations

Remember that strings are **immutable** meaning their values cannot be changed. Each of these operations returns a **new** string.

- `+`, `+=` concatenation
- `*`, `*=` repeat a string
- `[i]` get the character at index i
- `[a:b]` get the sub-string from a to b
- `[a:b:c]` get every `c`th character from a to b
- `find()` returns the index of a the first occurance of a string
- `upper()` convert to upper case
- `lower()` convert to lower case
- `startswith()` returns true if the string starts with the given string
- `endswith()` returns true if the string ends with the given string
- `replace()` replaces one string with another
- `strip()` moves leading and trailing characters
- `split()` splits a string into a list
- `join()` combines the elemnts of a list into a string

None of these functions edit the original string, because strings are immutible. If they return strings, they return **copies**. Sometimes people new to programming will make a mistake such as...

```python
s = ' Hello! '
s.lower()
s.strip()
print(s) # ' Hello! ', original value is unchanged
```




### Formatting

Often string concatenation with large strings or many variables becomes overwhelming. You can see some examples [here](https://pyformat.info/).

**c-style formatting**
```python
'%s %s' % ('one', 'two')
'%d %d' % (1, 2)

mylist = [1,2,3]
print("A list: %s" % mylist)
```



```python
'{} {}'.format('one', 'two')
'{} {}'.format(1, 2)
```

**f-strings** are prefixed with an `f`, one can then use curly braces `{}` and write variable names.


```python
>>> a = 'one'
>>> b = 2
>>> print(f'a is {a} and b is {2}')
a is one and b is two
```
















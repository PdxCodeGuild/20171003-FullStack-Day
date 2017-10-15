
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


## String Operations

- `+`, `+=` concatenation
- `*`, `*=` repeat a string
- `len(s)` get the length of a string
- `s[i]` get the character at index i
- `s[i:j]` get the sub-string from `i` to `j`
- `s[i:j:k]` get every `k`th character from `i` to `j`
- `s.find(a)` returns the index of a the first occurance of `a`
- `s.upper()` convert to upper case
- `s.lower()` convert to lower case
- `s.startswith(a)` returns true if the string starts with `a`
- `s.endswith(a)` returns true if the string ends with `a`
- `s.replace(a, b)` replaces occurances of string `a` with string `b`
- `s.strip()` moves leading and trailing characters
- `s.split(delimeter)` splits a string into a list
- `delimeter.join(list)` combines the elements of a list into a single string, separated by the delimeter

Remember that strings are **immutable** meaning their values cannot be changed. Each of these operations returns a **new** string. Sometimes people new to programming will make a mistake such as...

```python
s = ' Hello! '
s.lower()
s.strip()
print(s) # ' Hello! ' original value is unchanged
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

You can also format strings with the `format` function.

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

















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















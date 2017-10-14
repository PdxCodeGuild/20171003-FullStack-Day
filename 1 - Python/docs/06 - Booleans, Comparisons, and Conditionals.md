
# Booleans, Comparisons, and Conditionals

## Booleans

Booleans are one of the built-in types, and represent either `True` or `False`. There are three boolean operators: `not`, `and` and `or`.


### De Morgan's laws

De Morgan's laws are two rules for distributing a `not` over an `and` and an `or`. You can verify these rules by writing out the truth tables for these expressions.

```
not (A and B) == (not A) or (not B)
not (A or B) == (not A) and (not B)
```

# Comparisons

- `==` equals
- `!=` not-equals
- `<` less-than
- `<=` less-than-or-equal-to
- `>` greater-than
- `>=` greater-than-or-equal-to

If you're comparing whether a value is between two other values, you can also write it without an `and`: `x > 5 and x < 10` can also be written as `5 < x < 10`.


# Conditionals

The body which executes will be the first whose condition matches, or `else` if none of them match. Only one body of an if-elif-chain will execute, they're mutually exclusive. Therefore, it's unnecessary to rule-out prior conditions.

```python
temperature = 45

if temperature < 60:
    print('cold')
elif temperature >= 60 and temperature < 70:
    print('warm')

# can be re-written as...

if temperature < 60:
    print('cold')
elif temperature < 70:
    print('warm')
```

It's possible to write a conditional on one line, as `x if condition else y`. For example, a `min` function might be written as

```python
def min(a, b):
    return a if a < b else b
```






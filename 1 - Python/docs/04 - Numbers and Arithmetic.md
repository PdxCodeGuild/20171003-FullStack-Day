
# Numbers and Arithmetic

## Ints

'Ints' represent integers, or 'whole numbers', and they can be positive or negative.

```python
x = 5
print(x)
>>> 5
```

## Floats

'Float' is stort for 'floating-point number', which represents an approximation of a real number. Floats may also be written with an exponent, designated by `e`: `3.12e6` is 3,120,000.

```python
x = 5.23
print(x)
>>> 5.23
```

There are also three special values floats may take: positive infinity, negative infinity, and NaN. NaN is short for 'not a number', it's the result of some mathematical operations, particularly in `numpy`. You can check for these values with the `math` module.

```python
import math

x = float('nan')
print(math.isnan(x))

y = float('inf')
print(math.isinf(y))

z = float('-inf')
print(math.isinf(z))
print(math.isfinite(z))
```

## Arithmetic Operators

- `+` addition
- `-` subtraction
- `*` multiplication
- `/` division
- `//` floor division, results in an `int`
- `%` modulus, a%b is the remainder of a/b
- `**` exponentiation

Modulus is the 'remainder function' for example, 5%2 is 1, 6%2 is 0, 23%5 is 3, etc. It's also useful for containing the range of a variable.

```
i = 0
while i < 100:
    print(i%3)
    i = i + 1
>>> 0
>>> 1
>>> 2
>>> 0
>>> 1
>>> 2
>>> 0
etc
```


For each of the arithmetic operators, there are short-hand versions, which compute a result and store it as the original variable: `x += 2` is equivalent to `x = x + 2`.

```python
x = x + 2
x += 2

x = x - 2
x -= 2

x = x * 2
x *= 2

etc
```








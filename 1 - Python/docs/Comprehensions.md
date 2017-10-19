

# Comprehensions


## List Comprehensions

List comprehensions allow us to generate a list with a single statement.

```python
nums = [x**2 for x in range(10)]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

This is equivalent to a loop with `append`.
```python
nums = []
for x in range(10):
    nums.append(x**2)
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

### Transforming Elements

```python
names = ['David', 'Helen', 'Anne']
lower_names = [name.lower() for name in names]
lower_names  #> ['david', 'helen', 'anne']
```

```python
def lookup_phone_number_by_name(name):
    """Return the phone number of a person."""
    ...
names = ['David', 'Helen', 'Anne']
phone_numbers = [lookup_phone_number_by_name(name) for name in names]
```

### Filtering Elements

We can also put an `if` clause at the end of our comprehension to filter elements. The example below filters out leap years.

```python
years = [1995, 2000, 2004, 2011]
leap_years = [year for year in years if year % 4 == 0]
leap_years  #> [2000, 2004]
```

As another example, say we wanted to make a list of doubled odd elements. We could write it as...

```python
numbers = [1, 2, 3, 4, 5]
doubled_odds = []
for n in numbers:
    if n % 2 == 1:
        doubled_odds.append(n * 2)
```

A more succinct way to write this is by using a comprehension.

```python
numbers = [1, 2, 3, 4, 5]
doubled_odds = [n * 2 for n in numbers if n % 2 == 1]
```

### Nested Comprehensions

```python
[[1 if col == row else 0 for col in range(0, 3) ] for row in range(0, 3) ]

[[1, 0, 0],
 [0, 1, 0],
 [0, 0, 1]]
```

## Set Comprehensions

Set comprehensions can be written much like list comprehensions. Remember that sets can only contain unique elements, so any duplicates will be removed.

```python
{x // 10 for x in range(100)}
```


## Dict Comprehensions

Dict comprehensions also look similar to list comprehensions, but with curly braces and colons.

```py
names_to_ages = {'Amanda': 90, 'David': 50}
{name: age / 2 for name, age in names_to_ages.items()}  #> {'Amanda': 45, 'David': 25}
```





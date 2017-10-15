# Tuples

**Tuples** are like lists, but immutable. Their literals are surrounded by parentheses `()`. For more info, check out the [official docs](https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range).

Single item tuples need a trailing comma to distinguish them from grouping parentheses. Empty tuples are created using `tuple()`.

```py
('David', '503-555-9895')
(2016, 7, 13)
('Alice', )
tuple()
```

Why use tuples over lists? Lists tend to be used for _homogenous_ data, tuples tend to be used for "pairs", "triplets" or "n-tuples"; groupings of _heterogenous_ data. For example, a list of friends is a list because it doesn't matter exactly how many there are and all are names. A pair of address and phone number would be a tuple, since each is interpreted differently and if there was another item, it you wouldn't know what to do with it.

```python
friend_names = ['Kate', 'Al']
contact_info = ('123 Main St', '503-555-1234')
```

You can cast a sequence to a tuple with the `tuple()` function.

```python
fruits = ['apples', 'bananas', 'pears']
fruits_tuple = tuple(fruits)
print(fruits_tuple)
```

Tuples are immutable. Trying to modify them is an exception.

```python
contact_info = ('123 Main St', '503-555-1234')
contact_info[0] = '456 Water Ave'  # Throws TypeError
```

Also, realize there are four different ways to use parentheses now:

1. Order of operations
1. Line continuations
1. Function calls
1. Tuple literals

```py
x = (4 + 3) * 6
x = (4 *
     3 *
     8)
min(5, 6)
('Al', 'Kate')
```

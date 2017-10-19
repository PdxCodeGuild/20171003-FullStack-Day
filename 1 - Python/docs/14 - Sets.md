# Sets

**Sets** are an _unordered_, mutable, unique, iterable, collection of values. They are similar to the sets in mathematics. You can find more info [here](https://docs.python.org/3/tutorial/datastructures.html#sets).

Set literals are written using curly braces and . The empty set is  written as `set()` to not conflict with the empty dict.

```python
{2, 4, 6, 8}
set()
```

Only _immutable_ values can be inside, thus lists and other dicts can't be inner values. If there are duplicate values, they are automatically collapsed into a single one.

```python
{2, 2, 2}  #> {2}
```

You can convert any iterable to a set using the `set()` function.

```python
>>> set([1, 2, 2, 4, 4])
{1, 2, 4}
>>> set('hello world')
{'h', 'e', 'l', 'o', 'w', 'r', 'd'}
```

## Operators

|Operation|Description|
|--- |--- |
|`len(s)`|number of elements in set s (cardinality)|
|`x in s`|test x for membership in s|
|`x not in s`|test x for non-membership in s|
|`s.issubset(t)` or `s <= t`|test whether every element in `s is in t`|
|`s.issuperset(t)` or `s >= t` |test whether every element in t is in s|
|`s.union(t)` or `s &#124; t` | new set with elements from both s and t|
|`s.intersection(t)` or `s & t` | new set with elements common to s and t|
|`s.difference(t)` or `s - t` |new set with elements in s but not in t|
|`s.symmetric_difference(t)` or `s ^ t`|new set with elements in either s or t but not both|
|`s.copy()` |new set with a shallow copy of s|


```python
>>> 2 in {1, 2, 4}
True
>>> {1, 2, 3} | {3, 4}
{1, 2, 3, 4}
>>> {1, 2, 3} & {3, 4}
{3}
>>> {1, 2, 3} - {3, 4}
{1, 2}
```

Check out the [standard library docs for sets](https://docs.python.org/3/library/stdtypes.html#set-types-set-frozenset) for an overview of all the things you can do.


```python
>>> even_nums = {x * 2 for x in range(4)}
{0, 2, 4}
```
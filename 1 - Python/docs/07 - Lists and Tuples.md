
# Lists and Tuples

## Lists


Lists are collections of ordered elements. We can define lists using square brackets. The elements a list contains don't have to all be of the same type.

```python
fruits = ['apple', 'banana', 'peach', 'pear']
nums = [4, 56, 73, 12]
mixed = [3, 'red', 45.012, [3, 5]] # lists can even contain other lists!
```

We can check if a list contains an element using 'in':

```python
fruits = ['apples', 'bananas', 'pears']
if 'apples' in fruits:
    print('true!')
```


### List Operations

- `copy()` creates a copy of the list
- `append()` appends an element to the end
- `insert()` inserts the value at the specified index
- `remove()` removes the first occurance of the element
- `pop()` removes the element at the given index
- `extend()` combines two lists into one
- `index()` returns the index of a given element
- `reverse()` reverses a list
- `sort()` sorts a list




## Tuples

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



# Lists


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


## List Operations

- `copy()` creates a copy of the list
- `append()` appends an element to the end
- `insert()` inserts the value at the specified index
- `remove()` removes the first occurance of the element
- `pop()` removes the element at the given index
- `extend()` combines two lists into one
- `index()` returns the index of a given element
- `reverse()` reverses a list
- `sort()` sorts a list



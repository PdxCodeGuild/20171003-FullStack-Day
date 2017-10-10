
# Loops


## While Loops

`while` loops execute a block of code while a condition is true. Here, each iteration the value of `i` will increase by `1` until the value `i < 10` becomes false, and the loop will terminate.

```python
i = 0
while i < 10:
    print(i)
    i += 1
print('done')

>>> 0
>>> 1
>>> 2
>>> 3
>>> 4
>>> 5
>>> 6
>>> 7
>>> 8
>>> 9
>>> done
```

## For Loops

`for` loops are much more flexible, they allow us to iterate anything that's **iterable**: ranges, lists, strings, sets, dicts, etc.

To loop over a range of numbers, we can use `range`. The values it generates go up to but not including the number passed as a parameter (here, 10). Each iteration, the variable `i` will be bound to the values of `range`.

```python
for i in range(10):
    print(i)

>>> 0
>>> 1
>>> 2
>>> 3
>>> 4
>>> 5
>>> 6
>>> 7
>>> 8
>>> 9
```

We now have three ways of looping over a list:
```python
# iterate over the indices
fruits = ['apples', 'bananas', 'pears', 'cherries', 'pineapple']
for i in range(len(fruits)):
    print(fruits[i])

# iterate over the elements
fruits = ['apples', 'bananas', 'pears', 'cherries', 'pineapple']
for fruit in fruits:
    print(fruit)

# if we want both the indices and values, we can use enumerate
fruits = ['apples', 'bananas', 'pears', 'cherries', 'pineapple']
for i,fruit in enumerate(fruits):
    print(str(i)+' '+str(fruit))
```


## Break and Continue

The keywords `break` and `continue` are two ways of controlling the operation of a loop.

- `break` causes the loop to exit immediately, not executing any more statements of the loop's body
- `continue` skips the current iteration and continues with the next

```python
# 'continue' allows us to skip rest of the current iteration
# 'break' allows us to leave the loop entirely
fruits = ['apple', 'banana', 'peach', 'pear', 'pineapple', 'cherry']
for fruit in fruits:
    if fruit == 'banana':
        continue # skip over 'banana'
    elif fruit == 'pineapple':
        break # leave the loop on 'pineapple', note 'cherry' isn't printed either
    print(fruit)

>>> apple
>>> peach
>>> pear
```
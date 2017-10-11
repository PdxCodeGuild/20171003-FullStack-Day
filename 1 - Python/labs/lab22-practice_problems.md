# Lab 22: Practice Problems 2





## Problem 1

Write a REPL which asks users for a list of numbers, which they enter, until they say 'done'. Then print out the list.

```
>>> Enter a number (or 'done'): 5
>>> Enter a number (or 'done'): 34
>>> Enter a number (or 'done'): 515
>>> Enter a number (or 'done'): done
[5, 34, 515]
```


## Problem 2


```
nums = [0, 1, 2, 3, 4, 5, 6, 7, 8]
print_every_other(nums)
```
```
0, 2, 4, 6, 8
```

Print out every other element of a list, first using a while loop, then using a for loop.


## Problem 3

Given a list of numbers, and a target number, find a pair of numbers from the list that sum to a target number

```
nums = [5, 6, 2, 3]
target = 7
find_pair(nums, target)
```
```
[5, 2]
```



## Problem 4

Get a string from the user, print out another string, doubling every letter.

```
>>> Enter some text: hello
hheelloo
```

## Problem 5

Write a function that merges two lists into a single list, where each element of the outlist list is another list containing two elements.

`merge([5,2,1], [6,8,2])` -> `[[5,6],[2,8],[1,2]]`






## Problem 6

Write a function that takes two ints, a and b, and returns True if one is positive and the other is negative.

```python
opposite(10, -1) → True
opposite(2, 3) → False
opposite(-1, -1) → False
```
## Problem 7

Write a function that returns True if a number within 10 of 100.

```python
near_100(50) → False
near_100(99) → True
near_100(105) → True
```


## Problem 8

Write a function that takes a string, and returns a list of strings, each missing a different character.

```python
missing_char('kitten') → ['itten', 'ktten', 'kiten', 'kiten', 'kittn', 'kitte']
```


## Problem 9

Write a function that returns the number of occurances of 'hi' in a given string.

```python
count_hi('hihi') → 2
```

## Problem 10

Write a function that returns True if a given string contains the same number of 'cat' as it does 'dog'

```python
cat_dog('catdog') → True
cat_dog('catcat') → False
cat_dog('catdogcatdog') → True
```

## Problem 11

Write a function that takes a list of numbers, and returns True if there is an even number of even numbers.

```python
eveneven([5, 6, 2]) → True
eveneven([5, 5, 2]) → False
```


## Problem 12

Write a function `combine_all` that takes a list of lists, and returns a list containing each element from each of the lists.

```python
nums = [[5,2,3],[4,5,1],[7,6,3]]
combine_all(nums) → [5,2,3,4,5,1,7,6,3]
```


## Problem 13

Write a function that takes `n` as a parameter, and returns a list containing the first `n` [Fibonacci Numbers](https://en.wikipedia.org/wiki/Fibonacci_number).

```python
fibonacci(8) → [1, 1, 2, 3, 5, 8, 13, 21]
```

## Problem 14
Return the letter that appears the latest in the english alphabet.
```
>>> latest_letter('pneumonoultramicroscopicsilicovolcanoconiosis')
the latest letter is v.
```

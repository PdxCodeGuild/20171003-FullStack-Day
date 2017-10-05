# Lab 14: Practice Problems



### Problem 1
Return the number of letter occourances in a string.
```
>>> count_letter('i', 'Antidisestablishmentterianism')
5
>>> count_letter('p', 'Pneumonoultramicroscopicsilicovolcanoconiosis')
2
```

## Problem 2

Convert input strings to lowercase without any surrounding whitespace.

```
>>> lower_case("SUPER!")
'super!'
>>> lower_case("        NANNANANANA BATMAN        ")
'nannananana batman'
```


### Problem 3

Write a function that tells whether a number is even or odd (hint, compare a/2 and a//2, or use a%2)

`def is_even(a):`


`is_even(5)` will return False

`is_even(6)` will return True


### Problem 4

Write a function using random.randint and subscription to get a random element of a list and return it.

`def random_element(a):`

```
fruits = ['apples', 'bananas', 'pears']
random_element(fruits) could return 'apples', 'bananas' or 'pears'
```

### Problem 5

Write a function that returns the maximum of 3 parameters.

`def maximum_of_three(a, b, c):`

`maximum_of_three(5,6,2) will return 6`

`maximum_of_three(-4,3,10) will return 10`

### Problem 6

print out the powers of 2 from 2^0 to 2^20

`1, 2, 4, 8, 16, 32, ...`

### Problem 7
Write functions to find the minimum, maximum, mean, and (optionally) mode of a list of numbers.

`def minimum(nums):`

`def maxmimum(nums):`

`def mean(nums):`

(OPTIONAL)
`def mode(nums):`


### Problem 8
Write a function that returns the reverse of a list.

`def reverse(nums):`

### Problem 9
Write a function to find all common elements between two lists.

`def common_elements(nums1, nums2):`

### Problem 10
Write a function to move all the elements of a list with value less than 10 to a new list and return it.

`def extract_less_than_ten(nums):`

### Problem 11
Write a function to combine two lists of equal length into one, alternating elements.

`def combine(nums1, nums2):`

`combine(['a','b','c'],[1,2,3])` returns `['a', 1, 'b', 2, 'c', 3]`
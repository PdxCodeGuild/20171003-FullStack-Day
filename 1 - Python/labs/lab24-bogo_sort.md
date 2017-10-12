# Lab 24: Bogo Sort

Bogo sort is one of the least efficient sorting algorithms imaginable! It works by generating random arrangements of a list, checking if the list is sorted, and if it is, return it. For a list of 200 numbers, there are 200! = 7.88*10^374 possible combinations, only one of them is the sorted list.

`random_list(n)` generates and returns a list of length n, with random values between 0 and 100

`shuffle(nums)` randomly re-arranges a list
- iterate through the indices of the list
- for each index, generate a random index
- swap the elements at the two indices

`is_sorted(nums)` checks if a list is sorted
- iterate through the indices of the list
- if the element at the current index is greater than the element at the next index, the list isn't sorted, and you can return `False`
- if you get through the entire list and each element is less than or equal to the next element, the list is sorted, and you can return `True`

`bogosort(nums)` continues to generate random arrangements until the list is sorted
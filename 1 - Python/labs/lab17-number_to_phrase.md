# Lab 17: Number to Phrase

Convert a given number into its english representation. For example: 67 becomes 'sixty-seven'. Handle numbers from 0-99.


Hint: you can use modulus to extract the ones and tens digit.


```python
x = 67
tens_digit = x//10
ones_digit = x%10
```
Hint2: use the digit as an index to look up a string in a list.

## Version 2

Handle numbers from 100-999.

## Version 3 (optional)

Convert a number to roman numerals.

## Version 4 (optional)

Convert a time given in hours and minutes to a phrase.
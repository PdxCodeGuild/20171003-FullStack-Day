# Dictionaries

**Dictionaries** or 'dicts'  provide an unordered, mutable, sequence of key-value pairs or a mapping between keys and values. For more information check the [official docs](https://docs.python.org/3/library/stdtypes.html#mapping-types-dict).

Dict literals are written using curly braces, and key-value pairs defined with colons and separated by commas.

```python
{'apple': 1.0, 'pear': 1.5, 'grapes': 0.75}
{'David': ['day'], 'Sheri': ['day', 'night']}
{}
```

Keys have to be unique, values do not. Any _immutable_ value (int, float, string, tuple) can be a key, thus lists and other dicts can't be keys. Values can be any type.


### Accessing Values

The values of a dictionary are accessed by using the square-brackets with the key, similarly to how we access a specific element from a list using its index.

```python
product_to_price = {'apple': 1.0, 'pear': 1.5, 'grapes': 0.75}
product_to_price['apple']  #> 1.0
product_to_price['grapes']  #> 0.75
product_to_price['banana']  # Throws KeyError
product_to_price[1.0]  # Throws KeyError
```

### Adding and Updating Values

Values can then be added or updated by using the assignment operator `=`.

```python
product_to_price = {'apple': 1.0, 'pear': 1.5, 'grapes': 0.75}
product_to_price['apple'] = 2.0
product_to_price  #> {'apple': 2.0, 'pear': 1.5, 'grapes': 0.75}
product_to_price['banana'] = 0.25
product_to_price  #> {'apple': 1.0, 'pear': 1.5, 'banana': 0.25, 'grapes': 0.75}
```

### Checking if a Key Exists

To check if a list contains a key, use `in`

```python
product_to_price = {'apple': 1.0, 'pear': 1.5, 'grapes': 0.75}
if 'apple' in product_to_price:
    print('apple ' + str(product_to_price['apple']))
'apple 1.0'
```

### Combining Dictionaries

To combine two dictionaries, use the `.update()` type method. Note that it changes the given dict and does not return a new one.

```python
product_to_price = {'apple': 1.0, 'pear': 1.5, 'grapes': 0.75}
product_to_price.update({'banana': 0.25})
product_to_price  #> {'apple': 1.0, 'pear': 1.5, 'banana': 0.25, 'grapes': 0.75}
```

### Retrieving All Keys, Values, and Key-Value Pairs

There are a few type methods that allow you to view different parts of the dictionary. All produce sequences and not proper lists, so cast them to a list to use them normally.

```python
list(product_to_price.keys())  #> ['pear', 'apple', 'grapes']
list(product_to_price.values())  #> [0.75, 1.0, 1.5]
list(product_to_price.items())  #> [('grapes', 0.75), ('apple', 1.0), ('pear', 1.5)]
```

### Order

Dictionaries are unordered; there is no guarantee the same order will come out at each call. Call `sorted()` on the results if you need a stable order.

```python
sorted(product_to_price.keys())  #> ['apple', 'grapes', 'pear']
```

### Conversions

You can cast a sequences of two-tuples to a dictionary using `dict()`. This means `.items()` and `dict()` are inverses.

```py
names_and_fav_colors = [('Alice', 'red'), ('David', 'green')]
dict(names_and_fav_colors)  #> {'Alice': 'red', 'David': 'green'}
dict(product_to_price.items()) == product_to_price  #> True
```



# Classes: Dunder Methods


Classes can implement special methods, called 'dunder methods' which are denoted by two underscores. One which we've already seen is `__init__`, which represents the initializer. For more info, check the [official docs](https://docs.python.org/3/reference/datamodel.html#special-method-names).


### Commom Dunder Methods

| method    | equivalent |
| ---       | ---        |
| \_\_str__ | str(a)     |
| \_\_eq__  | a == b     |
| \_\_ne__  | a != b     |
| \_\_lt__  | a < b      |
| \_\_le__  | a <= b     |
| \_\_gt__  | a > b      |
| \_\_ge__  | a >= b     |
| \_\_add__ | a + b    |
| \_\_sub__ | a - b     |
| \_\_mul__ | a * b     |
| \_\_truediv__ | a / b     |
| \_\_floordiv__ | a // b     |
| \_\_len__ | len(a)     |
| \_\_getitem__ | a[i]     |
| \_\_call__ | a() |


Let's implement these methods on the following class:

```python
class Account:
    """A simple account class"""

    def __init__(self, owner, amount=0):
        """
        This is the constructor that lets us create
        objects from this class
        """
        self.owner = owner
        self.amount = amount
        self._transactions = []
    
    def add_transaction(self, amount):
        self._transactions.append(amount)
```

## String Representations

`__str__` is meant to return the 'pretty' or 'informal' string representation of the object. `__repr__` is meant to return the 'official' string representation of the object.

```python
class Account:
    # ... (see above)

    def __repr__(self):
        return 'Account({!r}, {!r})'.format(self.owner, self.amount)

    def __str__(self):
        return 'Account of {} with starting amount: {}'.format(
            self.owner, self.amount)
```

```
>>> str(acc)
'Account of bob with starting amount: 10'

>>> print(acc)
"Account of bob with starting amount: 10"

>>> repr(acc)
"Account('bob', 10)"
```

## Comparisons

The following methods let you compare objects. If you have to compare objects of different types, you can check the type of the parameter using `type(o) is str` or `isinstance(o, str)`.


| method    | equivalent |
| ---       | ---        |
| \_\_eq__  | a == b     |
| \_\_ne__  | a != b     |
| \_\_lt__  | a < b      |
| \_\_le__  | a <= b     |
| \_\_gt__  | a > b      |
| \_\_ge__  | a >= b     |


```python
class Account:
    # ... (see above)

    def __eq__(self, other):
        return self.balance == other.balance

    def __lt__(self, other):
        return self.balance < other.balance
```


## Arithmetic

The following methods let you use the arithmetic operators. Implementing `__add__` will allow the use of `a + b` and `a += b`.

| method    | equivalent |
| ---       | ---        |
| \_\_add__ | a + b    |
| \_\_sub__ | a - b     |
| \_\_mul__ | a * b     |
| \_\_truediv__ | a / b     |
| \_\_floordiv__ | a // b     |

```python
class Account:
    # ... (see above)
    
    def __add__(self, other):
        owner = self.owner + other.owner
        start_amount = self.balance + other.balance
        return Account(owner, start_amount)
```
```python
>>> acc3 = acc2 + acc
>>> acc3
Account('tim&bob', 110)

>>> acc3.amount
110
>>> acc3.balance
240
>>> acc3._transactions
[20, 40, 20, -10, 50, -20, 30]
```

## Iteration

`__len__` returns the 'length', and will be called we call `len(a)` on an instance. `__getitem__` will allow you to use indexing `a[i]`. Using them together allows you to put your object in a `for` loop.


```python
class Account:
    # ... (see above)

    def __len__(self):
        return len(self._transactions)

    def __getitem__(self, position):
        return self._transactions[position]
```

```
>>> len(acc)
5

>>> for t in acc:
...    print(t)
20
-10
50
-20
30

>>> acc[1]
-10
```

## Callable Objects

You can allow your object to be called like a function

```python
class Account:
    # ... (see above)

    def __call__(self):
        print('Start amount: {}'.format(self.amount))
        print('Transactions: ')
        for transaction in self:
            print(transaction)
        print('\nBalance: {}'.format(self.balance))
```

```
>>> acc = Account('bob', 10)
>>> acc.add_transaction(20)
>>> acc.add_transaction(-10)
>>> acc.add_transaction(50)
>>> acc.add_transaction(-20)
>>> acc.add_transaction(30)
>>> acc()

Start amount: 10
Transactions:
20
-10
50
-20
30
Balance: 80
```




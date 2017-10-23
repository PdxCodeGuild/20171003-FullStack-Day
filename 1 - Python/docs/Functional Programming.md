
# Functional Programming

Remember that Python supports many different programming paradigms, one of which is 'functional programming'. Examples of functional programming languages are [Clojure](https://clojure.org/) and [Haskell](https://www.haskell.org/). Below are a few examples of functional programming in Python.

Printing first 10 Fibonacci numbers, iterative
```python
def fibonacci(n, first=0, second=1):
    while n != 0:
        print(first, end="\n") # side-effect
        n, first, second = n - 1, second, first + second # assignment
fibonacci(10)
```

Printing first 10 Fibonacci numbers, functional expression style

```python
fibonacci = (lambda n, first=0, second=1:
    "" if n == 0 else
    str(first) + "\n" + fibonacci(n - 1, second, first + second))
print(fibonacci(10), end="")
```

Printing a list with first 10 Fibonacci numbers, with generators

```python
def fibonacci(n, first=0, second=1):
    while n != 0:
        yield first
        n, first, second = n - 1, second, first + second # assignment
print(list(fibonacci(10)))
```

Printing a list with first 10 Fibonacci numbers, functional expression style
```python
fibonacci = (lambda n, first=0, second=1:
    [] if n == 0 else
    [first] + fibonacci(n - 1, second, first + second))
print(fibonacci(10))
```
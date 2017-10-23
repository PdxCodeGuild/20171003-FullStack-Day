
# Classes

Classes, like functions and modules, are another of the major building-blocks of a python program. They represent the grouping of data and functions which together serve a common purpose.

## Types

Classes also represent types, like those we've experienced before (`int`, `float`, `string`, `list`, etc). We can call the initializers of our built-in types as well, rather than literals as we've been using them. Creating classes allows us to define custom types.

```python
# every object in python has a type
x = 5
print(type(x)) # 'int'
y = 'hello'
print(type(y)) # 'str'
print(type(type(y))) # 'type'
```

## Initializers

The built-in types also have initializers, which allow us to create instances of the type.

```python
# call the initializer of the str class
s = str() # equivalent to: s = ''

# call the initializer of the int class
i = int() # equivalent to: i = 0
```

Our classes can have initializers too, which allows us to create instances of them. The initializer is a special type of function which uses the parameters passed into it to initialize the instance. Here, we copy the parameters `x` and `y` into the instance by assigning them to variables on `self`, which is an object that represents the class' "self".

```python
class Point:
    def __init__(self, x, y): # this is the initializer
        self.x = x # these are member variables
        self.y = y
    
p = Point(5,2) # call the initializer, instantiate the class
print(p.x) # 5
print(p.y) # 2

print(type(p)) # Point
```

If you tried to do this with dictionaries, every time you'd want to refer to the member variables `x` and `y`, you'd have to write `p['x']` and `p['y']`. If you used lists, you'd have to refer ambiguously to `p[0]` and `p[1]`. You'd also have no way of checking the type, or attaching functions to the object.

```python
import math

# we could instead use dictionaries instead of classes
#p1 = {'x': 5, 'y': 2}
#p1['x']

# or just use lists, and write functions to perform operations on those lists
def distance(p1, p2):
    dx = p1[0] - p2[0]
    dy = p1[1] - p2[1]
    return math.sqrt(dx*dx + dy*dy)

p1 = [5, 2]
p2 = [8, 4]
print(distance(p1, p2))
```


## Methods

Classes allow us to write 'methods' or 'member-functions', which are functions that are called 'on the object'. These are exactly like regular functions, except that the first parameter is always 'self'.

```python
import math

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    def distance(self, p): # method, or 'member function'
        dx = self.x - p.x
        dy = self.y - p.y
        return math.sqrt(dx*dx + dy*dy)
    
    def scale(self, v):
        self.x *= v
        self.y *= v
    
p3 = Point()
p1 = Point(5,2)
p2 = Point(8,4)
dist = p1.distance(p2) # or p2.distance(p1), either works
print(dist)

# similar to how we can call methods of the str class
s = 'hello world'
print(s.split(' '))
```

## Static Methods

Static methods are methods that belong to the **type** and **not** the instance. They're represented by an `@staticmethod` above the function declaration.


```python
import math

class Point:
    ...
    
    @staticmethod
    def from_polar(r, theta): # static methods belong to the type, not the instance
        px = r * math.cos(theta)
        py = r * math.sin(theta)
        return Point(px, py)

    
polar_point = Point.from_polar(5.0, math.pi/6)
polar_point.scale(2)
print(len(polar_point))
print(polar_point)
```

## Dunder Methods

A class can implement several 'dunder' methods which have special functionality.

```python
import math

class Point:
    ...
    
    def __str__(self): # specify a str conversion
        return '['+str(self.x)+','+str(self.y)+']'
    
    def __len__(self):
        return 2

p = Point(5, 2)
print(p) # [5,2]
print(len(p)) # 2

```


## Private Variables

We can specify private variables to maximize **encapsulation**. What if the variable is sometimes in an 'invalid' state? Furthermore setting the variable directly could have strange side-effects. These are represented by two underscores before the variable name.

```python
import math

class PointPriv:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
    
    def distance(self, p):
        dx = self.__x - p.__x
        dy = self.__y - p.__y
        return math.sqrt(dx*dx + dy*dy)

p1 = PointPriv(5,2)
p2 = PointPriv(7,8)
print(p1.distance(p2))
print(p1.__x) # AttributeError: 'PointPriv' object has no attribute '__x'
```

Note that these variables are still accessible, and are merely re-named when the code is run.

```python
print(p1.__dict__) # {'_PointPriv__x': 5, '_PointPriv__y': 2}
print(p1._PointPriv__x)   # 5
```

Below is an example where private variables are useful. If other code changed the value of `alpha`, it wouldn't have any effect on the transformation, which they wouldn't expect. So we restrict access to `alpha` but provide a 'setter' method, which ensures the `cos_alpha` and `sin_alpha` terms are properly set.

```python
import math

class Rotator:
    
    def __init__(self, alpha):
        self.setAlpha(alpha)
    
    def setAlpha(self, alpha):
        self.__alpha = alpha
        self.cos_alpha = math.cos(alpha)
        self.sin_alpha = math.sin(alpha)
    
    def rotate(self, px, py):
        rx = px*self.cos_alpha + py*self.sin_alpha
        ry = -px*self.sin_alpha + py*self.cos_alpha
        return rx, ry
```


## Inheritance

You can visualize it like an onion, with the super-class in the center, and a subclass representing a new shell. The child class has all the attributes of its parent, but additional attributes all its own.


```python
class Animal:
    pass


class Squirrel(Animal):
    pass
```



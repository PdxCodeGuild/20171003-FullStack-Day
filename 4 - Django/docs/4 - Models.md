

# Models

Models are Python classes that parallel tables in the database. The ORM manages this dual representation, translating statements in Python to operations on the database. You can read more about models [here](https://docs.djangoproject.com/en/1.11/topics/db/models/), and more about the ORM [here](https://docs.djangoproject.com/en/1.11/ref/models/querysets/).


## Class-Table Representation

Database tables are like excel spreadsheets: they have headers and rows. Tables can also be thought of as Python classes, where the headers are class attributes, and the rows are instances.

| id | email_address | first_name | last_name |
| --- | --- | --- | --- |
| 1 | wendy@gmail.com | Wendy | Carson |
| 2 | alyssa@gmail.com | Alyssa	 | Lyons |
| 3 | brian@gmail.com | Brian | Barber |

```python
class User:
    def __init__(self, id, email_address, first_name, last_name):
        self.id = id
        self.email_address = email_address
        self.first_name = first_name
        self.last_name = last_name
user1 = User(1, 'wendy@gmail.com', 'Wendy', 'Carson')
user2 = User(2, 'alyssa@gmail.com', 'Alyssa', 'Lyons')
user3 = User(3, 'brian@gmail.com', 'Brian', 'Barber')
```
All models are automatically given an `id` field, which is an int that uniquely idenifies a row.




## Field Types

You can read more about the field types [here](https://docs.djangoproject.com/en/1.11/ref/models/fields/).

- `BooleanField` represents a boolean (true/false) value
- `IntegerField` represents an integer
- `FloatField` represents a floating-point number
- `CharField` represents a string, requires `max_length` parameter indicating the number of characters
- `TextField` like `CharField` but has unlimited length
- `DateTimeField` represents a datetime (more [here](https://docs.djangoproject.com/en/1.11/topics/i18n/timezones/))
- `OneToOneField` represents a [one-to-one relationship](https://docs.djangoproject.com/en/1.11/topics/db/examples/one_to_one/)
- `ForeignKey` represents a [many-to-one relationship](https://docs.djangoproject.com/en/1.11/topics/db/examples/many_to_one/)
- `ManyToManyField` represents a [many-to-many relationship](https://docs.djangoproject.com/en/1.11/topics/db/examples/many_to_many/)

### Nullable Fields

Fields can be 'null' or absent. In Python, the attributes of the instances will be `None`. To declare these fields to be 'nullable', you must specify both `null=True` for the database, and `blank=True` for the admin interface.

```Python
date_completed = models.DateTimeField(null=True, blank=True)
```

### Default Values

You can specify a default value for a field by adding `default=<value>`. That way, you can leave the value out when creating and saving an instance.

```python
class Person(models.Model):
    # ...
    age = models.IntegerField(default=0)

person = Person(name="mike") # no need to specify age
person.save()
```


## Database Relationships

The three types of database relationships: one-to-one, many-to-one, and many-to-many. The `id` field of a table is called the **primary key** because it uniquely identifies a table. When another table contains a reference to that `id` field, it's called a **foreign key**. In the following example, `city_id` on `Users` is a **foreign key**, `id` on Users and `id` on Cities are **Primary Keys**. This is an example of a **many-to-one relationship**.

#### Users
| id | email_address | first_name | last_name | city_id |
| --- | --- | --- | --- | --- |
| 1 | wendy@gmail.com | Wendy | Carson | 1 | 
| 2 | alyssa@gmail.com | Alyssa	 | Lyons | 1 |
| 3 | brian@gmail.com | Brian | Barber | 2 |

#### Cities
| id | name |
| --- | --- |
| 1 | Portland |
| 2 | Eugene |

This relationship would be represented in Python as thus:

```python
from django.db import models

class City(models.Model):
    name = models.CharField(max_length=200)

class User(models.Model):
    email_address = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    city = models.ForeignKey(Question, on_delete=models.CASCADE)
```

### One-to-One

A one-to-one relationship means that for every row in table A, there will be a single corresponding row in table B. An example might be between [counties and capital cities](https://upload.wikimedia.org/wikipedia/commons/thumb/f/f7/CPT-Databases-OnetoOne.svg/460px-CPT-Databases-OnetoOne.svg.png). Any country only has one capital. Any capital only pretains to one country. You can read more about one-to-one relationships [here](https://docs.djangoproject.com/en/1.11/topics/db/examples/one_to_one/).

### Many-to-One

A many-to-one relationship means that for every row in table A, there may be multiple rows in table B connected to it. An example might be between a [mother and her children](https://upload.wikimedia.org/wikipedia/commons/thumb/2/26/CPT-Databases-OnetoMany.svg/460px-CPT-Databases-OnetoMany.svg.png). A mother may have multiple children, but any child only has one mother. You can read more about many-to-one relationships [here](https://docs.djangoproject.com/en/1.11/topics/db/examples/many_to_one/).


### Many-to-Many

An example might be between [authors and books](https://upload.wikimedia.org/wikipedia/commons/thumb/c/c4/CPT-Databases-ManytoMany.svg/460px-CPT-Databases-ManytoMany.svg.png). One book may have multiple authors. One author may have multiple books. To define such a relationship, you can create a [junction table](https://upload.wikimedia.org/wikipedia/commons/thumb/0/02/Databases-ManyToManyWJunction.jpg/800px-Databases-ManyToManyWJunction.jpg) with two many-to-one relationships. Or you can use a `ManyToManyField`
You can read more about many-to-many relationships [here](https://docs.djangoproject.com/en/1.11/topics/db/examples/many_to_many/).


### on_delete

The `on_delete` parameter lets you control what to do with other rows when a connected row is deleted. You can read more about `on_delete` [here](https://docs.djangoproject.com/en/2.0/ref/models/fields/#arguments). The important options are:

- `CASCADE` deleted this row when the other is deleted
- `PROTECT` throws an exception when the other is deleted, this forces the developer re-assign the relationship when they want to delete a row
- `SET_NULL` sets the field containing the relationship to null (the field must also be nullable)
- `SET_DEFAULT` sets the field containing the relationship to its default value (a default must be specified)


## ORM Operations

The ORM 'object relational mapping' provides functions in Python that perform operations on the database. To read more about ORM operations, look [here](https://docs.djangoproject.com/en/1.11/topics/db/queries/).

Note that `__init__`, `get`,  and `filter` take `**kwargs` (which turns named parameters into a dictionary), whereas `order_by` takes `*args` (which turns arguments into a list). 


### Create an Instance

```python
from django.utils import timezone
todo_text = "wash the dishes"
todo_item = TodoItem(todo_text=todo_text, date_entered=timezone.now(), date_completed=None)
```

### Save an Instance

Just call `save()` on an instance.

```python
todo_item.save()
```


### Get All Rows

To get all the rows in a table use `all()`.

```python
todo_items = TodoItem.objects.all()
```


### Get a Particular Row

To get a particular row, use `get()`. Here we're getting the item with a given primary key (pk), but you can use any attribute.

```python
item_id = 5
item = TodoItem.objects.get(pk=item_id)
```

### Filter Rows

You can `filter` particular rows by specifying a particular attribute's value. This is like `get` but you get multiple results instead of the first matching one.

```python
todo_items = TodoItem.objects.filter(text='water the roses')
```

To filter variables by whether or not a field is null, use `<field_name>__isnull`
```python
completed_items = TodoItem.objects.filter(date_completed__isnull=False)
```

### Specify an Order

To specify an order, use `order_by`, which takes any number of strings containing the names of the attributes to sort by. By default sort is ascending, use a negative symbol `-` to sort in the descending order.

```python
todo_items = TodoItem.objects.order_by('-date_entered', '-date_completed')
```


### Specify the Number of Rows to Return

To limit the number of items returned, use slicing.

```python
# only get the first 5 results
todo_items = TodoItem.objects.order_by('-date_entered')[:5]
```

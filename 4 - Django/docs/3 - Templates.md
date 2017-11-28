


# Templates

Templates are like blueprints for your HTML pages. They contain plain HTML/CSS/JavaScript, but also additional syntax for generating HTML/CSS/JavaScript using variables from your Python view. You can read more about Templates [here](https://docs.djangoproject.com/en/1.11/topics/templates/3 - Templates.md).


## if

What you put inside an `if` block will only be rendered if the condition is true.

```html
{% if number == 5 %}
<span>the number is 5</span>
{% endif %}
```

## for

Whatever you put inside the `for` block will be repeated for each iteration of the loop. For example, we can build a list of items.

```html
<ul>
    {% for todo_item in todo_items %}
    <li>{{ todo_item.text }}</li>
    {% endfor %}
</ul>
```


## Rendering URLs

In order for Django to find the proper path when rendering the template, the app's `urls.py` must contain the variable `app_name`, e.g. `app_name = 'todos'`.


#### urls.py
```python
from django.conf.urls import url
from . import views
app_name = 'todos'
urlpatterns = [
    url('^$', views.index, name='index'),
    url('add/$', views.add, name='add')
]
```

#### index.html
```html
<form action="{% url 'todos:add' %}" method="post">
    {% csrf_token %}
    <input type="text" name="todo_text"/>
    <button type="submit">+</button>
</form>
```


The `name` given in `urls.py` and the actual `path` can be different. To keep things simple, use consistent names. You can read more about [routing](https://docs.djangoproject.com/en/1.11/topics/http/urls/) and the [urls package](https://docs.djangoproject.com/en/1.11/ref/urls/).


## Forms

A form is an HTML element that can transmit data to a server. Forms have two important attributes: `action` and `method`. The `action` is the url to which the form's data will be submitted. The `method` is the HTTP method (POST, GET, PUT, DELETE).

The `input` elements inside a form. To 'submit' the data, add a button with `type="submit` inside the form. You can read more about forms [here](https://developer.mozilla.org/en-US/docs/Learn/HTML/Forms/Your_first_HTML_form).

Django also requires a CSRF token to be submitted as part of the form. CSRF stands for 'cross-site request You can include this just by adding `{% csrf_token %}` inside the form. You can read more about CSRF [here](https://en.wikipedia.org/wiki/Cross-site_request_forgery).

```html
<form action="/savetodo" method="post">
    {% csrf_token %}
    <input type="text" name="todo_text"/>
    <button type="submit">+</button>
</form>
```

## Static Files

To load static files into a page, create a folder in your app called `static`. Inside that folder, create a folder with the same name as your app (just as you did with templates). In your template, you then must add `{% load static %}` before you load your static file.

```html
{% load static %}
<img src="{% static 'todos/example.jpg' %}" alt="My image"/>
```

## Template Inheritance

todo
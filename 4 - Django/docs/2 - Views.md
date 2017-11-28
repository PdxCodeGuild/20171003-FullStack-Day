
# Views

**Views** are python functions that are executed when a request follows a route. The view can then respond with HTML, JSON, etc. An app's views are contained in its `views.py` file. You can read about both the request and response objects [here](https://docs.djangoproject.com/en/1.11/ref/request-response/).


## Requests

The request object received by the view contains lots of important information.

- `request.method` tells you which of the HTTP methods was used (GET, POST, etc)
- `request.body` the raw request body, you can also use `request.read()`
- `request.path` path of the requested page, e.g. `"/music/bands/the_beatles/"`
- `request.GET` dictionary-like object of query parameters
- `request.POST` dictionary-like object of post parameters
- `request.COOKIES` a dictionary of cookies


### Path Parameters

Path parameters must be 'captured' in the regular expression of the path. These are called 'named capture groups'. These values then become parameters to the view.

##### urls.py
```python
from django.conf.urls import url
from . import views
app_name = 'todoapp'
urlpatterns = [
    # e.g. /detail/5, /detail/23
    url(r'^detail/(?P<todo_item_id>[0-9]+)/$', views.detail, name='detail')
]
```

##### views.py
```python
def detail(request, todo_item_id):
    todo_item = get_object_or_404(TodoItem, pk=todo_item_id)
    return render(request, 'todoapp/detail.html', {'todo_item': todo_item})

```


### Query Parameters

Query parameters are passed as part of the url and are turned into dictionary-like objects.

```python
print(request.GET['todo_item_text'])
```


### POST parameters

```python
print(request.POST['todo_item_text'])
```


### JSON

To read posted JSON, you can use the built-in `json` module to read the request's body.

```python
import json
def postdata(request):
    received_json_data = json.loads(request.body)
    print(received_json_data)
    return HttpResponse('OK')
```


## Responses

### Responding with a String / Raw HTML

```python
from django.http import HttpResponse
def index(request):
    return HttpResponse('Hello World!')
```

### Responding with a Template

To render a template, use the `render` function. The first parameter is the original request, the second is the location of the template, and the third is a dictionary containing the variables to be rendered.

```python
from django.shortcuts import render
from .models import TodoItem
def index(request):
    todo_items = TodoItem.objects.all()
    context = {'todo_items': todo_items}
    return render(request, 'todos/index.html', context)
```

### Responding with JSON


To respond with a JSON object, you can just pass a dictionary to a JsonResponse.

```python
from django.http import JsonResponse
def getdata(request):
    data = {'foo': 'bar', 'hello': 'world'}
    return JsonResponse(data)
```


### Redirecting

To redirect, you can use the HttpResponseRedirect class. It's also best to use the `reverse` function to look up the url using the name rather than hard-coding it.

```python
from django.http import HttpResponseRedirect
from django.urls import reverse
def add(request):
    ...
    return HttpResponseRedirect(reverse('todos:index'))
```

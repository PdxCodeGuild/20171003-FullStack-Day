
# Routes

Routes connect URLs to views. The routes are stored in a **urls.py** file, which can be found in both the project folder and in each of the apps' folders. URLs are matched via **regular expressions**. To more easily express regular expressions, we'll use **raw strings** which ignore escape sequences. You can specify raw strings by placing an 'r' in front of a string literal, e.g. `r'\'` is the same as `'\\'`. You can read more about routes [here](https://docs.djangoproject.com/en/1.11/topics/http/urls/).


```python
from django.conf.urls import url

# import your views module, so you can tell Django about the view functions
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^posts$', views.posts, name='posts'),
]
```

Every path should start with `^` and end with `$` to ensure you don't over-match. Routes are evaluated **in order**: whichever route matches first is the one used.

```python
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^base/', views.base),  # if you forget a $, will "eat" longer paths.
    url(r'^base/(?P<named>.+)/$', views.base_capture),  # captures might "eat" longer paths.
    url(r'^base/wont_match/$', views.base_wont_match),  # this will never match because of _both_ of above routes.
]
```

## include()

The `include` function allows you to combine the routes of multiple `urls.py` files into one. This is used to connect the project's 'main' `urls.py` to the `urls.py` in each of the apps.

```python
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^<path>/', include('<appname>.urls'))
]
```

## Parameter Capture

See the [views.md](views.md/#Path_Parameters) file.



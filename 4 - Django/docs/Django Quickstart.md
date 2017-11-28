# Django Quickstart


## Create a Project and App

- Create a site/project: `django-admin startproject <site/project name>`
- Move into the site's directory: `cd <site/project name>`
- Create an app: `python manage.py startapp <app-name>`

## Create a View

- In your app's `views.py` create a function `def <viewname>(request):`

## Create a Route to the View

- Create a `urls.py` inside your app
- Add a route in your app's `urls.py` which points to the the view
- Add an `app_name` to be able to reference URLs when you render a template

```python
from django.conf.urls import url
from . import views

app_name = '<app name>'
urlpatterns = [
    url(r'^$', views.<viewname>, name='<viewname>')
]
```
- Add a route in your project's `urls.py` which points to the app's `url.py` using `include`

```python
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^<path>/', include('<appname>.urls'))
]
```

- Add your app (`appname.apps.AppnameConfig`) to the `INSTALLED_APPS` in `settings.py`

## Create Models

- Define your models (Python classes) in the app's `models.py`
- Stage your migrations: `python manage.py makemigrations <appname>`
- (optional) View the SQL commands that will occur during migrations: `python manage.py sqlmigrate <appname> <migration number>`. You can find the migration number and the code that'll be executed during the migration in `<appname>/migrations/<migration number>_initial.py`
- Perform migrations (synchronize your models with your database): `python manage.py migrate`

## Set Up Admin Interface

- Create an admin account `python manage.py createsuperuser`
- Enter a username, email address, and password
- Add a `def __str__(self):` to your model so the admin interface knows how to show it.
- Make your app visible in the admin panel by registering your models with our app's `admin.py`

```python
from django.contrib import admin
from .models import <model name>
admin.site.register(<model name>)
```

- Go to `localhost/admin` in your browser


## Other Stuff

- Run the server: `python manage.py runserver`
- Access the shell `python manage.py shell`

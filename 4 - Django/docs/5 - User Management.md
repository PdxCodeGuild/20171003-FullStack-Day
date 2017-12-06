
# User Management

Many web applications have the ability for a user to 1) create an account, 2) log into and out of that account, and 3) view pages that are only accessible to logged-in users. For more info, read [here](https://docs.djangoproject.com/en/2.0/topics/auth/) and [here](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Authentication).


## Users, Groups, and Permissions

Start by looking at the users section of the admin interface. Here you can create users, groups, and assign permissions. A group is a collection of users which you can add and remove permisions from, so you don't have to go to each user to change their permissions. Django has many built-in permissions, but you can also define your own. For more information about these, look [here](https://docs.djangoproject.com/en/2.0/ref/contrib/auth/).

## Creating & Editing Users

You can create users programmatically using the 'create_user' function, which automatically creates a user and saves it. It's important to note that Django does not save passwords in 'plain text', only a hash of the password. This means you cannot retrieve a user's password, only check if the password you have is correct by putting it through the same hashing algorithm. You can read more about how Django manages passwords [here](https://docs.djangoproject.com/en/2.0/topics/auth/passwords/).

```python
from django.contrib.auth.models import User
user = User.objects.create_user('jane', 'jane@gmail.com', 'janespassword')
```

You can also create users from within the admin panel, by clicking 'add' next to 'Users' under 'AUTHENTICATION AND AUTHORIZATION'.


### Accessing Groups and Permissions

The `User` model has two many-to-many fields: groups and permissions. You can access these on the User object using the ORM. Note that `user_permissions` only include permissions assigned to that individual user, and not permissions that user has as part of a group. However, `has_perm` will check if the given permission is amony the group.

- `user.groups.set([group_list])` set the groups
- `user.groups.add(group, group, ...)` add to a group
- `user.groups.remove(group, group, ...)` remove from group
- `user.groups.clear()` remove from all groups
- `user.user_permissions.set([permission_list])` set permissions
- `user.user_permissions.add(permission, permission, ...)` add permissions
- `user.user_permissions.remove(permission, permission, ...)` remove permissions
- `user.user_permissions.clear()` clear all user permissions
- `user.has_perm(permission_code)` check if a user has a permission, either in user_permissions or in one of their groups

```python
from django.contrib.auth.models import User, Group, Permission

# add a user to a group
group = Group.objects.get(name='commenters')
user.groups.add(group)
user.save()

# add a permission to a group
permission = Permission.objects.get(codename='change_comment')
group.permissions.add(permission)
group.save()

# check if a user has a permission
if user.has_perm('blog.add_comment'):
    # ...


# check if a user is in a group
if user.groups.filter(name='commenters').exists():
    # ...
```

### Changing Passwords

You can change a user's password using `set_password` in Python or `changepassword` in the terminal. You can also change a user's password in the admin panel.

```python
from django.contrib.auth.models import User
user = User.objects.get(username='jane')
user.set_password('newpassword')
user.save()
``` 

```
python manage.py changepassword jane
```

## Authentication, Login, & Logout

To log a user in, we can use a form to post the username and password to a view. The `authenticate` function verifies their username and password are correct. If they are, it returns the user. If they aren't, it returns `None`. After verifying that the username and password match, we can log a user in using `login`.

```python
from django.contrib.auth import authenticate, login

def mylogin(request):
    # retrieve the variables from the form submission
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        # redirect to a success page
    else:
        # return an 'invalid login' error message
```

Logging out a user is even simpler.

```python
from django.contrib.auth import logout

def logout_view(request):
    logout(request)
    # redirect to a success page.
```

## Authorization

In other views, we can check if a user is logged in by checking the `is_authenticated` field.

```python
def otherview(request):
    if request.user.is_authenticated:
        # do something for authenticated users.
    else:
        # do something else for anonymous users.
```

If you want to restrict access to users with particular permissions, use `has_perm`.

```python
def otherview(request):
    if request.user.has_perm('blog.add_comment'):
        # do something for users with this permision
    else:
        # do something for everyone else
```

### @login_required

Django comes with a built-in decorator which can check if a user is logged in. If the user is logged in, the execution of the view coninues unabated. If not, the user will be redirected to [settings.LOGIN_URL](https://docs.djangoproject.com/en/1.11/ref/settings/#std:setting-LOGIN_URL). You can read more [here](https://docs.djangoproject.com/en/1.11/topics/auth/default/#the-login-required-decorator).

```python
from django.contrib.auth.decorators import login_required

@login_required
def my_view(request):
    ...
```

### @permission_required

Like `@login_required`, if this fails, the user will be redirected to [settings.LOGIN_URL](https://docs.djangoproject.com/en/1.11/ref/settings/#std:setting-LOGIN_URL).
You can read more [here](https://docs.djangoproject.com/en/1.11/topics/auth/default/#the-permission-required-decorator).

```python
from django.contrib.auth.decorators import permission_required

@permission_required('polls.can_vote')
def my_view(request):
    ...
```

### @user_passes_test(f)

The `@users_passes_test` decorator takes a function which is given a user. That function can then return `True` or `False` whether that user should be allowed in. Like the others, if this fails, the user will be redirected to [settings.LOGIN_URL](https://docs.djangoproject.com/en/1.11/ref/settings/#std:setting-LOGIN_URL). You can read more [here](https://docs.djangoproject.com/en/1.11/topics/auth/default/#limiting-access-to-logged-in-users-that-pass-a-test).


```python
from django.contrib.auth.decorators import user_passes_test

def email_check(user):
    return user.email.endswith('@example.com')

@user_passes_test(email_check)
def my_view(request):
    ...
```


## Extending the User Model

If you want to have a custom user model, you should create one **when you start a project**. It's much more difficult to change once you already have users in your database. You can read more [here](https://docs.djangoproject.com/en/1.11/topics/auth/customizing/#auth-custom-user).


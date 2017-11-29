
# Custom Management Commands

If you need to execute some Python code to perform administrative operations (load data into a database from a file or API, erase saved files, etc), you can write a custom management command. These are executed just like other management commands (`runserver`, `startapp`, `migrate`, etc).

To create a custom management command, first create a `management` folder inside your app. Inside of that, create a `commands` folder. Inside of that, create a `<command name>.py`. Inside your `<command name>.py`, write the following.

```python
from django.core.management.base import BaseCommand

class Command(BaseCommand):

    def handle(self, *args, **options):
        # write the code here
        pass
```

Now you can execute this function using `python manage.py <command name>`. Any parameters you write after the `<command name>` will be passed to the `handle` function.
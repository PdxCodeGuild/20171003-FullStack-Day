# VirtualEnv

Different Python applications will have different dependencies. A **virtualenv** is a way to isolate dependencies and swap them out quickly as we move between them.

A virtualenv is an isolated "installation" of Python and packages. It is just a **directory** that contains a "copy" of a Python interpreter, the standard library, an isolated set of installed packages, and some scripts to enable and disable itself.

When you **activate** a virtualenv, any commands that deal with Python or packages will only affect further commands inside the virtualenv. You should create a virtualenv for each separate project you're working on that needs packages.

Realize that virtualenv commands are totaly unrelated to Git commands. Changing your Git branch will not modify your virtualenv; changing your virtualenv will not dirty or commit or change Git branches.

## Installing

Virtualenv is also the name of the command to manage virtualenvs. You need to install it system-wide to be able to use it. You should only need to run this once on your computer.

```bash
pip install virtualenv
```

## Create

The first action is to **create** a new, empty virtualenv. I would recommend you use the name `venv`.

```bash
virtualenv venv
```

This will create a directory called `venv` in the working directory. You'll not need to modify this directory by hand.

## Activate

Once you've created a virtualenv, you can **activate** it. Source a script in the virtualenv directory.

On bash:
```bash
source venv/bin/activate
```

On PowerShell:
```
venv\Scripts\activate
```

Your prompt should change and show `(venv)` at the beginning to let you know you've activated. After you have activated a virtualenv, all `python` and `pip` commands will use **their virtualenv versions** and not the ones system-wide.

## Modifying Packages

Once a virtualenv has been activated, all [Pip commands](/notes/py-pip.md) modify that virtualenv. You don't need to worry about running `pip3` once activated.

## Running Python

Once a virtualenv has been activated, you can use `python` to run Python code. It will have access to all the installed packages in the virtualenv. You don't need to worry about running `python3` once activated.

## Freeze

**Freezing** is the process of taking all of the current packages and their versions and writing it out to `requirements.txt`. This is how you save the specific dependencies of your application.

```bash
pip freeze > requirements.txt
```

`>` is a special shell operator that takes the output of the previous command and writes it to a file. If you ever install more dependent packages, you should re-freeze.

## Deactivate

To exit your virtualenv, **deactivate** it. It is available only inside of the virtualenv. Your prompt should change back to normal showing you've deactivated.


```bash
deactivate
```

## Virtualenvs and PyCharm

When you make a new virtualenv, you can add it as the **selected interpreter** of a PyCharm project. Go to `Settings -> Project -> Project Interpreter` then select the drop-down menu and `Select All`. You can then click the plus `+` button to add a new interpreter, select the `venv/bin/python` file.
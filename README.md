# Django Local Test
This is a repo to test local changes to the Django framework.

## Steps to Recreate

Create the folder in wheverever it needs to be:

> -> mkdir django-local-test

Set the local Python version using `pyenv`:

> -> pyenv local 3.11

Make a virtual environment:

> -> python -m venv venv

Activate the new virtual environment:

> -> source venv/bin/activate

Create a `.gitignore` and paste what's in [here](https://github.com/github/gitignore/blob/main/Python.gitignore):

> -> touch .gitignore

Install your local version of Django:

> -> pip install -e path/to/django

Additionally, you can add this to your `requirements.txt` and then use `pip install requirements.txt`:

> -> echo "-e ../django" >> requirements.txt

Make Django project to test whatever you need:

> -> django-admin startproject cakeshop

> -> python manage.py startapp cakes

> -> python manage.py migrate

> -> python manage.py runserver

## Sources
I used two great blog posts to do this all really quickly!

- https://marijkeluttekes.dev/blog/articles/2024/01/25/a-simple-approach-to-running-django-core-locally/
- https://noumenal.es/notes/django/single-folder-layout/


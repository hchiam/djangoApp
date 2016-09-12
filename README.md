# My First Django App
Based on tutorial at [https://docs.djangoproject.com/en/1.10/intro/tutorial01/](https://docs.djangoproject.com/en/1.10/intro/tutorial01/)

## Usage:
1. Within terminal/commandline the the folder with manage.py in it.
2. Run the code in terminal or command-line: `python manage.py runserver`.  Alternatively, see the description on `python manage.py runserver 0.0.0.0:8000` at the [tutorial link](https://docs.djangoproject.com/en/1.10/intro/tutorial01/).
3. Visit [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your own browser to test it.

You can also visit (http://localhost:8000/polls/)[http://localhost:8000/polls/] to see the index view.

## Terminology:
App = does something.  can be in multiple projects.
Project = collection of configurations and apps for a particular website.  can contain multiple apps.

# Part 2:
Continue with [https://docs.djangoproject.com/en/1.10/intro/tutorial02/](https://docs.djangoproject.com/en/1.10/intro/tutorial02/)

## Three Steps to Make Model Changes:
1. Change your models in `models.py`.
2. Run the command `python manage.py makemigrations` to create migrations for those changes.
3. Run the command `python manage.py migrate` to apply those changes to the database.

Why are there separate commands?  To commit migrations to a version control system.

# Next Step:
"Introducing the Django Admin" [https://docs.djangoproject.com/en/1.10/intro/tutorial02/](https://docs.djangoproject.com/en/1.10/intro/tutorial02/)
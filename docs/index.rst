.. Flask-DJ documentation master file, created by
   sphinx-quickstart on Thu Mar  5 16:21:14 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Flask-DJ's documentation!
====================================
.. image:: https://img.shields.io/pypi/dd/Flask-DJ
    :target: https://pypi.org/project/Flask-DJ/

.. image:: https://img.shields.io/pypi/l/Flask-DJ
    :target: https://pypi.org/project/Flask-DJ/

.. image:: https://img.shields.io/pypi/pyversions/Flask-DJ
    :target: https://pypi.org/project/Flask-DJ/

Install package:
-------------------
::

$ pip install Flask-DJ

Hello world examle:
-------------------

Creating a project:
~~~~~~~~~~~~~~~~~~~
::

   # setup.py
   from Flask_DJ import ProjectConstructor
   from os import getcwd
   your_project_name = 'app'
   project_dir = getcwd()
   ProjectConstructor(your_project_name, project_dir).startproject()
   # if your project need templates and static files:
   # ProjectConstructor(your_project_name, project_dir, need_templates=True, need_static=True).startproject()

This will create a app directory in your project_dir with the following contents::

   app/
       app/
           __init__.py
           config.py
           urls.py
       manage.py

Creating the index app:
~~~~~~~~~~~~~~~~~~~
::

   $ python manage.py strtapp index

That`ll create a directory index, which is laid out like this::

   app/
       app/
           __init__.py
           config.py
           urls.py
       index/
             forms.py
             models.py
             urls.py
             views.py
       manage.py

Create view function:
~~~~~~~~~~~~~~~~~~~
::

   # index/views.py
   def index():
       return "Hello world"

Add start url:
~~~~~~~~~~~~~~~~~~~
Add to index app::

   # index/urls.py
   from utils.urls import relative_path
   from .views import index

   urlpatterns = [
       relative_path("", index),
   ]

Add to main app::

   # app/urls.py
   from utils.urls import add_relative_path, include

   urlpatterns = [
       add_relative_path("/", include("index.urls")),
   ]

Run project:
~~~~~~~~~~~~~~~~~~~
::

   $ python manage.py runserver


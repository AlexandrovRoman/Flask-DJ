Creating a project
~~~~~~~~~~~~~~~~~~~
.. code-block:: shell

    $ flask-dj startproject app

If your project need templates and static files

.. code-block:: shell

    $ startproject app -t -st

If something went wrong

.. code-block:: python

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

Creating the index app
~~~~~~~~~~~~~~~~~~~
.. code-block:: shell

   $ python manage.py startapp index

That`ll create a directory index, is shown below::

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

Create view function
~~~~~~~~~~~~~~~~~~~
.. code-block:: python

   # index/views.py
   def index():
       return "Hello world"

Add start url
~~~~~~~~~~~~~~~~~~~
Add to index application:

.. code-block:: python

   # index/urls.py
   from utils.urls import relative_path
   from .views import index

   urlpatterns = [
       relative_path("", index),
   ]

Add to main application:

.. code-block:: python

   # app/urls.py
   from utils.urls import add_relative_path, include

   urlpatterns = [
       add_relative_path("/", include("index.urls")),
   ]

Run project
~~~~~~~~~~~~~~~~~~~
.. code-block:: shell

   $ python manage.py runserver


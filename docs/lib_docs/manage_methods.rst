Manage:
-------------------

startapp {name}
~~~~~~~~~~~~~~~~~~~
Creates a folder {name} with forms, models, urls, views .py files

runserver
~~~~~~~~~~~~~~~~~~~
Runs your project

db {method}
~~~~~~~~~~~~~~~~~~~
`Full db documentation`_.

.. _`Full db documentation`: https://flask-migrate.readthedocs.io/en/latest/

init
""""""""""""""""""
Initializes database, should be runed before the first migration

migrate
""""""""""""""""""
Models migration.

Put all models in the models list before you start.

.. code-block:: python

    # {project}/config.py
    # add your file containing models
    models = [

    ]
    ...

upgrade
""""""""""""""""""
Upgrades your database

downgrade
""""""""""""""""""
Rollback to a previous migration

add custom methods
~~~~~~~~~~~~~~~~~~~
`Full flask-manager docs`_.

.. _`Full flask-manager docs`: https://flask-script.readthedocs.io/en/latest/

.. code-block:: python

    # manage.py
    ... manage.py default code
    @manage.manager.command
    def my_command(params):
        pass

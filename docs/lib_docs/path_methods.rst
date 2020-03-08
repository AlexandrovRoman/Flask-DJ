Path:
-------------------

relative_path
~~~~~~~~~~~~~~~~~~~
Brings the data to the format you need for the include

Use in your apps

add_relative_path
~~~~~~~~~~~~~~~~~~~
Activates URLs from apps

Use in {project_name}/urls.py only

include
~~~~~~~~~~~~~~~~~~~
Include your app URLs

add_absolute_path
~~~~~~~~~~~~~~~~~~~
Activates URLs directly

When using add to

.. code-block:: python

    # {project_name}/config.py
    ... Some code
    # Special urlpatterns
    urlpatterns = [
        '{project_name}.urls',
    ]
    ... Some code

Undesirable to use

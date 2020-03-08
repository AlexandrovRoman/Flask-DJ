Path:
-------------------

relative_path
~~~~~~~~~~~~~~~~~~~
Brings the data to the format you need for the include

Should be used in the applications

add_relative_path
~~~~~~~~~~~~~~~~~~~
Activates URLs from applications

Use it in {project_name}/urls.py only

include
~~~~~~~~~~~~~~~~~~~
Includes your application URLs

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

This path is undesirable to use

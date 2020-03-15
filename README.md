![image](docs/_static/flask-dj_logo.png)


# Flask-DJ
 
 Since the flask has no strict architecture, <br>
it's easy to get confused when creating a project.<br>
This library was created to help everyone who wants to <br>
create a project with mvc structure.<br>
 
 ## Quick start
 ### Install:
 pip install Flask-DJ
 ### Start project:
 
 ```shell script
$ flask-dj startproject app
```

or

 ```python
from Flask_DJ import ProjectConstructor
from os import getcwd

your_project_name = 'app'
ProjectConstructor(your_project_name, getcwd()).startproject()
```
 ### New app:
 
   ```shell script
 python manage.py startapp {app_name}
```

### Start server:

```shell script
 python manage.py runserver
```
 
 ## Useful links:
 pypi: https://pypi.org/project/Flask-DJ/<br>
 full docs: https://flask-dj.readthedocs.io/en/latest/

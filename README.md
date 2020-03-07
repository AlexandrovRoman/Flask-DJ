# Flask-DJ
 
 Since the flask has no strict project architecture, <br>
 it is easy for beginners to get confused when creating an application.<br>
 This library was created to help everyone who wants to create a small application.<br>
 
 ## Quick start
 ### Install:
 pip install Flask-DJ
 ### Start app:

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
 
 ## View more info in:
 pypi: https://pypi.org/project/Flask-DJ/<br>
 full docs: https://flask-dj.readthedocs.io/en/latest/

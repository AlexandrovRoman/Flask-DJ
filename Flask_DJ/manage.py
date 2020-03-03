from flask_migrate import MigrateCommand
from flask_script import Manager
from importlib import import_module
from Flask_DJ.templates import views_file, models_file, urls_file, forms_file
from waitress import serve

from .docs import urls_docs
from .utils import get_project_name, create_folder, create_file

"""database-methods: https://flask-migrate.readthedocs.io/en/latest/"""
manager = None
app_ = None

commands = [
    'startapp',
]


def init_manage(app):
    global manager, app_
    app_ = app
    manager = Manager(app)


def init_db(models=[]):
    manager.add_command('db', MigrateCommand)
    for file in models:
        import_module(file)


def runserver(host, port):
    if app_.debug:
        app_.run(host=host, port=port)
    else:
        serve(app_, host=host, port=port)


def create_app_files(app_name):
    project_name = get_project_name()
    create_file(app_name, 'views', views_file)
    create_file(app_name, 'models', models_file.format(project_name=project_name))
    create_file(app_name, 'urls', urls_file.format(docs=urls_docs, project_name=project_name))
    create_file(app_name, 'forms', forms_file)


def startapp(name):
    """Create folder containing forms.py, models.py, urls.py, views.py"""
    create_folder(name)
    create_app_files(name)
    print(f'app {name} created')

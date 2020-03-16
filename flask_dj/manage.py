from flask_migrate import MigrateCommand
from flask_script import Manager
from importlib import import_module
from flask_dj.templates import views_file, models_file, urls_file, forms_file
from waitress import serve
from os.path import join
from .utils import get_project_name, create_folder, create_file, valid_folder_name

"""database-methods: https://flask-migrate.readthedocs.io/en/latest/"""
manager = None
app_ = None

commands = [

]


def init_manage_and_app(app):
    global manager, app_
    app_ = app
    manager = Manager(app)


def init_db_commands(models=[]):
    manager.add_command('db', MigrateCommand)

    for file in models:
        import_module(file)


def runserver(host, port):
    app_.run(host=host, port=port) if app_.debug else serve(app_, host=host, port=port)


def startapp(templates, static, name):
    """Create folder containing forms.py, models.py, urls.py, views.py"""
    valid_folder_name(name)

    create_folder(name)
    create_app_files(name)

    if templates:
        create_app_templates(name)
    if static:
        create_app_static(name)

    print(f'app {name} created')


def create_app_files(app_name):
    """Create .py files for your app"""
    project_name = get_project_name()

    create_file(app_name, 'views', views_file)
    create_file(app_name, 'models', models_file.format(project_name=project_name))
    create_file(app_name, 'urls', urls_file.format(functions="relative_path"))
    create_file(app_name, 'forms', forms_file)


def create_app_templates(app_name):
    create_folder(join("templates", app_name))


def create_app_static(app_name):
    create_folder(join("static", app_name))

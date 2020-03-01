from os import getcwd, mkdir
from os.path import exists
from flask_migrate import MigrateCommand
from flask_script import Manager
from importlib import import_module
from . import CreationError
from Flask_DJ.templates import views_file, models_file, urls_file, forms_file
from waitress import serve

"""database-methods: https://flask-migrate.readthedocs.io/en/latest/
some methods:
runserver - start server
startapp name - create folder containing forms.py, models.py, urls.py, views.py, 
"""
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


def create_dir(name):
    try:
        mkdir(name)
    except (FileNotFoundError, PermissionError):
        raise CreationError('Не удается создать директорию с данным именем')


def create_files(name):
    with open(f'{name}/views.py', 'w') as f:
        f.write(views_file)
    with open(f'{name}/models.py', 'w') as f:
        f.write(models_file.format(project=getcwd().split('\\')[-1]))
    with open(f'{name}/urls.py', 'w') as f:
        f.write(urls_file)
    with open(f'{name}/forms.py', 'w') as f:
        f.write(forms_file)


def warning_handler(message):
    commands = {1: lambda: None, 2: exit}
    try:
        commands[int(input(f'{message}\n1. Yes\n2. No'))]()
    except (ValueError, KeyError):
        print('Incorrect input')
        exit(1)


def startapp(name):
    if exists(name):
        warning_handler('Директория с данным именем уже существует, все равно создать?')
    else:
        create_dir(name)
    create_files(name)
    print(f'app {name} created')

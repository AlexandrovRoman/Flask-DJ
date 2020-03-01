from os import makedirs
from os.path import exists
from flask_migrate import MigrateCommand
from flask_script import Manager
from importlib import import_module

"""database-methods: https://flask-migrate.readthedocs.io/en/latest/
db init - начало поддержки миграций
db migrate - миграция бд
db upgrade - обновление бд
db downgrade - откат миграции
some methods:
runserver - запуск сервера
startapp name - создание приложения name
new_user_has_full_data surname, name, fathername, birth_year, birth_month, birth_day, age, email, password, sex - 
создание пользователя с заданными параметрами
new_default_user mail, password - создание пользователя с дефолтными параметрами
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


def runserver():  # TODO: Production config
    app_.run()


def startapp(name):
    if not exists(name):
        makedirs(name)
    with open(f'{name}/views.py', 'w') as f:
        f.write('# Create your views functions or classes\n')
    with open(f'{name}/models.py', 'w') as f:
        f.write('from app import db\n\n# Create your models\n')  # TODO: Заменить app на нужную папку
    with open(f'{name}/urls.py', 'w') as f:
        f.write('from Flask_DJ.utils.urls import path\n\n# Add your urls\nurlpatterns = [\n    \n]\n')
    with open(f'{name}/forms.py', 'w') as f:
        f.write('from flask_wtf import FlaskForm\nimport wtforms\n\n# Create your forms\n')
    print(f'app {name} created')


if __name__ == '__main__':
    manager.run()

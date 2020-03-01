from os import makedirs, mkdir
from Flask_DJ.exceptions import CreationError
from Flask_DJ.templates import config_file, init_file, urls_file, manage_file
from string import ascii_letters
from random import choices, randint
from sys import argv


def create_file(path, name, template):
    with open(f'{path}\\{name}.py', 'w') as f:
        f.write(template)


def create_init(app_path):
    create_file(app_path, '__init__', init_file)


def generate_key(length):
    return "".join(choices(ascii_letters, k=length))


def create_config(app_path):
    create_file(app_path, 'config',
                config_file.format(csrf=generate_key(randint(9, 12)), secret_key=generate_key(randint(9, 12))))


def create_urls(app_path):
    create_file(app_path, 'urls', urls_file)


def create_main(path, name):
    app_path = f'{path}\\{name}'
    mkdir(app_path)
    create_init(app_path)
    create_config(app_path)
    create_urls(app_path)


def create_manage(path, name):
    create_file(path, 'manage', manage_file.format(project_name=name))


def create_path(name, path):
    try:
        project_path = f'{path}\\{name}' if path else name
        makedirs(project_path)
        return project_path
    except FileExistsError:
        raise CreationError('Директория с таким именем уже существует')
    except PermissionError:
        raise CreationError('У вас недостаточно прав для действий в данной директории, '
                            'попробуйте сменить пользователя и повтрить попытку')


def get_name(name):
    try:
        return name or argv[1]
    except IndexError:
        raise ValueError("Argument name is underfind")


def start(name=None, path=''):
    name = get_name(name)
    project_path = create_path(name, path)
    create_main(project_path, name)
    create_manage(project_path, name)

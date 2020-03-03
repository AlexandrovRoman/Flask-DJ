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


def create_urls(app_path, project_name):
    create_file(app_path, 'urls', urls_file.format(project_name=project_name))


def create_main(path, project_name):
    app_path = f'{path}\\{project_name}'
    mkdir(app_path)
    create_init(app_path)
    create_config(app_path)
    create_urls(app_path, project_name)


def create_manage(path, project_name):
    create_file(path, 'manage', manage_file.format(project_name=project_name))


def create_path(project_name, path):
    try:
        project_path = f'{path}\\{project_name}' if path else project_name
        makedirs(project_path)
        return project_path
    except FileExistsError:
        raise CreationError('The directory with that name already exists.')
    except PermissionError:
        raise CreationError('You do not have enough permissions to act in this directory, '
                            'try changing users and try again.')


def get_name(project_name):
    try:
        return project_name or argv[1]
    except IndexError:
        raise ValueError("project_name is not defined")


def start(project_name=None, path=''):
    project_name = get_name(project_name)
    project_path = create_path(project_name, path)
    create_main(project_path, project_name)
    create_manage(project_path, project_name)

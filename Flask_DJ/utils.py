from os.path import join, split
from os import makedirs, getcwd
from string import ascii_letters, digits
from flask_dj.exceptions import CreationError


def create_file(path, name, template):
    with open(join(path, f'{name}.py'), 'w') as f:
        f.write(template)


def create_folder(path):
    try:
        makedirs(path)
    except FileExistsError:
        raise CreationError('The directory with that name already exists.')
    except PermissionError:
        raise CreationError('You do not have enough permissions to act in this directory, '
                            'try changing users and try again.')


def get_project_name():
    return split(getcwd())[-1]


def valid_folder_name(name):
    if set(name).issubset(set(ascii_letters + digits + "_")) and name[0] not in digits:
        return
    raise ValueError("Invalid name")

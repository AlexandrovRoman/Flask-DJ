from os.path import join, split
from os import makedirs, getcwd
from Flask_DJ.exceptions import CreationError


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

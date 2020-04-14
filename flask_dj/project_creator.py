from argparse import ArgumentParser
from typing import Iterable
from flask_dj.templates import config_file, init_file, urls_file, manage_file, utils_urls
from string import ascii_letters
from random import choices, randint
from sys import argv
from os.path import join
from ._utils import create_file, create_folder, valid_folder_name


class ProjectConstructor:
    """
    Your project creator
    :param project_name: str
    :param path: str
    :param need_templates: bool - Do you need to create the templates folder
    :param need_static: bool - Do you need to create the static folder
    """
    def __init__(self, project_name=None, path='', need_templates=False, need_static=False):
        self.path = path
        self.project_name = project_name
        valid_folder_name(project_name)
        self.project_path = join(self.path, self.project_name) if self.path else self.project_name
        self.main_app_path = join(self.project_path, self.project_name)
        self.need_templates = need_templates
        self.need_static = need_static

    def startproject(self):
        self._create_project_folder()
        self._create_main()
        self._create_manage()
        self._create_utils()
        if self.need_templates:
            self._create_templates()
        if self.need_static:
            self._create_static()

    def _create_project_folder(self):
        create_folder(self.project_path)

    def _create_main(self):
        self._create_main_app_folder()
        self._create_init()
        self._create_config()
        self._create_urls()

    def _create_main_app_folder(self):
        create_folder(self.main_app_path)

    def _create_init(self):
        create_file(self.main_app_path, '__init__', init_file)

    def _create_config(self):
        create_file(self.main_app_path, 'config',
                    config_file.format(project_name=self.project_name, csrf=self.generate_key(randint(9, 12)),
                                       secret_key=self.generate_key(randint(9, 12))))

    @staticmethod
    def generate_key(length: int):
        return "".join(choices(ascii_letters, k=length))

    def _create_urls(self):
        create_file(self.main_app_path, 'urls', urls_file.format(functions="add_relative_path, include"))

    def _create_manage(self):
        create_file(self.project_path, 'manage',
                    manage_file.format(project_name=self.project_name))

    def _create_utils(self):
        self._create_utils_folder()
        self._create_utils_urls()

    def _create_utils_folder(self):
        create_folder(join(self.project_path, 'utils'))

    def _create_utils_urls(self):
        create_file(join(self.project_path, 'utils'), 'urls', utils_urls.format(project_name=self.project_name))

    def _create_templates(self):
        create_folder(join(self.project_path, 'templates'))

    def _create_static(self):
        create_folder(join(self.project_path, 'static'))


def command():
    commands = {
        'startproject': console_creation
    }

    try:
        commands[argv[1]]()
    except KeyError:
        print("Input correct command")
        print_commands(commands)
    except IndexError:
        print("Input command")
        print_commands(commands)


def console_creation():
    parser = ArgumentParser()
    parser.add_argument("command")
    parser.add_argument("project_name")
    parser.add_argument("--templates", "-t", action="store_true", default=False)
    parser.add_argument("--static", "-st", action="store_true", default=False)
    args = parser.parse_args()

    startproject(args.project_name, need_templates=args.templates, need_static=args.static)


def startproject(project_name, path="", need_templates=False, need_static=False):
    ProjectConstructor(project_name, path, need_templates, need_static).startproject()


def print_commands(commands: Iterable):
    for key in commands:
        print(f"\t\t{key}")

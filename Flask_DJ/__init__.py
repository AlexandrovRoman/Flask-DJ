from os import makedirs, mkdir
from Flask_DJ.exceptions import CreationError
from Flask_DJ.templates import config_file, init_file, urls_file, manage_file
from string import ascii_letters
from random import choices, randint
from sys import argv
from .utils import create_file


class ProjectConstructor:
    """
    Create your project
    :param project_name: str
    :param path: str
    :param need_templates: bool - Do you need to create the templates folder
    :param need_static: bool - Do you need to create the static folder
    """
    def __init__(self, project_name=None, path='', need_templates=False, need_static=False):
        self.path = path
        self.project_name = self.get_project_name(project_name)
        self.project_path = f'{self.path}\\{self.project_name}' if self.path else self.project_name
        self.main_app_path = f'{self.project_path}\\{project_name}'
        self.need_templates = need_templates
        self.need_static = need_static

    @staticmethod
    def get_project_name(project_name):
        try:
            return project_name or argv[1]
        except IndexError:
            raise ValueError("project_name is not defined")

    def _create_init(self):
        create_file(self.main_app_path, '__init__', init_file)

    @staticmethod
    def generate_key(length):
        return "".join(choices(ascii_letters, k=length))

    def _create_config(self):
        create_file(self.main_app_path, 'config',
                    config_file.format(csrf=self.generate_key(randint(9, 12)),
                                       secret_key=self.generate_key(randint(9, 12))))

    def _create_urls(self):
        create_file(self.main_app_path, 'urls', urls_file.format(project_name=self.project_name))

    def _create_main_app_folder(self):
        mkdir(self.main_app_path)

    def _create_templates(self):
        mkdir(f'{self.project_path}\\templates')

    def _create_static(self):
        mkdir(f'{self.project_path}\\static')

    def _create_main(self):
        self._create_main_app_folder()
        self._create_init()
        self._create_config()
        self._create_urls()

    def _create_manage(self):
        create_file(self.path, 'manage', manage_file.format(project_name=self.project_name))

    def _create_project_folder(self):
        try:
            makedirs(self.project_path)
        except FileExistsError:
            raise CreationError('The directory with that name already exists.')
        except PermissionError:
            raise CreationError('You do not have enough permissions to act in this directory, '
                                'try changing users and try again.')

    def startproject(self):
        self._create_project_folder()
        self._create_main()
        self._create_manage()
        if self.need_templates:
            self._create_templates()
        if self.need_static:
            self._create_static()

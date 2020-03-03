from Flask_DJ.exceptions import CreationError
from Flask_DJ.templates import config_file, init_file, urls_file, manage_file, utils_urls
from string import ascii_letters
from random import choices, randint
from sys import argv
from .docs import urls_docs, manage_docs
from .utils import create_file, create_folder, format_docs


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
        create_file(self.main_app_path, 'urls', urls_file.format(docs=format_docs(urls_docs)))

    def _create_main_app_folder(self):
        create_folder(self.main_app_path)

    def _create_templates(self):
        create_folder(f'{self.project_path}\\templates')

    def _create_static(self):
        create_folder(f'{self.project_path}\\static')

    def _create_main(self):
        self._create_main_app_folder()
        self._create_init()
        self._create_config()
        self._create_urls()

    def _create_manage(self):
        create_file(self.path, 'manage',
                    manage_file.format(docs=format_docs(manage_docs), project_name=self.project_name))

    def _create_project_folder(self):
        create_folder(self.project_path)

    def _create_utils_folder(self):
        create_folder(f'{self.project_path}\\utils')

    def _create_utils_urls(self):
        create_file(f'{self.project_path}\\utils', 'urls', utils_urls.format(project_name=self.project_name))

    def startproject(self):
        self._create_project_folder()
        self._create_main()
        self._create_manage()
        if self.need_templates:
            self._create_templates()
        if self.need_static:
            self._create_static()

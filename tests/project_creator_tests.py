from os import getcwd
from shutil import rmtree
from os.path import exists, join
from Flask_DJ import ProjectConstructor
from string import ascii_letters
from random import choices


class TestBaseSettingProjectConstructor:
    def setup(self, need_templates=False, need_static=False):
        self.need_templates = need_templates
        self.need_static = need_static
        self.cwd = getcwd()
        self.project_name = ''.join(choices(ascii_letters, k=12))
        self.project_path = join(self.cwd, self.project_name)
        ProjectConstructor(self.project_name, self.cwd, self.need_templates, self.need_static).startproject()

    def test_project_folder_exist(self):
        assert exists(self.project_path)

    def test_main_folder_exist(self):
        assert exists(join(self.project_path, self.project_name))

    def main_file_test(self, filename, test_contents=['']):
        self._file_test(self.project_name, filename, test_contents)

    def _file_test(self, folder, filename, test_contents=['']):
        test_path = join(join(self.project_path, folder), f'{filename}.py')
        assert exists(test_path)
        with open(test_path) as f:
            file_content = f.read()
            assert all([test_content in file_content for test_content in test_contents])

    def test_main_init(self):
        self.main_file_test('__init__', ['from flask import Flask', 'from flask_login import LoginManager'])

    def test_main_config(self):
        self.main_file_test('config', ["HOST = '127.0.0.1'", "PORT = 5000", "Config = DevelopConfig"])

    def test_main_urls(self):
        assert exists(join(join(self.project_path, self.project_name), 'urls.py'))

    def test_main_manage(self):
        self._file_test(self.project_path, 'manage', [f'from {self.project_name} import app, config'])

    def test_utils_folder_exist(self):
        assert exists(join(self.project_path, 'utils'))

    def test_utils_urls(self):
        self._file_test('utils', 'urls', [f'from {self.project_name} import app'])

    def test_templates_folder(self):
        assert exists(join(self.project_path, 'templates')) or not self.need_templates

    def test_static_folder(self):
        assert exists(join(self.project_path, 'static')) or not self.need_static

    def teardown(self):
        rmtree(self.project_path)


class TestAdvancedProjectConfig(TestBaseSettingProjectConstructor):
    def setup(self, need_templates=False, need_static=False):
        super().setup(True, True)

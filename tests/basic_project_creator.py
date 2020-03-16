from os import getcwd
from os.path import join, exists
from random import choices
from shutil import rmtree
from string import ascii_letters
from flask_dj import startproject


class ProjectCreate:
    def setup(self, need_templates=False, need_static=False):
        self.need_templates = need_templates
        self.need_static = need_static
        self.cwd = getcwd()
        self.project_name = ''.join(choices(ascii_letters, k=12))
        self.project_path = join(self.cwd, self.project_name)
        startproject(self.project_name, self.cwd, self.need_templates, self.need_static)

    def _file_test(self, folder, filename, test_contents=['']):
        test_path = join(join(self.project_path, folder), f'{filename}.py')
        assert exists(test_path)
        with open(test_path) as f:
            file_content = f.read()
            assert all([test_content in file_content for test_content in test_contents])

    def teardown(self):
        rmtree(self.project_path)

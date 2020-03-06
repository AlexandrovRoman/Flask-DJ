from os import chdir
from os.path import exists, join, split
from tests.basic_project_creator import ProjectCreate
from Flask_DJ.manage import startapp


class TestManage(ProjectCreate):
    def setup(self, need_templates=False, need_static=False):
        super().setup(need_templates, need_static)
        app_name = 'index'
        self.app_path = join(self.project_path, app_name)
        chdir(self.project_path)
        startapp(app_name)

    def test_startapp_folder(self):
        assert exists(self.app_path)

    def test_startapp_models(self):
        self._file_test(self.app_path, 'models', [f"from {self.project_name} import db", "# Create your models"])

    def test_startapp_urls(self):
        self._file_test(self.app_path, 'urls', ["from utils.urls import get_relative_path, add_absolute_path"])

    def test_startapp_forms(self):
        self._file_test(self.app_path, 'forms', ["from flask_wtf import FlaskForm", "import wtforms"])

    def test_startapp_views(self):
        self._file_test(self.app_path, 'views', ["# Create your views functions or classes\n"])

    def teardown(self):
        chdir(split(self.project_path)[0])
        super().teardown()

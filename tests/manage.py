import os
from os import chdir, system
from os.path import exists, join, split
from multiprocessing import Process

from tests.basic_project_creator import ProjectCreate
import requests


class BaseManage(ProjectCreate):
    def setup(self):
        super().setup()
        app_name = 'index'
        self.app_path = join(self.project_path, app_name)
        chdir(self.project_path)
        self.interpretator = r"C:\Users\AlexandrovRoman\Documents\GitHub\Flask-DJ\venv\Scripts\python"
        system(f"{self.interpretator} manage.py startapp {app_name}")

    def teardown(self):
        chdir(split(self.project_path)[0])
        try_count = 0
        while True:
            try:
                super().teardown()
            except (OSError, PermissionError):
                if try_count == 100:
                    raise RecursionError
                try_count += 1
            else:
                break


class TestManageStartapp(BaseManage):
    def test_startapp_folder(self):
        assert exists(self.app_path)

    def test_startapp_models(self):
        self._file_test(self.app_path, 'models', [f"from {self.project_name} import db", "# Create your models"])

    def test_startapp_urls(self):
        self._file_test(self.app_path, 'urls', ["from utils.urls import relative_path"])

    def test_startapp_forms(self):
        self._file_test(self.app_path, 'forms', ["from flask_wtf import FlaskForm", "import wtforms"])

    def test_startapp_views(self):
        self._file_test(self.app_path, 'views', ["# Create your views functions or classes\n"])


class TestManageRunserver(BaseManage):
    def setup(self):
        super().setup()
        self.edit_app()
        self.server = Process(target=system, args=(f"{self.interpretator} manage.py runserver",), daemon=True)
        self.server.start()

    def edit_app(self):
        with open(join(self.app_path, "views.py"), "a") as f:
            f.write("def index():\n    return 'Hello world'")
        app_urls = """from utils.urls import relative_path
from .views import index
            
urlpatterns = [
    relative_path('', index)
]
"""
        with open(join(self.app_path, "urls.py"), "w") as f:
            f.write(app_urls)
        with open(join(self.project_path, self.project_name, "urls.py"), "w") as f:
            f.write(f"""from utils.urls import add_relative_path, include
            
urlpatterns = [add_relative_path('/', include('index.urls'))]
""")

    def test_connection(self):
        res = requests.get("http://127.0.0.1:5000/")
        with open("log.txt", "w") as f:
            f.write(res.text)
        assert res.status_code == 200

    def teardown(self):
        self.server.terminate()
        self.server.join()
        super().teardown()

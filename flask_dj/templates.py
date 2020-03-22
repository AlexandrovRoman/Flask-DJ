config_file = """# add your file containing models
models = [
    
]
# Special urlpatterns
urlpatterns = [
    '{project_name}.urls',
]

HOST = '127.0.0.1'
PORT = 5000


class BaseConfig:
    WTF_CSRF_SECRET_KEY = '{csrf}'
    SECRET_KEY = '{secret_key}'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///app.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(BaseConfig):
    DEBUG = False
    CSRF_ENABLED = True


class DevelopConfig(BaseConfig):
    DEBUG = True
    ASSETS_DEBUG = True


Config = DevelopConfig
"""

init_file = """import sqlalchemy.ext.declarative as dec
from flask import Flask
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_dj.app_init import create_session
from .config import Config

app = Flask('__main__')
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

SqlAlchemyBase = dec.declarative_base()

login_manager = LoginManager()
login_manager.init_app(app)
session = create_session(Config.SQLALCHEMY_DATABASE_URI, SqlAlchemyBase)
"""

manage_file = """from flask_dj import manage
from flask_dj.app_init import add_urls
from {project_name} import app, config

manage.init_manage_and_app(app)
manage.init_db_commands(config.models)

manage.manager.option("--templates", "-t", action="store_true")(
    manage.manager.option("--static", "-st", action="store_true")(
        manage.manager.option("name")(manage.startapp)))


@manage.manager.command
def runserver():
    add_urls(config.urlpatterns)
    manage.runserver(config.HOST, config.PORT)


manage.manager.run()
"""

views_file = "# Create your views functions or classes\n"

models_file = """from {project_name} import db

# Create your models
"""

forms_file = """from flask_wtf import FlaskForm
import wtforms

# Create your forms
"""

urls_file = """from utils.urls import {functions}

# Add your urls
urlpatterns = [
    
]
"""

utils_urls = """# View only file
from {project_name} import app
from flask_dj import urls

_path = urls.Path(app)
add_absolute_path = _path.add_absolute_path
add_relative_path = _path.add_relative_path
relative_path = _path.relative_path
include = urls.include
"""

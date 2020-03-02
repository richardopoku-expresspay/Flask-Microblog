from flask import Flask
from config.instance import app_config
import os
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object(app_config[os.getenv('APP_SETTINGS')])
app.config.from_pyfile('../config/instance.py')
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)

from app import routes, models
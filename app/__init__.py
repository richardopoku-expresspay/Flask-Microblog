from flask import Flask
from config.instance import app_config
import os
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand

app = Flask(__name__)
app.config.from_object(app_config[os.getenv('APP_SETTINGS')])
app.config.from_pyfile('../config/instance.py')
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes, models
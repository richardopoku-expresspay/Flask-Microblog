from flask import Flask
from config.instance import app_config
import os

app = Flask(__name__)
app.config.from_object(app_config[os.getenv('APP_SETTINGS')])
app.config.from_pyfile('../config/instance.py')

from app import routes
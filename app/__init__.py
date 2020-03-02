from flask import Flask
from config.instance import app_config

app = Flask(__name__)
app.config.from_object(app_config)
app.config.from_pyfile('../config/instance.py')

from app import routes
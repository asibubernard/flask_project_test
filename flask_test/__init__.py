from flask import Flask
from config import Config
import logging 
from logging.handlers import SMTPHandler
from flask_mail import Mail # new

app = Flask(__name__)
app.config.from_object(Config)
mail = Mail(app)  # new

from flask_test import routes


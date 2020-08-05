from flask import Flask
from config import Config# new

app = Flask(__name__)
app.config.from_object(Config) # new 

from flask_test import routes


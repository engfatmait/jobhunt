"""
The flask application package.
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, instance_relative_config=True)

app.config['SECRET_KEY'] = 'hello' 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///jobs.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
app.app_context().push()

from jobhunt import views
import jobhunt.models
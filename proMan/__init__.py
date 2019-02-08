import os, sys
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import sqlite3

# SQLite URI compatible
WIN = sys.platform.startswith('win')
if WIN:
    prefix = 'sqlite:///'
else:
    prefix = 'sqlite:////'

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = prefix + os.path.join(os.path.dirname(app.root_path), os.getenv('DATABASE_FILE', 'data.db'))
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev')
db = SQLAlchemy(app)

# 注册环境变量
@app.context_processor
def inject_person():
    from proMan.models import Person, Project
    person = 'admin' # Person.query.filter_by(name='admin').first()
    projects = Project.query.all()# person.projects
    return dict(person=person, projects=projects)

from proMan import views, errors, commands

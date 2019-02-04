from proMan import db

'''
single:
Project
Task

relationship:
ProjectPerson
ProjectTask

'''

class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    projects = db.relationship('Project', backref='person', lazy=True)

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    person_id = db.Column(db.Integer, db.ForeignKey('person.id'))

class Task(db.Model):
    task_id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(20))
    project_id = db.Column(db.Integer)
    project = db.Column(db.String(20))
    resource = db.Column(db.String(50))
    start_date = db.Column(db.String(10))
    end_date = db.Column(db.String(10))
    duration = db.Column(db.Integer)
    pct_complete = db.Column(db.Integer)
    dependencies = db.Column(db.String(50))

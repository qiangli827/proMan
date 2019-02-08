from proMan import db

'''
table:
Person
Project
Task


relationship:
ProjectPerson, n:m
ProjectTask, 1:n
'''

ProjectPerson = db.Table('ProjectPerson',
    db.Column('project_id', db.Integer, db.ForeignKey('project.id'), primary_key=True),
    db.Column('person_id', db.Integer, db.ForeignKey('person.id'), primary_key=True)
)

class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    projects = db.relationship('Project', secondary=ProjectPerson, lazy='subquery',
        backref=db.backref('persons', lazy=True))

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    tasks = db.relationship('Task', backref='project', lazy='dynamic')

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    resource = db.Column(db.String(50))
    start_date = db.Column(db.String(10))
    end_date = db.Column(db.String(10))
    duration = db.Column(db.Integer)
    pct_complete = db.Column(db.Integer)
    dependencies = db.Column(db.String(50))
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'))

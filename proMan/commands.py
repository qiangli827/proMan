import click
from proMan import app, db
from proMan.models import Task, Person, Project

@app.cli.command()
@click.option('--drop', is_flag=True, help='Create after drop.')
def initdb(drop):
    """Initialize the database."""
    if drop:
        db.drop_all()
    db.create_all()
    click.echo('Initialized database.')

@app.cli.command()
def populate_data():
    """Populate fake data to database."""

    db.drop_all()
    db.create_all()

    # person
    persons = ['jacky', 'bradly', 'katty']
    for p in persons:
        person = Person(name=p)
        db.session.add(person)
    db.session.commit()

    # project
    projects = ['p1', 'p2', 'p3', 'p4', 'p5', 'p6', 'p7', 'p8', 'p9']
    for pjt in projects:
        project = Project(name=pjt)
        db.session.add(project)
    db.session.commit()

    # many to many relationship: PersonProject
    p_dict = {}
    pjt_dict = {}
    for p in persons:
        p_obj = Person.query.filter_by(name=p).first()
        p_dict[p] = p_obj
    for pjt in projects:
        pjt_obj = Project.query.filter_by(name=pjt).first()
        pjt_dict[pjt] = pjt_obj
    p_dict['katty'].projects = list(pjt_dict.values())
    pjt_dict['p1'].persons = list(p_dict.values())
    db.session.commit()

    # task
    tasks = [
        dict(name = '整理资料',
             resource = '人力,物力,财力',
             start_date = '2019/1/1',
             end_date = '2019/2/28',
             duration = 59,
             pct_complete = 60,
             dependencies = ''),
        dict(name = '清点物资',
             resource = '人力,物力',
             start_date = '2019/1/5',
             end_date = '2019/2/25',
             duration = 50,
             pct_complete = 70,
             dependencies = ''),
        dict(name = '人员安排',
             resource = '人力',
             start_date = '2019/1/1',
             end_date = '2019/2/28',
             duration = 59,
             pct_complete = 65,
             dependencies = ''),
        dict(name = '招投标',
             resource = '人力,物力,财力',
             start_date = '2019/2/1',
             end_date = '2019/3/31',
             duration = 59,
             pct_complete = 10,
             dependencies = ''),
        dict(name = '设备进场',
             resource = '人力,物力,财力',
             start_date = '2019/4/1',
             end_date = '2019/4/30',
             duration = 30,
             pct_complete = 0,
             dependencies = '')
    ]
    for t in tasks:
        task = Task(name=t['name'],
                    resource=t['resource'],
                    start_date=t['start_date'],
                    end_date=t['end_date'],
                    duration=t['duration'],
                    pct_complete=t['pct_complete'],
                    dependencies=t['dependencies'])
        db.session.add(task)
    db.session.commit()

    task_name = ['整理资料', '清点物资', '人员安排', '招投标', '设备进场']
    task_dict = {}
    for t in task_name:
        t_obj = Task.query.filter_by(name=t).first()
        task_dict[t] = t_obj
    pjt_dict['p1'].tasks = list(task_dict.values())[0:3]
    pjt_dict['p2'].tasks = list(task_dict.values())[3:5]
    db.session.commit()

    click.echo('Done.')

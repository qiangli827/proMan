import click
from proMan import app, db
from proMan.models import Task

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

    tasks = [
        dict(task = '整理资料',
             project_id = 1,
             project = '项目 - 01',
             resource = '人力,物力,财力',
             start_date = '2019/1/1',
             end_date = '2019/2/28',
             duration = 59,
             pct_complete = 60,
             dependencies = ''),
        dict(task = '清点物资',
             project_id = 1,
             project = '项目 - 01',
             resource = '人力,物力',
             start_date = '2019/1/5',
             end_date = '2019/2/25',
             duration = 50,
             pct_complete = 70,
             dependencies = '整理资料'),
        dict(task = '人员安排',
             project_id = 1,
             project = '项目 - 01',
             resource = '人力',
             start_date = '2019/1/1',
             end_date = '2019/2/28',
             duration = 59,
             pct_complete = 65,
             dependencies = ''),
        dict(task = '招投标',
             project_id = 2,
             project = '项目 - 02',
             resource = '人力,物力,财力',
             start_date = '2019/2/1',
             end_date = '2019/3/31',
             duration = 59,
             pct_complete = 10,
             dependencies = ''),
        dict(task = '设备进场',
             project_id = 2,
             project = '项目 - 02',
             resource = '人力,物力,财力',
             start_date = '2019/4/1',
             end_date = '2019/4/30',
             duration = 30,
             pct_complete = 0,
             dependencies = '招投标')
    ]

    for t in tasks:
        task = Task(task=t['task'],
                    project_id=t['project_id'],
                    project=t['project'],
                    resource=t['resource'],
                    start_date=t['start_date'],
                    end_date=t['end_date'],
                    duration=t['duration'],
                    pct_complete=t['pct_complete'],
                    dependencies=t['dependencies'])
        db.session.add(task)

    db.session.commit()
    click.echo('Done.')

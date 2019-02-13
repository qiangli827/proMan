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
    projects = ['IB01项目', '细分行业1', '细分行业2', '细分行业3', '细分行业4', '细分行业5', '细分行业6', '细分行业7', '细分行业8', '细分行业9']
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
    pjt_dict['细分行业1'].persons = list(p_dict.values())
    db.session.commit()

    # 任务
    tasks = [
        ['任务/里程碑', '工期', '开始', '结束'],
        ['碧桂园战略合作协议签署', '1', '2018-01-01', '2018-01-02'],
        ['IB01项目组成立', '17', '2018-01-03', '2018-01-20'],
        ['项目组业绩梳理', '3', '2018-01-01', '2018-01-04'],
        ['石家庄碧桂园项目落地', '3', '2018-01-01', '2018-01-04'],
        ['苏州碧桂园区域集采方案确定', '44', '2018-01-21', '2018-03-06'],
        ['东莞、重庆、贵阳区域碧桂园落地', '22', '2018-03-07', '2018-03-29'],
        ['武汉区域碧桂园集采准备中', '18', '2018-03-30', '2018-04-17'],
        ['滁州碧桂园（欧洲城）配电房，公关市政部，达成采购', '29', '2018-03-01', '2018-03-30'],
        ['苏州区域分公司来司考察', '2', '2018-04-18', '2018-04-20'],
        ['公关碧桂园东莞公司', '303', '2018-01-01', '2018-10-31'],
        ['公关碧桂园惠深公司', '364', '2018-01-01', '2018-12-31'],
        ['公关鲁亿通电气实现碧桂园部分项目产品更改品牌', '303', '2018-01-01', '2018-10-31'],
        ['鲁亿通电气与我司商务、经销商商务对接及交流会', '244', '2018-03-01', '2018-10-31'],
        ['鲁亿通电气技术交流会', '60', '2018-03-01', '2018-04-30'],
        ['公关淀山湖碧桂园芳华里项目', '305', '2018-03-01', '2018-12-31'],
        ['公关太仓碧桂园漫悦兰亭项目', '305', '2018-03-01', '2018-12-31'],
        ['公关碧桂园长兴龙山项目', '214', '2018-03-01', '2018-10-01'],
        ['公关常熟碧桂园春江名筑项目', '245', '2018-03-01', '2018-11-01'],
        ['公关常熟碧桂园南部新城项目', '274', '2018-04-01', '2018-12-31'],
        ['组织鲁亿通电气与我司合作大型成套厂技术交流', '29', '2018-04-01', '2018-04-30'],
        ['公关如皋如城碧桂园项目（颐和樾园）', '93', '2018-04-08', '2018-07-10'],
        ['公关如皋龙游湖项目', '89', '2018-04-11', '2018-07-09'],
        ['公关如东掘港项目东洲壹号院', '92', '2018-04-19', '2018-07-20'],
        ['公关莱山碧桂园，实现一期收购项目品牌选用', '183', '2018-05-01', '2018-10-31'],
        ['成都碧桂园落地跟进', '20', '2018-05-22', '2018-06-11'],
        ['合肥区域碧桂园落地', '27', '2018-05-22', '2018-06-18'],
        ['昆明采购进度更新', '20', '2018-05-22', '2018-06-11'],
        ['武汉区域集采推进', '62', '2018-05-22', '2018-07-23'],
        ['苏州碧桂园集采落地', '8', '2018-05-22', '2018-05-30'],
        ['公关马鞍山当涂碧桂园，跟进H3流程通过', '175', '2018-05-28', '2018-11-19'],
        ['公关常熟碧桂园东辰名筑项目', '245', '2018-05-31', '2019-01-31'],
        ['浙江区域碧桂园项目公关及采购落地', '213', '2018-06-01', '2018-12-31'],
        ['昆明碧桂园落地', '213', '2018-06-01', '2018-12-31'],
        ['南京碧桂园项目新签及落地', '213', '2018-06-01', '2018-12-31'],
        ['重庆碧桂园项目落地', '213', '2018-06-01', '2018-12-31'],
        ['合肥碧桂园年度落地', '213', '2018-06-01', '2018-12-31'],
        ['公关阜阳界首碧桂园，配电箱（户内 非标）变更', '28', '2018-06-01', '2018-06-29'],
        ['公关招远碧桂园，实现展示区品牌提交选用', '61', '2018-06-01', '2018-08-01'],
        ['碧桂园东莞区域推广会', '51', '2018-06-10', '2018-07-31'],
        ['成都碧桂园分公司关系梳理', '30', '2018-07-01', '2018-07-31'],
        ['郑州碧桂园节点反馈', '30', '2018-07-01', '2018-07-31'],
        ['成都碧桂园H3首例落地', '10', '2018-07-01', '2018-07-11'],
        ['滁州碧桂园（滁州碧桂园观澜悦府小区）配电房项目', '44', '2018-07-03', '2018-08-16'],
        ['华东区域碧桂园分公司走访', '40', '2018-07-06', '2018-08-15'],
        ['上海两家碧桂园分公司拜访', '40', '2018-07-06', '2018-08-15'],
        ['石家庄办碧桂园邢台、辛集项目落地', '101', '2018-07-06', '2018-10-15'],
        ['公关碧桂园河源、梅州公司', '106', '2018-08-15', '2018-11-29'],
        ['组织鲁亿通电气各部门进行节日联谊', '27', '2018-09-01', '2018-09-28'],
        ['碧桂园惠深区域技术交流会', '11', '2018-10-15', '2018-10-26'],
        ['项目组任务完成情况梳理', '13', '2018-11-16', '2018-11-29'],
        ['黔江碧桂园电房开发', '9', '2019-01-01', '2019-01-10'],
        ['开发巫溪、云阳、涪陵碧桂园电房', '70', '2019-01-01', '2019-03-12'],
        ['开发永川碧桂园电房', '36', '2019-01-01', '2019-02-06'],
        ['开关碧桂园合作项目', '30', '2019-01-01', '2019-01-31']
    ]
    for t in tasks:
        name, duration, start_date, end_date = t[0], t[1], t[2], t[3]
        resource, pct_complete, dependencies = '', '', ''
        task = Task(name=name,
                    resource=resource,
                    start_date=start_date,
                    end_date=end_date,
                    duration=duration,
                    pct_complete=pct_complete,
                    dependencies=dependencies)
        db.session.add(task)
    db.session.commit()

    task_name = []
    for t in tasks:
        task_name.append(t[0])
    task_dict = {}
    for t in task_name:
        t_obj = Task.query.filter_by(name=t).first()
        task_dict[t] = t_obj
    pjt_dict['IB01项目'].tasks = list(task_dict.values())
    db.session.commit()

    click.echo('Done.')

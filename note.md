# salalchemy
## relationship
### 一对多
假设有两个表, 人员和项目, 1个人员对应多个项目, 那么model如下:
```python
class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    projects = db.relationship('Project', backref='person', lazy=True)

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    person_id = db.Column(db.Integer, db.ForeignKey('person.id'))
```
人员是主表, 需要添加一个关系projects, 与该人所负责的项目关联, 具体来看是声明从表的名称, 但是这一列在主表不显示, 只是一个关系.
项目是从表, 需要添加一列person_id, 表示关联的主键, 也就是主表的主键.
主表中的backref表示, 在从表引用时所使用的名称, 这个名称代表主表的一行记录, 也就是1个对象, 这个对象中包含了主表的这一行记录的所有信息, 包括id, name等等.

主表的lazy表示何时载入数据, 默认是True, 表示需要时用标准select语句在一个批处理go中载入.

### 多对多
```python
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
```
多对多需要声明一个关系表, 将主表和从表各自的主键关联起来. 关系属性只需要在其中一个表定义就行, 形式和一对多差不多.

具体使用时, 关系属性可以通过表.字段进行引用, 当记录实例化之后, 关系属性数据随之产生, 像引用常规列一样使用.

# jinja2
## context_processor
注册环境变量, 然后每个html模板都可以直接使用

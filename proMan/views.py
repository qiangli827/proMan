from proMan import app, db
from proMan.models import Task
from proMan.models import Task
from flask import Flask, render_template, url_for, request, flash, redirect

# 首页
@app.route('/')
def index():
    return render_template('index.html')

# 任务
@app.route('/tasks', methods=['GET', 'POST'])
def tasks():
    # 添加任务
    if request.method == 'POST':
        task_name = request.form.get('task')
        project_name = request.form.get('project')
        task = Task(task=task_name, project=project_name)
        db.session.add(task)
        db.session.commit()
        flash('添加任务成功')
        return redirect(url_for('tasks'))
    # 展示任务清单
    tasks = Task.query.all()
    return render_template('tasks.html', tasks=tasks)

# 编辑任务
@app.route('/task/edit/<int:task_id>', methods=['GET', 'POST'])
def edit(task_id):
    task = Task.query.get_or_404(task_id)
    # 编辑任务
    if request.method == 'POST':
        task_name = request.form['task']
        project_name = request.form['project']
        task.task = task_name
        task.project = project_name
        db.session.commit()
        flash('任务编辑成功')
        return redirect(url_for('tasks'))
    return render_template('edit.html', task=task)

# 删除任务
@app.route('/task/delete/<int:task_id>', methods=['POST'])
def delete(task_id):
    task = Task.query.get_or_404(task_id)
    # 删除任务
    db.session.delete(task)
    db.session.commit()
    flash('任务删除成功')
    return redirect(url_for('tasks'))

# 关于
@app.route('/about')
def about():
    return render_template('about.html')

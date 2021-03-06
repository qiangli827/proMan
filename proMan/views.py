import os
from proMan import app, db, allowed_file
from proMan.models import Task, Project
from flask import Flask, render_template, url_for, request, flash, redirect, send_from_directory
from werkzeug import secure_filename

# 上传文件
@app.route('/project/<int:project_id>/files/uploads', methods=['GET', 'POST'])
def upload_file(project_id):
    project = Project.query.get_or_404(project_id)
    tasks = project.tasks
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            if str(project_id) not in os.listdir(app.config['UPLOAD_FOLDER']):
                os.mkdir(str(project_id))
            save_file = os.path.join(app.config['UPLOAD_FOLDER'], str(project_id)) + '\\' + filename
            file.save(save_file)
            return redirect(url_for('uploaded_file', project_id=project_id, filename=filename))
    return render_template('files.html', project=project, tasks=tasks)

# 上传后展示文件
@app.route('/project/<int:project_id>/files/<filename>')
def uploaded_file(project_id, filename):
    return send_from_directory(app.config['UPLOAD_FOLDER']+'\\'+str(project_id), filename)

# 首页
@app.route('/')
def index():
    return render_template('index.html')

# 项目
@app.route('/project/<int:project_id>')
def project(project_id):
    project = Project.query.get_or_404(project_id)
    tasks = project.tasks
    return render_template('project.html', project=project, tasks=tasks)

# 任务
@app.route('/project/<int:project_id>/tasks')
def tasks(project_id):
    project = Project.query.get_or_404(project_id)
    tasks = project.tasks
    return render_template('tasks.html', project=project, tasks=tasks)

# 进展
@app.route('/project/<int:project_id>/progress')
def progress(project_id):
    project = Project.query.get_or_404(project_id)
    tasks = project.tasks
    return render_template('progress.html', project=project, tasks=tasks)
# 人员
@app.route('/project/<int:project_id>/persons')
def persons(project_id):
    project = Project.query.get_or_404(project_id)
    tasks = project.tasks
    return render_template('persons.html', project=project, tasks=tasks)
# 文件
@app.route('/project/<int:project_id>/files')
def files(project_id):
    project = Project.query.get_or_404(project_id)
    tasks = project.tasks
    return render_template('files.html', project=project, tasks=tasks)
# 费用
@app.route('/project/<int:project_id>/expense')
def expense(project_id):
    project = Project.query.get_or_404(project_id)
    tasks = project.tasks
    return render_template('expense.html', project=project, tasks=tasks)


# 添加任务
@app.route('/project/<int:project_id>/task/add', methods=['GET', 'POST'])
def tasks_add(project_id):
    project = Project.query.get_or_404(project_id)
    if request.method == 'POST':
        task_name = request.form.get('task_name')
        project_name = request.form.get('project_name')
        resource = request.form.get('resource')
        start_date = request.form.get('start_date')
        end_date = request.form.get('end_date')
        duration = request.form.get('duration')
        pct_complete = request.form.get('pct_complete')
        dependencies = request.form.get('dependencies')

        project = Project.query.filter_by(name=project_name).first()
        task = Task(name=task_name,
                    resource=resource,
                    start_date=start_date,
                    end_date=end_date,
                    duration=duration,
                    pct_complete=pct_complete,
                    dependencies=dependencies,
                    project=project)
        db.session.add(task)
        db.session.commit()
        flash('添加任务成功')
        return redirect(url_for('tasks', project_id=project.id))
    return render_template('add.html', project=project)
# 编辑任务
@app.route('/project/<int:project_id>/task/<int:task_id>/edit', methods=['GET', 'POST'])
def edit(project_id, task_id):
    project = Project.query.get_or_404(project_id)
    task = Task.query.get_or_404(task_id)
    # 编辑任务
    if request.method == 'POST':
        task_name = request.form.get('task_name')
        project_name = request.form.get('project_name')
        resource = request.form.get('resource')
        start_date = request.form.get('start_date')
        end_date = request.form.get('end_date')
        duration = request.form.get('duration')
        pct_complete = request.form.get('pct_complete')
        dependencies = request.form.get('dependencies')

        project = Project.query.filter_by(name=project_name).first()
        task.name = task_name
        task.resource = resource
        task.start_date = start_date
        task.end_date = end_date
        task.duration = duration
        task.pct_complete = pct_complete
        task.dependencies = dependencies
        task.project = project
        db.session.commit()
        flash('任务编辑成功')
        return redirect(url_for('tasks', project_id=project.id))
    return render_template('edit.html', task=task, project=project)

# 删除任务
@app.route('/project/<int:project_id>/task/<int:task_id>/delete', methods=['POST'])
def delete(project_id, task_id):
    project = Project.query.get_or_404(project_id)
    task = Task.query.get_or_404(task_id)
    # 删除任务
    db.session.delete(task)
    db.session.commit()
    flash('任务删除成功')
    return redirect(url_for('tasks', project_id=project.id))

# 测试

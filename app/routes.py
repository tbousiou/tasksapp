
from app import app, db
from app.models import Task, Project
from flask import render_template, request, redirect, url_for
from datetime import datetime
from sqlalchemy import desc


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/mytasks', methods=['GET', 'POST'])
def mytasks():
    current_user = 'Θεόδωρος Μ.'
    all_projects = db.session.execute(db.select(Project)).scalars()
    if request.method == 'POST':
        project_id = request.form['project']
        description = request.form['description']
        hours = request.form['hours']
        date_string = request.form['date']
        date = datetime.strptime(date_string, "%Y-%m-%d")
        _, week, _= date.isocalendar()
        task = Task(user=current_user,project_id=project_id,description=description,hours=hours,date=date,week=week)
        db.session.add(task)
        db.session.commit()
        return redirect(url_for('mytasks'))
    my_tasks = db.session.execute(db.select(Task).filter_by(user=current_user).order_by(desc(Task.week))).scalars()
    return render_template('mytasks.html', tasks=my_tasks, projects=all_projects)

@app.route('/task/delete/<int:id>')
def task_delete(id):
    task_to_delete = Task.query.get_or_404(id)
    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect(url_for('mytasks'))
    except:
        return 'There was an error while deleting that task'


@app.route('/alltasks')
def alltasks():
    all_tasks = db.session.execute(db.select(Task)).scalars()
    
    return render_template('alltasks.html', tasks=all_tasks)


@app.route('/projects', methods=['GET', 'POST'])
def projects():
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        project = Project(name=name,description=description)
        db.session.add(project)
        db.session.commit()
        return redirect(url_for('projects'))

    all_projects = db.session.execute(db.select(Project)).scalars()
    return render_template('projects.html', projects=all_projects)


@app.route('/project/delete/<int:id>')
def project_delete(id):
    project_to_delete = Project.query.get_or_404(id)
    try:
        db.session.delete(project_to_delete)
        db.session.commit()
        return redirect(url_for('projects'))
    except:
        return 'There was an error while deleting that project'
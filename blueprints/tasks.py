from flask import Blueprint, render_template, redirect, url_for, request
from flask_login import login_required, current_user
from sqlalchemy import cast, Date
from forms import TaskForm
from models import Task
from database import db

tasks = Blueprint('tasks', __name__)

@tasks.route('/', methods=['GET', 'POST'])
@login_required
def tasks_dashboard():
    form = TaskForm()
    if form.validate_on_submit():
        new_task = Task(title=form.title.data, description=form.description.data, deadline=form.deadline.data, user_id=current_user.id)
        db.session.add(new_task)
        db.session.commit()
    tasks_list = Task.query.filter_by(user_id=current_user.id).all()
    if current_user.role == 'admin' or current_user.role == 'superadmin':
        tasks_list = Task.query.all()
    return render_template('tasks.html', form=form, tasks=tasks_list, role=current_user.role)

@tasks.route('/task/<int:id>/edit', methods=['GET', 'POST'])
@login_required
def edit_task(id):
    task = Task.query.get(id)
    form = TaskForm()
    if form.validate_on_submit():
        task.title = form.title.data
        task.description = form.description.data
        task.deadline = form.deadline.data
        db.session.commit()
        return redirect(url_for('tasks.tasks_dashboard'))
    elif request.method == 'GET':
        form.title.data = task.title
        form.description.data = task.description
        form.deadline.data = task.deadline
    return render_template('edit_task.html', form=form)

@tasks.route('/task/<int:id>/delete')
@login_required
def delete_task(id):
    task = Task.query.get(id)
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for('tasks.tasks_dashboard'))
from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required
from database import db
from models import User
from decorators import role_required

users = Blueprint('users', __name__)

@users.route('/users')
@login_required
@role_required('superadmin')
def users_dashboard():
    users_list = User.query.filter(User.role != 'superadmin').all()
    return render_template('users.html', users=users_list)

@users.route('/user/<int:id>/promote')
@login_required
@role_required('superadmin')
def promote_user(id):
    user = User.query.get(id)
    user.role = 'admin'
    db.session.commit()
    return redirect(url_for('users.users_dashboard'))

@users.route('/user/<int:id>/demote')
@login_required
@role_required('superadmin')
def demote_user(id):
    user = User.query.get(id)
    user.role = 'user'
    db.session.commit()
    return redirect(url_for('users.users_dashboard'))

@users.route('/user/<int:id>/delete')
@login_required
@role_required('superadmin')
def delete_user(id):
    user = User.query.get(id)
    db.session.delete(user)
    db.session.commit()
    return redirect(url_for('users.users_dashboard'))
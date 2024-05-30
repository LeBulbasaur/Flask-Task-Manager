from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_user, login_required, logout_user, LoginManager
from werkzeug.security import check_password_hash, generate_password_hash
from forms import LoginForm, RegisterForm
from models import User
from database import db

auth = Blueprint('auth', __name__)

login_manager = LoginManager()

@login_manager.user_loader
def load_user(user_id):
    return db.session.get(User, int(user_id))

@auth.route('/register', methods=['GET', 'POST'])
def register_site():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.verify_password.data:
            flash('Passwords do not match')
            return redirect(url_for('auth.register_site'))
        if User.query.filter_by(username=form.username.data).first():
            flash('Username is already taken')
            return redirect(url_for('auth.register_site'))
        hashed_password = generate_password_hash(form.password.data, method='pbkdf2')
        new_user = User(username=form.username.data, password=hashed_password, role='user')
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('auth.login_site'))
    return render_template('register.html', form=form)

@auth.route('/login', methods=['GET', 'POST'])
def login_site():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and check_password_hash(user.password, form.password.data):
            if form.remember.data:
                login_user(user, remember=form.remember.data)
            else:
                login_user(user)
            return redirect(url_for('tasks.tasks_dashboard'))
        flash('Invalid username or password')
    return render_template('login.html', form=form)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login_site'))
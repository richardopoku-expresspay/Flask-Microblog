from app import app
from flask import render_template, flash, redirect, url_for
from app.forms import LoginForm
from app.models import User
from flask_login import current_user, login_user, logout_user

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Dev Man'}
    return render_template('index.html', user=user)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.find_by_username(form.username.data)

        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))

        login_user(user, remember=form.remember_me.data)

        return redirect(url_for('index'))
    return render_template('login.html', form=form)

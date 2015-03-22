# -*- coding: utf-8 -*-
from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for

from app import db, bcrypt

from app.users.forms import LoginForm
from app.users.models import User
from flask.ext.login import login_required, login_user, logout_user


mod = Blueprint('users', __name__, url_prefix='/users')


@mod.route('/')
@mod.route('/index')
def index():
    user = {'nickname': 'Michael'}
    posts = [
        {
            'author': {'nickname': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'nickname': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('users/home.html', title='Users', user=user, posts=posts)


@mod.route('/<int:user_id>')
@login_required
def show_user(user_id):
    user = User.query.get(user_id)
    return render_template('users/user.html', title=user.nickname,  user=user)


@mod.route('/login', methods=['GET', 'POST'])
def login():
    error = None

    form = LoginForm()  # request.form inside?
    if request.method == 'POST':
        if form.validate_on_submit():
            user = User.query.filter_by(nickname=request.form['username']).first()

            if user is not None and bcrypt.check_password_hash(user.password, request.form['password']):
                login_user(user, remember=False)
                return redirect(url_for('.show_user', user_id=2))
            else:
                error = 'Invalid credentials. Please try again'

    return render_template('users/login.html', title="Login", form=form, error=error)


@mod.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You were logged out')
    return redirect(url_for('adverts.index'))

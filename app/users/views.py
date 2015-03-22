# -*- coding: utf-8 -*-
from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for

from app import db, bcrypt

from app.users.forms import LoginForm, RegisterForm
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
    title = 'No such user' if user is None else user.nickname
    return render_template('users/user.html', title=title,  user=user)


@mod.route('/register/', methods=['GET', 'POST'])   # pragma: no cover
def register():
    error = None
    form = RegisterForm(request.form)

    if form.validate_on_submit():
        user = User(form.username.data, form.email.data, form.password.data, form.email.data)
        db.session.add(user)
        db.session.commit()
        login_user(user)
        return redirect(url_for('home.home'))

    return render_template('register.html', form=form, error=error)


@mod.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    form = LoginForm(request.form)

    if request.method == 'POST':
        if form.validate_on_submit():
            from pprint import pprint as p
            p(form)
            user = User.query.filter_by(nickname=form.username.data).first()

            if user is not None and bcrypt.check_password_hash(user.password, form.password.data):
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

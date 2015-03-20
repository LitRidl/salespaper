# -*- coding: utf-8 -*-
from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for

from app import db, bcrypt
from forms import LoginForm

from app.users.forms import LoginForm
from app.users.models import User


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
def show_user(user_id):
    user = User.query.get(user_id)
    return render_template('users/user.html', title=user.nickname,  user=user)


@mod.route('/login', methods=['GET', 'POST'])
def login():
    error = None

    form = LoginForm()  # request.form inside?
    if request.method == 'POST':
        if form.validate_on_submit():
            if request.form['username'] == 'admin' and request.form['password'] == 'admin':
                session['logged_in'] = True
                flash('You were logged in')
                return redirect(url_for('users/index'))
            else:
                error = 'Invalid credentials. Please try again'
        else:
            error = 'Please provide more data'

    return render_template('users/login.html', title="Login", form=form, error=error)

# -*- coding: utf-8 -*-
from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for
from werkzeug import check_password_hash, generate_password_hash

from app import db

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
    return render_template('index.html', title='Home', user=user, posts=posts)


@mod.route('/<int:user_id>')
def show_user(user_id):
    user = User.query.get(user_id)
    return render_template('users/user.html', user=user)



@mod.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template('login.html', title='Sign In', form=form)

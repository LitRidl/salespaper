# -*- coding: utf-8 -*-
from datetime import datetime

from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for

from app import db, bcrypt, login_manager

from app.users.forms import LoginForm, RegisterForm
from app.users.models import User
from flask.ext.login import login_required, login_user, logout_user, current_user
from sqlalchemy import exists


mod = Blueprint('users', __name__, url_prefix='/users')


@mod.route('/')
@mod.route('/index')
@login_required
def index():
    user = current_user
    return render_template('users/home.html', title=user.nickname,  user=user, adverts=user.adverts)


@mod.route('/home')
@login_required
def home():
    user = current_user
    return render_template('users/home.html', title=user.nickname,  user=user, adverts=user.adverts)


@mod.route('/<int:user_id>')
@login_required
def show_user(user_id):
    user = User.query.get(user_id)
    title = u'No such user' if user is None else user.nickname

    if current_user.id != user.id and not current_user.is_admin():
        return login_manager.unauthorized()

    return render_template('users/user.html', title=title,  user=user)


@mod.route('/<int:advert_id>/block')
@login_required
def block_user(user_id):
    if not current_user.is_admin():
        return render_template('errors/404.html'), 404
    else:
        user = User.query.get(user_id)
        if user:
            user.active = False
            db.session.add(user)
            db.session.commit()
        return redirect(url_for('users.show_user', user_id=user.id))


@mod.route('/register/', methods=['GET', 'POST'])   # pragma: no cover
def register():
    errors = []
    form = RegisterForm(request.form)

    if form.validate_on_submit():
        login_taken = db.session.query(exists().where(User.nickname == form.nickname.data)).scalar()
        email_taken = db.session.query(exists().where(User.email == form.email.data)).scalar()

        if login_taken or email_taken:
            if login_taken:
                errors.append(u'Nickname already taken. Please try another one')
            if email_taken:
                errors.append(u'E-mail already registered. Please try another one')
        else:
            user = User(form.nickname.data, form.password.data, form.email.data)
            db.session.add(user)
            db.session.commit()
            login_user(user)
            return redirect(url_for('users.home'))

    return render_template('users/register.html', form=form, errors=errors)


@mod.route('/login', methods=['GET', 'POST'])
def login():
    errors = []
    form = LoginForm(request.form)

    if request.method == 'POST':
        if form.validate_on_submit():
            user = User.query.filter_by(nickname=form.username.data).first()

            if user is not None and bcrypt.check_password_hash(user.password, form.password.data):
                login_user(user, remember=form.remember_me.data)
                return redirect(request.args.get('next') or url_for('.show_user', user_id=user.id))
            else:
                errors.append(u'Invalid credentials. Please try again')

    return render_template('users/login.html', title=u"Login", form=form, errors=errors)


@mod.route('/logout')
@login_required
def logout():
    logout_user()
    flash(u'You were logged out')
    return redirect(url_for('adverts.index'))

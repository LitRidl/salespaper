# -*- coding: utf-8 -*-
from datetime import datetime
from flask.ext.babel import Babel

import os
import wtforms_json

from flask import Flask, render_template
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager, AnonymousUserMixin, current_user
from flask.ext.bcrypt import Bcrypt

from config import _basedir

app = Flask(__name__, static_folder='../static', template_folder='../templates')
bcrypt = Bcrypt(app)

DEFAULT_CONFIG_CLASS = os.getenv('CONF', 'DevelopmentConfig')
app.config.from_object('config.' + DEFAULT_CONFIG_CLASS)

# Patch WTForms to accept JSON
wtforms_json.init()

# Create ORM session
db = SQLAlchemy(app)


class UserAnonymous(AnonymousUserMixin):
    id = None
    locale = app.config['BABEL_DEFAULT_LOCALE']
    timezone = app.config['BABEL_DEFAULT_TIMEZONE']

# Login Manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.anonymous_user = UserAnonymous
login_manager.session_protection = 'strong'
login_manager.login_view = 'users.login'


@login_manager.user_loader
def load_user(user_id):
    from app.users.models import User
    return User.query.get(int(user_id))


# @login_manager.unauthorized_handler
# def unauthorized():
#     # do stuff
#     return a_response

# i18n and l18n
babel = Babel(app)


@babel.localeselector
def get_locale():
    return current_user.locale
    # return request.accept_languages.best_match(['de', 'fr', 'en'])


@babel.timezoneselector
def get_timezone():
    return current_user.timezone


# App common handlers
@app.errorhandler(404)
def page_not_found(error):
    return render_template('errors/404.html'), 404


# @app.errorhandler(500)
# def internal_error(error):
#     db.session.rollback()
#     return render_template('errors/500.html'), 500


# Pre/post-request actions
@app.before_request
def before_request():
    app.jinja_env.globals['user'] = current_user


@app.after_request
def after_request(response):
    if not current_user.is_anonymous():
        current_user.last_req_date = datetime.utcnow()
        db.session.add(current_user)
        db.session.commit()
    return response


######################
# Initialize modules #
######################

# Jinja2 filters
from filters import mod as JinjaFilters
app.register_blueprint(JinjaFilters)

# Users
from app.users.views import mod as Users
app.register_blueprint(Users)

# Adverts
from app.adverts.views import mod as Adverts
app.register_blueprint(Adverts)

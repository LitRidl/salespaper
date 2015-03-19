# -*- coding: utf-8 -*-

import os
import wtforms_json

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__, static_folder='../static', template_folder='../templates')

DEFAULT_CONFIG_CLASS = os.getenv('CONF', 'DevelopmentConfig')
app.config.from_object('config.' + DEFAULT_CONFIG_CLASS)

# Patch WTForms to accept JSON
wtforms_json.init()

# Create ORM session
db = SQLAlchemy(app)

######################
# Initialize modules #
######################

# Users
from app.users.views import mod as Users
app.register_blueprint(Users)

# Adverts
from app.adverts.views import mod as Adverts
app.register_blueprint(Adverts)

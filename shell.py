#!env/bin/python
# -*- coding: utf-8 -*-

import os
import sys
import random
import datetime
import readline

from pprint import pprint as p

from flask import *
from sqlalchemy.exc import SQLAlchemyError

from app import *

from app.users.models import *
from app.adverts.models import *

# Example: db_create_user('ipetrov', '123456', 'ipetrov98@gmail.com', 'admin')
def create_user(username, password, email, role):
    '''Adds User(username, password, email, role) to database'''
    user = User(username, password, email, role=role)
    user.active = True
    try:
        db.session.add(user)
        db.session.commit()
    except SQLAlchemyError as e:
        print(e)
        db.session.rollback()

try:
    import IPython
    IPython.embed()
except ImportError:
    os.environ['PYTHONINSPECT'] = 'True'

ctx = app.test_request_context()
ctx.push()
app.preprocess_request()

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


def db_create_admin():
    admin = User('LitRidl', '123456', 'litridl@gmail.com', role='admin')
    admin.active = True
    try:
        db.session.add(admin)
        db.session.commit()
    except SQLAlchemyError as e:
        print(e)
        db.session.rollback()


os.environ['PYTHONINSPECT'] = 'True'

ctx = app.test_request_context()
ctx.push()
app.preprocess_request()

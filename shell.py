#!env/bin/python
# -*- coding: utf-8 -*-

import os
import sys
import random
import datetime
import readline

from pprint import pprint as p

from flask import *
from app import *

from app.users.models import *
from app.adverts.models import *

os.environ['PYTHONINSPECT'] = 'True'

ctx = app.test_request_context()
ctx.push()
app.preprocess_request()

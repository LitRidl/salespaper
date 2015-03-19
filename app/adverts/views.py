# -*- coding: utf-8 -*-
from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for
from werkzeug import check_password_hash, generate_password_hash

from app import db

from app.adverts.forms import LoginForm
from app.adverts.models import Advert


mod = Blueprint('adverts', __name__, url_prefix='/adverts')


@mod.route('/')
@mod.route('/index')
def index():
    adverts = Advert.query.all()
    return render_template('adverts/index.html', title='Adverts', adverts=adverts)

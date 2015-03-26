# -*- coding: utf-8 -*-
from flask import Blueprint, request, render_template, redirect, url_for
from flask.ext.login import login_required

from app import db

from app.adverts.forms import AdvertForm
from app.adverts.models import Advert


mod = Blueprint('adverts', __name__, url_prefix='/adverts')


@mod.route('/')
@mod.route('/index')
def index():
    adverts = Advert.query.all()
    return render_template('adverts/index.html', title='Adverts', adverts=adverts)


@mod.route('/<int:advert_id>')
def show_advert(advert_id):
    advert = Advert.query.get(advert_id)
    return render_template('adverts/advert_info.html', advert=advert)


@mod.route('/<int:advert_id>/edit')
@login_required
def advert_edit(advert_id):
    advert = Advert.query.get(advert_id)
    form = AdvertForm(advert)  # WORKS???
    return render_template('adverts/advert_edit.html', advert=advert, form=form)


@mod.route('/new', methods=['GET', 'POST'])
@login_required
def advert_create():
    errors = []
    form = AdvertForm(request.form)

    if form.validate_on_submit():
        advert = Advert(
            title='',
            comment=''
        )
        db.session.add(advert)
        db.session.commit()
        return redirect(url_for('users.edit_advert', advert_id=advert.id))  # IS ID ALREADY HERE???

    return render_template('adverts/advert_create.html', form=form, errors=errors)

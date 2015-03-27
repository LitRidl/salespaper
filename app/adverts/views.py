# -*- coding: utf-8 -*-
import datetime
from flask import Blueprint, request, render_template, redirect, url_for
from flask.ext.login import login_required, current_user

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


@mod.route('/<int:advert_id>/edit', methods=['GET', 'POST'])
@login_required
def advert_edit(advert_id):
    advert = Advert.query.get(advert_id)
    form = AdvertForm(obj=advert)
    return render_template('adverts/advert_edit.html', advert=advert, form=form)


@mod.route('/new', methods=['GET', 'POST'])
@login_required
def advert_create():
    errors = []
    form = AdvertForm(request.form)

    if form.validate_on_submit():
        advert = Advert(user_id=current_user.id, title=form.title.data, comment=form.comment.data,
                        phone=form.phone.data, place=form.place.data, closed=False)

        year = datetime.date(year=int(form.car_year.data), month=1, day=1)
        advert.set_car_data(used=form.car_used.data, cost=int(form.car_cost.data),
                            year=year, mileage=int(form.car_mileage.data),
                            transmission=form.car_transmission.data, engine_power=int(form.car_engine_power.data),
                            engine_volume=form.car_engine_volume.data, fuel=form.car_fuel_consumption.data,
                            drive=form.car_drive.data)

        db.session.add(advert)
        db.session.commit()

        return redirect(url_for('adverts.advert_edit', advert_id=advert.id))  # IS ID ALREADY HERE???

    return render_template('adverts/advert_create.html', form=form, errors=errors)

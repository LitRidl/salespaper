# -*- coding: utf-8 -*-
from flask import Blueprint, request, render_template, redirect, url_for
from flask.ext.login import login_required, current_user

from app import db, app

from app.adverts.forms import AdvertForm, SearchForm
from app.adverts.models import Advert
from sqlalchemy import and_


mod = Blueprint('adverts', __name__, url_prefix='/adverts')


@mod.route('/', methods=['GET', 'POST'])
@mod.route('/index', methods=['GET', 'POST'])
def index():
    form = SearchForm(request.form)
    q = Advert.query.filter(and_(Advert.closed == False, Advert.approved == True))

    if form.validate_on_submit():
        if form.car_used.data:
            q = q.filter(Advert.car_used.in_(form.car_used.data))

        if form.car_cost_min.data and form.car_cost_max.data:
            q = q.filter(Advert.car_cost.between(form.car_cost_min.data, form.car_cost_max.data))

        if form.car_mileage_min.data and form.car_mileage_max:
            q = q.filter(Advert.car_mileage.between(form.car_mileage_min.data, form.car_mileage_max.data))

        if form.car_transmission.data:
            q = q.filter(Advert.car_transmission.in_(form.car_transmission.data))

        if form.car_engine_power_min.data and form.car_engine_power_max:
            q = q.filter(Advert.car_cost.between(form.car_engine_power_min.data, form.car_engine_power_max.data))

        if form.car_engine_volume_min.data and form.car_engine_volume_max:
            q = q.filter(Advert.car_cost.between(form.car_engine_volume_min.data, form.car_engine_volume_max.data))

        if form.car_drive.data:
            q = q.filter(Advert.car_drive.in_(form.car_drive.data))

    adverts = q.all()

    return render_template('adverts/adverts_feed.html', title='Adverts', adverts=adverts, form=form)


@mod.route('/<int:advert_id>')
def show_advert(advert_id):
    advert = Advert.query.get(advert_id)
    return render_template('adverts/advert_info.html', advert=advert)


@mod.route('/<int:advert_id>/close')
@login_required
def close_advert(advert_id):
    advert = Advert.query.get(advert_id)
    if not advert or not (current_user.id == advert.user_id or current_user.is_admin()):
        return render_template('errors/404.html'), 404
    if advert:
        advert.closed = True
        db.session.add(advert)
        db.session.commit()
        return redirect(url_for('adverts.show_advert', advert_id=advert.id))


@mod.route('/<int:advert_id>/block')
@login_required
def block_advert(advert_id):
    if not current_user.is_admin():
        return render_template('errors/404.html'), 404
    else:
        advert = Advert.query.get(advert_id)
        if advert:
            advert.approved = False
            db.session.add(advert)
            db.session.commit()
        return redirect(url_for('adverts.show_advert', advert_id=advert.id))


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

        advert.set_car_data(used=form.car_used.data, cost=int(form.car_cost.data), mileage=int(form.car_mileage.data),
                            transmission=form.car_transmission.data, engine_power=int(form.car_engine_power.data),
                            engine_volume=form.car_engine_volume.data, fuel=form.car_fuel_consumption.data,
                            drive=form.car_drive.data)

        db.session.add(advert)
        db.session.commit()

        return redirect(url_for('adverts.show_advert', advert_id=advert.id))

    return render_template('adverts/advert_create.html', form=form, errors=errors)

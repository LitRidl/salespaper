from datetime import datetime
from app.adverts.constants import TRANSMISSION_CHOICES, USED_CHOICES, DRIVE_CHOICES
from flask.ext.wtf import Form
from wtforms import TextField, BooleanField, SelectField, IntegerField, SelectMultipleField
from wtforms.validators import Required, Length, Optional, NumberRange
from wtforms.widgets import TextArea


class AdvertForm(Form):
    title = TextField('title', validators=[Required(), Length(min=10, max=240)])
    comment = TextField('comment', widget=TextArea(), validators=[Optional(), Length(min=10, max=5000)])

    phone = TextField('phone', validators=[Required(), Length(min=12, max=20)])
    place = TextField('place', validators=[Optional(), Length(min=10, max=500)])

    closed = BooleanField('closed')

    car_used = SelectField('car_used', choices=USED_CHOICES)
    car_cost = IntegerField('car_mileage', validators=[Required(), NumberRange(1, 20000000)])

    car_mileage = IntegerField('car_mileage', validators=[Optional()])
    car_transmission = SelectField('car_transmission', choices=TRANSMISSION_CHOICES)
    car_engine_power = IntegerField('car_fuel_consumption',
                                    validators=[Optional(), NumberRange(min=30, max=700)])
    car_engine_volume = IntegerField('car_fuel_consumption',
                                     validators=[Optional(), NumberRange(min=600, max=8200)])
    car_fuel_consumption = IntegerField('car_fuel_consumption',
                                        validators=[Optional(), NumberRange(min=4, max=22)])
    car_drive = SelectField('car_drive', choices=DRIVE_CHOICES)


class SearchForm(Form):
    car_used = SelectMultipleField(choices=USED_CHOICES, validators=[Optional()])

    car_cost_min = IntegerField(validators=[Optional(), NumberRange(1, 20000000)])
    car_cost_max = IntegerField(validators=[Optional(), NumberRange(1, 20000000)])

    car_mileage_min = IntegerField(validators=[Optional()])
    car_mileage_max = IntegerField(validators=[Optional()])

    car_transmission = SelectMultipleField(choices=TRANSMISSION_CHOICES, validators=[Optional()])

    car_engine_power_min = IntegerField(validators=[Optional(), NumberRange(min=0, max=100000)])
    car_engine_power_max = IntegerField(validators=[Optional(), NumberRange(min=0, max=100000)])

    car_engine_volume_min = IntegerField(validators=[Optional(), NumberRange(min=0, max=100000)])
    car_engine_volume_max = IntegerField(validators=[Optional(), NumberRange(min=0, max=100000)])

    car_fuel_consumption_min = IntegerField(validators=[Optional(), NumberRange(min=0, max=100000)])
    car_fuel_consumption_max = IntegerField(validators=[Optional(), NumberRange(min=0, max=100000)])

    car_drive = SelectMultipleField(choices=DRIVE_CHOICES, validators=[Optional()])

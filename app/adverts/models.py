# -*- coding: utf-8 -*-
from datetime import datetime

from app import db
import constants
from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey, Date, Enum
from sqlalchemy.orm import relationship


class Advert(db.Model):
    __tablename__ = 'advert'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)

    title = Column(String(250), nullable=False)
    comment = Column(String(5000), default='', nullable=False)

    phone = Column(String(20), nullable=True)
    place = Column(String(500), nullable=True)

    timestamp = Column(DateTime, default=datetime.utcnow(), nullable=False, index=True)
    approved = Column(Boolean, default=True, nullable=False)
    closed = Column(Boolean, default=False, nullable=False)

    user_id = Column(Integer, ForeignKey('user.id'), nullable=False, index=True)
    user = relationship('User', back_populates='adverts')

    # Car properties (!: no need for indexing columns with few values)
    car_used = Column(Enum(*constants.USED), default='used')
    car_cost = Column(Integer, index=True)
    car_mileage = Column(Integer, index=True)
    car_transmission = Column(Enum(*constants.TRANSMISSION), default='automatic')
    car_engine_power = Column(Integer, index=True)
    car_engine_volume = Column(Integer, index=True)
    car_fuel_consumption = Column(Integer, index=True)
    car_drive = Column(Enum(*constants.DRIVE), default='front')

    def __init__(self, user_id, title, comment, phone=None, place=None, approved=True, closed=False):
        self.title = title
        self.comment = comment

        self.phone = phone
        self.place = None

        self.timestamp = datetime.utcnow()
        self.approved = approved
        self.closed = closed

        self.user_id = user_id

    def set_car_data(self, used=None, cost=None, mileage=None, transmission=None,
                     engine_power=None, engine_volume=None, fuel=None, drive=None):
        self.car_used = used
        self.car_cost = cost
        self.car_mileage = mileage
        self.car_transmission = transmission
        self.car_engine_power = engine_power
        self.car_engine_volume = engine_volume
        self.car_fuel_consumption = fuel
        self.car_drive = drive

    def __repr__(self):
        return '<Post %r>' % (self.title, )

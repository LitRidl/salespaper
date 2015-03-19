# -*- coding: utf-8 -*-

from app import db
import constants as ADVERT

class Advert(db.Model):
    __tablename__ = 'advert'

    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    user = db.relationship('User', back_populates='adverts')

    def __repr__(self):
        return '<Post %r>' % (self.body)

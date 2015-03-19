# -*- coding: utf-8 -*-

from app import db
import constants as USER

class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(64), unique=True)
    email = db.Column(db.String(120), unique=True)
    role = db.Column(db.SmallInteger, default=USER.USER)

    adverts = db.relationship('Advert', back_populates='user', lazy='select')

    def __repr__(self):
        return '<User %r>' % (self.nickname)

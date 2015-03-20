# -*- coding: utf-8 -*-

from app import db, bcrypt
import constants as USER


class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(64), unique=True)
    password = db.Column(db.String(60))
    email = db.Column(db.String(120), unique=True)
    role = db.Column(db.SmallInteger, default=USER.USER)

    adverts = db.relationship('Advert', back_populates='user', lazy='select')

    def __init__(self, nickname, password, email, role=USER.USER):
        self.nickname = nickname
        self.password = bcrypt.generate_password_hash(password)
        self.email = email
        self.role = role

    def __repr__(self):
        return '<User %r>' % (self.nickname)

# -*- coding: utf-8 -*-

from app import db
import constants as USER

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    role = db.Column(db.SmallInteger, default=USER.USER)

    def __repr__(self):
        return '<User %r>' % (self.nickname)

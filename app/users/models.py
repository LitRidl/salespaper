# -*- coding: utf-8 -*-
from datetime import datetime

from app import db, bcrypt, app
import constants as USER
from sqlalchemy import event


class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(64), unique=True, nullable=False, index=True)
    password = db.Column(db.String(60), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    role = db.Column(db.SmallInteger, default=USER.USER, nullable=False)

    active = db.Column(db.Boolean, default=True, nullable=False)

    last_req_date = db.Column(db.DateTime, default=datetime.utcnow)

    locale = db.Column(db.String(10), default=app.config['BABEL_DEFAULT_LOCALE'])
    timezone = db.Column(db.String(100), default=app.config['BABEL_DEFAULT_TIMEZONE'])

    adverts = db.relationship('Advert', back_populates='user', lazy='select')

    def __init__(self, nickname, password, email, role=USER.USER):
        self.nickname = nickname
        self.password = password
        self.email = email
        self.role = role

    def is_authenticated(self):
        return True

    def is_active(self):
        return self.active

    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self.id)

    def __repr__(self):
        return '<User %r>' % (self.nickname)


@event.listens_for(User.password, 'set', retval=True)
def password_change_listener(target, value, oldvalue, initiator):
    value = bcrypt.generate_password_hash(value) if value else value
    return value

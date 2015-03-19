# -*- coding: utf-8 -*-

import os

_basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    PORT = 5000
    HOST = '127.0.0.1'

    DEBUG = False
    TESTING = False

    CSRF_ENABLED = True
    CSRF_SESSION_KEY = "Ad125F930ez20C508dDq82l75c5E047r"

    SECRET_KEY = 'S2lsbGFHb3ZuYVNEeGN2QEFXRiQjdnM'

    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(_basedir, 'salespaper.db')
    SQLALCHEMY_MIGRATE_REPO = os.path.join(_basedir, 'db_repository')


class DevelopmentConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    pass

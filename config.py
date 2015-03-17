# -*- coding: utf-8 -*-


class Config(object):
    PORT = 5000
    HOST = 'localhost'

    DEBUG = False
    TESTING = False


class DevelopmentConfig(Config):
    DEBUG = True

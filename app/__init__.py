# -*- coding: utf-8 -*-

from Flask import Flask


app = Flask(__name__, static_folder='../static', template_folder='../templates')

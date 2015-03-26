# -*- coding: utf-8 -*-
from functools import wraps
from app.adverts.models import Advert
from flask import current_app
from flask.ext.login import current_user


def admin_required(func):
    @wraps(func)
    def decorated_view(*args, **kwargs):
        if not current_user or not current_user.is_admin():
            return current_app.login_manager.unauthorized()
        return func(*args, **kwargs)
    return decorated_view

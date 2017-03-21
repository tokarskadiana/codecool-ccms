from flask import Blueprint, session, flash, redirect, url_for
from functools import wraps


# login required decorator
def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('You need to login first')
            return redirect(url_for('authorization.login'))

    return wrap


# user perrmitions decorator
def required_roles(*roles):
    def wrapper(f):
        @wraps(f)
        def wrapped(*args, **kwargs):
            if session['type'] not in roles:
                flash("Permission denied")
                return redirect(url_for('index'))
            return f(*args, **kwargs)

        return wrapped

    return wrapper

from flask import Blueprint, render_template, session, url_for, redirect
from controller.user_session import user_session
from controller.decorators import login_required
from controller.decorators import login_required
import os

main_page = Blueprint('main_page', __name__,
                      template_folder='templates')


@main_page.route('/')
@login_required
def index():
    """
    handle main index page, display nav of current user
    :return:
    """
    return render_template('index.html', user=user_session(session['user'], session['type']))

from flask import Blueprint, session, render_template, redirect, url_for, flash, request, session
from model.manager import Manager
from model.mentor import Mentor
from model.student import Student
from model.employee import Employee
from controller.decorators import login_required, required_roles
# -----------------LOGIN------------------


authorization = Blueprint('authorization', __name__,
                          template_folder='templates')


@authorization.route("/login", methods=["GET", "POST"])
def login():
    """
    Login page
    GET: returns a login form
    POST: returns HTTP 200 on success and redirect to index page
          returns HTTP 200 when login/password not correct and back to login page
    """
    if request.method == "POST":
        username, password = request.form['username'], request.form['password']
        users = [Student, Mentor, Manager, Employee]
        user = None
        index = 0
        while not user and index < 4:
            user = users[index].get_to_login(username, password)
            index += 1
        if user:
            session['logged_in'] = True
            session['user'] = user.id
            session['type'] = user.__class__.__name__
            return redirect(url_for('main_page.index'))
        else:
            flash("Invalid Credentials. Please Try Again ")

    return render_template("login.html")


@authorization.route("/logout", methods=["GET", "POST"])
def logout():
    """
    Logout from user session
    GET: Returns HTTP 302 and redirect to login page.
    """
    session.pop('logged_in', None)
    session.pop('user', None)
    session.pop('type', None)
    flash('You are logged out, Have Fun')
    return redirect(url_for('authorization.login'))

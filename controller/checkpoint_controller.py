from flask import Blueprint, session, render_template, redirect, url_for, flash, request
from controller.decorators import login_required, required_roles
from controller.user_session import user_session
from model.checkpoint import Checkpoint
from model.mentor import Mentor
from model.student import Student

checkpoint_controller = Blueprint('checkpoint_controller', __name__,
                                  template_folder='templates')


# ---------------CHECKPOINT-----------------


@checkpoint_controller.route('/list-checkpoints')
@login_required
@required_roles('Mentor', 'Student')
def list_checkpoints():
    """
    List all checkpoints
    :return: template
    """

    user = user_session(session['user'], session['type'])
    choose = None
    if isinstance(user, Mentor):
        choose = "Mentor"
        list_checkpoints = Checkpoint.get_list_distinct()
        return render_template('viewcheckpoints.html', user=user_session(session['user'], session['type']),
                               choose=choose,
                               list_checkpoints=list_checkpoints)
    elif isinstance(user, Student):
        choose = "Student"
        list_checkpoints = Checkpoint.get_by_studedent_id(user.id)
        return render_template('viewcheckpoints.html', user=user_session(session['user'], session['type']),
                               choose=choose, list_checkpoints=list_checkpoints)
    else:
        return render_template('404.html', user=user_session(session['user'], session['type']))


@checkpoint_controller.route('/list-checkpoints/add-checkpoint', methods=['GET', 'POST'])
@login_required
@required_roles('Mentor')
def add_checkpoint():
    """
    GET: returns add assistant formula
    POST: returns list of assistant with new assistant added
    """
    user = user_session(session['user'], session['type'])
    if isinstance(user, Mentor):
        if request.method == 'POST':
            if request.form['add_checkpoint']:
                students = Student.list_students()
                checkpoint_name = request.form['checkpoint_name']
                date = request.form['date']
                Checkpoint.add_checkpoint_students(checkpoint_name, date,
                                                   user_session(session['user'], session[
                                                       'type']).id, students)
                return redirect(url_for('checkpoint_controller.list_checkpoints'))

        return render_template('add_checkpoint.html', user=user_session(session['user'], session['type']))

    return render_template('404.html', user=user_session(session['user'], session['type']))


@checkpoint_controller.route('/list-checkpoints/remove-checkpoint', methods=['GET', 'POST'])
@login_required
@required_roles('Mentor')
def delete_checkpoint():
    user = user_session(session['user'], session['type'])
    if isinstance(user, Mentor):
        if request.method == 'POST':
            if request.form['action']:
                checkpoint_name = request.form['checkpoint_name']
                Checkpoint.remove_checkpoint(checkpoint_name)
                return redirect(url_for('checkpoint_controller.list_checkpoints'))

    return render_template('404.html', user=user_session(session['user'], session['type']))


@checkpoint_controller.route('/list-checkpoints/<checkpoint_name>', methods=['GET', 'POST'])
@login_required
@required_roles('Mentor')
def grade_checkpoint(checkpoint_name):
    user = user_session(session['user'], session['type'])

    if isinstance(user, Mentor):
        if request.method == 'POST':
            id_list = request.form.getlist('id[]')
            grade_list = request.form.getlist('checkpoint-grade[]')
            Checkpoint.grade_checkpoints(grade_list, id_list)
            return redirect(url_for('checkpoint_controller.list_checkpoints'))

        chkp_list = Checkpoint.get_details_checkpoint_by_name(checkpoint_name)
        return render_template('grade_checkpoint.html', checkpoint_name=checkpoint_name, chkp_list=chkp_list,
                               user=user_session(session['user'], session['type']))

    return render_template('404.html', user=user_session(session['user'], session['type']))

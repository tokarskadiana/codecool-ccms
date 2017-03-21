from flask import Blueprint, session, render_template, redirect, url_for, flash, request
from controller.decorators import login_required, required_roles
from controller.user_session import user_session
from model.student import Student
from model.team import Team

student_controller = Blueprint('student_controller', __name__,
                               template_folder='templates')


# ----------------STUDENTS--------------


def save_student(save, id=None):
    student = Student(id=id,
                      first_name=request.form['first-name'],
                      last_name=request.form['last-name'],
                      password=request.form['password'],
                      telephone=request.form.get('phone-number', ''),
                      mail=request.form.get('mail', ''),
                      team_id=request.form.get('team', ''))
    if save == 'add':
        student.add_student()
    elif save == 'edit':
        student.edit_student()


@student_controller.route('/list-students', methods=['GET', 'POST'])
@login_required
@required_roles('Manager', 'Mentor', 'Employee')
def list_students():
    """
    GET to generate a list of students
    """
    students = Student.list_students()
    return render_template('viewstudents.html', user=user_session(session['user'], session['type']), students=students)


@student_controller.route('/list-students/add', methods=['GET', 'POST'])
@login_required
@required_roles('Mentor')
def add_student():
    """
    GET: returns add student formula
    POST: returns list of students with new student added
    """
    teams = Team.list_teams()
    if request.method == 'POST':
        save_student('add')
        return redirect(url_for('student_controller.list_students'))
    return render_template('student_form.html', user=user_session(session['user'], session['type']), teams=teams)


@student_controller.route('/list-students/edit/<student_id>', methods=['GET', 'POST'])
@login_required
@required_roles('Mentor')
def edit_student(student_id):
    """
    Edit student formula to edit student details
    :param student_id: int
    GET return edit student formula
    POST return list of students with edited student changes saved
    """
    teams = Team.list_teams()
    student = Student.get_by_id(student_id)
    if student:
        if request.method == 'POST':
            save_student('edit', student.id)
            return redirect(url_for('student_controller.list_students'))
        return render_template('edit_student_form.html', user=user_session(session['user'], session['type']),
                               student=student, teams=teams)
    return redirect('list-students')


@student_controller.route('/list-student/delete/<student_id>')
@login_required
@required_roles('Mentor')
def delete(student_id):
    """
    Remove student from list(data base)
    :param student_id: int
    GET return list of students without removed student
    """
    student = Student.get_by_id(student_id)
    if student:
        student.delete_student()
        return redirect(url_for('student_controller.list_students'))
    return redirect(url_for('student_controller.list_students'))

# ------------STUDENT STATISTICS------------------


@student_controller.route('/student-statistics')
@login_required
@required_roles('Manager', 'Mentor', 'Student')
def statistics():
    """Return statistics.html with Student objects."""
    students = Student.list_students()
    if session['type'] == 'Student':
        students = [student for student in students if student.id == int(session[
                                                                         'user'])]
    return render_template('statistics.html', user=user_session(session['user'], session['type']), students=students)

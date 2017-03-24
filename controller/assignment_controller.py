from flask import Blueprint, session, render_template, redirect, url_for, flash, request
from controller.decorators import login_required, required_roles
from controller.user_session import user_session
from model.team import Team
from model.mentor import Mentor
from model.student import Student
from model.submit import Submition
from model.assignment import Assignment


assignment_controller = Blueprint('assignment_controller', __name__,
                                  template_folder='templates')
# ------------ASSIGNMENTS----------------


@assignment_controller.route('/list-assignments')
@login_required
@required_roles('Mentor', 'Student')
def list_assignments():
    """
    List assignments

    GET: returns 404 or Student view or Mentor view
    POST: returns HTTP 200 on success and redirect to list-assignments page
    """

    user = user_session(session['user'], session['type'])
    if isinstance(user, Mentor):
        choose = "Mentor"
        assignListOfObjects = Assignment.get_list()
        return render_template('viewassignments.html', user=user_session(session['user'], session['type']),
                               choose=choose,
                               assignListOfObjects=assignListOfObjects)

    elif (isinstance(user, Student)):

        choose = "Student"
        student_id = user_session(session['user'], session['type']).id
        student_assignments = Assignment.get_all_assigmnets(student_id)

        return render_template('viewassignments.html', user=user_session(session['user'], session['type']),
                               choose=choose, student_assignments=student_assignments)
    else:
        return render_template('404.html', user=user_session(session['user'], session['type']))


@assignment_controller.route('/list-assignments/add-assignment', methods=['GET', 'POST'])
@login_required
@required_roles('Mentor')
def add_assignment():
    """
    Add assignment
    :return:
    """
    if request.method == 'POST':
        if request.form['add_assignment']:
            title = request.form['title']
            description = request.form['description']
            due_to = request.form['due_to']
            type = request.form['type']
            Assignment.create(title, description, type,
                              user_session(session['user'], session[
                                  'type']).username, due_to,
                              user_session(session['user'], session['type']).id)
            flash('Assignment was added')
            return redirect(url_for('assignment_controller.list_assignments'))

    return render_template('addassignment.html', user=user_session(session['user'], session['type']))


@assignment_controller.route('/list-assignments/grade-assignment', methods=['GET', 'POST'])
@login_required
@required_roles('Mentor')
def grade_assignment():
    """
    List user of assignments and add possibility to grade it
    :return:
    """
    if request.method == 'POST':
        if request.form['assignmentID']:
            assigID = Assignment.get_by_id(request.form['assignmentID'])
            studentsDetails = Assignment.get_students_of_assigmnent(assigID.id)

            return render_template('grade_assignment.html', user=user_session(session['user'], session['type']),
                                   students=studentsDetails, assignment=assigID)
    elif request.method == "GET":
        assigID = Assignment.get_by_id(request.args['assignmentID'])
        studentsDetails = Assignment.get_students_of_assigmnent(assigID.id)
        return render_template('grade_assignment.html', user=user_session(session['user'], session['type']),
                               students=studentsDetails, assignment=assigID)
    else:
        return render_template('404.html', user=user_session(session['user'], session['type']))


@assignment_controller.route('/list-assignments/grade-assignment/<username>', methods=['GET', 'POST'])
@login_required
@required_roles('Mentor')
def grade_user_assignments(username):
    """
    Grade assignment of user if you are mentor
    :param username:
    :return:
    """
    if request.method == "POST":

        if request.form['grade_user'] == 'grade':
            assignment_id = request.form['assignment']
            student_id = request.form['id']
            assignment = Assignment.get_by_id(assignment_id)
            student = Student.get_by_id(student_id)
            student_submit = Submition.get_submit(student_id, assignment_id)
            return render_template('grade_user_assignments.html', user=user_session(session['user'], session['type']),
                                   student=student, assignment=assignment,
                                   student_submit=student_submit)
        elif request.form['grade_user'] == 'Save':
            submit_id = request.form['submit_id']
            new_grade = request.form['new_grade']
            assignment_id = request.form['assignment_id']
            assignment = Assignment.get_by_id(assignment_id)
            submit = Submition.get_by_id(submit_id)
            if assignment.type == 'group':
                team_id = Student.get_by_id(submit.student_id).team_id
                team = Team.get_by_id(team_id)
                team_members = team.get_members()
                for student in team_members:
                    submit = Submition.get_submit(student.id, assignment_id)
                    submit.update_grade(new_grade)
            else:
                submit.update_grade(new_grade)
            return redirect(url_for('assignment_controller.grade_assignment', assignmentID=assignment_id))
    return render_template('404.html', user=user_session(session['user'], session['type']))


@assignment_controller.route('/list-assignments/view-assignments/<int:assignments_id>', methods=['GET', 'POST'])
@login_required
@required_roles('Student')
def view_assignments(assignments_id):
    """
    List all assignments of user
    :param assignments_id:
    :return:
    """
    assignment = Assignment.get_by_id(assignments_id)
    submit = Submition.get_submit(user_session(
        session['user'], session['type']).id, assignments_id)
    return render_template('stud_view_assiment.html', user=user_session(session['user'], session['type']),
                           assignment=assignment, submit=submit)


@assignment_controller.route('/list-assignments/view-assignments/<int:assignments_id>/submit_edition', methods=["GET", "POST"])
@login_required
@required_roles('Student')
def assignment_submit(assignments_id):
    """
    Student submit assignment
    :param assignments_id:
    :return:
    """
    assignment = Assignment.get_by_id(assignments_id)
    submit = Submition.get_submit(user_session(
        session['user'], session['type']).id, assignments_id)
    if request.method == "POST":
        content = request.form['content']
        if assignment.type == 'group':
            team_id = user_session(session['user'], session['type']).team_id
            team = Team.get_by_id(team_id)
            team_members = team.get_members()
            for student in team_members:
                submit = Submition.get_submit(student.id, assignments_id)
                submit.change_content(content)
        else:
            submit.change_content(content)
        return redirect(url_for('assignment_controller.view_assignments', assignments_id=assignments_id))

    return render_template('stud-submit.html', user=user_session(session['user'], session['type']),
                           assignment=assignment, submit=submit)


@assignment_controller.route('/list-assignments/delete/<assignment_id>')
@login_required
@required_roles('Mentor')
def delete_assignment(assignment_id):
    """
    Delete assignment
    :param assignment_id:
    :return:
    """
    assignment = Assignment.get_by_id(assignment_id)
    assignment.delete_assignment()
    return redirect(url_for('assignment_controller.list_assignments'))

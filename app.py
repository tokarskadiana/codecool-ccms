import os
from functools import wraps
from flask import Flask, render_template, request, redirect, url_for, session, flash
from controller.database_controller import DatabaseController
from model.manager import Manager
from model.mentor import Mentor
from model.student import Student
from model.submit import Submition
from model.team import Team
from model.assignment import Assignment
from model.attendance import Attendance
from model.employee import Employee
import datetime


app = Flask(__name__)
app.secret_key = os.urandom(24)


# login required decorator
def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('You need to login first')
            return redirect(url_for('login'))

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


# redirect to index page if url was not found
@app.errorhandler(404)
@login_required
def page_not_found(e):
    flash('Such url doesn\'t exist')
    return render_template('index.html', user=user_session(session['user'], session['type'])), 404


@app.route('/')
@login_required
def index():
    """
    handle main index page, display nav of curent user
    :return:
    """
    return render_template('index.html', user=user_session(session['user'], session['type']))


# -----------------LOGIN------------------

@app.route("/login", methods=["GET", "POST"])
def login():
    error = None
    students = Student.list_students()
    employees = Employee.list_employee('assistant')
    mentors = Mentor.list_mentors()
    managers = Manager.list_managers()
    all_users = students + employees + mentors + managers

    if request.method == "POST":
        for user in all_users:
            if request.form['username'] == user.username and request.form['password'] == user.password:
                session['logged_in'] = True
                session['user'] = user.id
                session['type'] = user.__class__.__name__
                return redirect(url_for('index'))
            else:
                error = "Invalid Credentials. Please Try Again "

    return render_template("login.html", error=error)


@app.route("/logout", methods=["GET", "POST"])
def logout():
    session.pop('logged_in', None)
    session.pop('user', None)
    session.pop('type', None)
    flash('You are logged out, Have Fun')
    return redirect(url_for('login'))


# -----------------EMPLOYEE------------------


def save_employee(position, save, id=None):
    employee = Employee(id=id,
                        password=request.form['password'],
                        first_name=request.form['first_name'],
                        last_name=request.form['last_name'],
                        position=position,
                        telephone=request.form.get('phone_number', ''),
                        mail=request.form.get('mail', ''),
                        salary=request.form.get('salary', ''))
    if save == 'add':
        employee.add_employee()
    elif save == 'edit':
        employee.edit_employee()


# ----------------MENTORS-----------------


@app.route('/list-mentors')
@login_required
@required_roles('Manager')
def list_mentors():
    """
    :return:
    """
    mentors_list = Mentor.list_mentors()
    add = 'add_mentor'
    edit = 'edit_mentor'
    delete = 'delete_mentor'
    return render_template('viewemployee.html', user=user_session(session['user'], session['type']),
                           employee_list=mentors_list, employee='Mentor',
                           add=add, edit=edit, delete=delete)


@app.route('/list-mentors/add', methods=['GET', 'POST'])
@login_required
@required_roles('Manager')
def add_mentor():
    if request.method == 'POST':
        save_employee('mentor', 'add')
        return redirect(url_for('list_mentors'))
    return render_template('addemployee.html', user=user_session(session['user'], session['type']), list='list_mentors')


@app.route('/list-mentors/edit/<employee_id>', methods=['GET', 'POST'])
@login_required
@required_roles('Manager')
def edit_mentor(employee_id):
    mentor = Mentor.get_by_id(employee_id)
    if request.method == 'POST':
        save_employee('mentor', 'edit', mentor.id)
        return redirect('list-mentors')
    return render_template('editemployee.html', user=user_session(session['user'], session['type']), employee=mentor,
                           list='list_mentors')


@app.route('/delete-mentor/<employee_id>')
@login_required
@required_roles('Manager')
def delete_mentor(employee_id):
    """
    :return:
    """
    mentor = Mentor.get_by_id(employee_id)
    mentor.delete_employee()
    return redirect('list-mentors')


# ----------------ASSISTANTS-----------------


@app.route('/list-assistants')
@login_required
@required_roles('Manager')
def list_assistants():
    """
    :return:
    """
    assistants_list = Employee.list_employee('assistant')
    add = 'add_assistant'
    edit = 'edit_assistant'
    delete = 'delete_assistant'
    return render_template('viewemployee.html', user=user_session(session['user'], session['type']),
                           employee_list=assistants_list, employee='Assistant',
                           add=add, edit=edit, delete=delete)


@app.route('/list-assistants/add', methods=['GET', 'POST'])
@login_required
@required_roles('Manager')
def add_assistant():
    if request.method == 'POST':
        save_employee('assistant', 'add')
        return redirect(url_for('list_assistants'))
    return render_template('addemployee.html', user=user_session(session['user'], session['type']),
                           employee='Assistant', list='list_assistants')


@app.route('/list-assistant/edit/<employee_id>', methods=['GET', 'POST'])
@login_required
@required_roles('Manager')
def edit_assistant(employee_id):
    assistant = Employee.get_by_id(employee_id, 'assistant')
    if request.method == 'POST':
        save_employee('assistant', 'edit', assistant.id)
        return redirect('list-assistants')
    return render_template('editemployee.html', user=user_session(session['user'], session['type']), employee=assistant,
                           list='list_assistants')


@app.route('/delete-assistant/<employee_id>')
@login_required
@required_roles('Manager')
def delete_assistant(employee_id):
    """
    :return:
    """
    assistant = Employee.get_by_id(employee_id, 'assistant')
    assistant.delete_employee()
    return redirect('list-assistants')


# ----------------STUDENTS--------------


@app.route('/list-students', methods=['GET', 'POST'])
@login_required
@required_roles('Manager', 'Mentor', 'Employee')
def list_students():
    """

    :return:
    """
    students = Student.list_students()
    return render_template('viewstudents.html', user=user_session(session['user'], session['type']), students=students)


@app.route('/list-students/add', methods=['GET', 'POST'])
@login_required
@required_roles('Mentor')
def add_student():
    """
    """
    teams = Team.list_teams()
    if request.method == 'POST':
        student = Student(id=None,
                          first_name=request.form['first-name'],
                          last_name=request.form['last-name'],
                          password=request.form['password'],
                          telephone=request.form.get('phone-number', ''),
                          mail=request.form.get('mail', ''),
                          team_id=request.form.get('team', ''))
        student.add_student()
        return redirect(url_for('list_students'))
    return render_template('student_form.html', user=user_session(session['user'], session['type']), teams=teams)


@app.route('/list-students/edit/<student_id>', methods=['GET', 'POST'])
@login_required
@required_roles('Mentor')
def edit_student(student_id):
    teams = Team.list_teams()
    student = Student.get_by_id(student_id)
    if student:
        if request.method == 'POST':
            Student(id=student.id,
                    first_name=request.form['first-name'],
                    last_name=request.form['last-name'],
                    password=request.form['password'],
                    telephone=request.form.get('phone-number', ''),
                    mail=request.form.get('mail', ''),
                    team_id=request.form.get('team', '')).edit_student()
            return redirect(url_for('list_students'))
        return render_template('edit_student_form.html', user=user_session(session['user'], session['type']),
                               student=student, teams=teams)
    return redirect('list-students')


@app.route('/list-student/delete/<student_id>')
@login_required
@required_roles('Mentor')
def delete(student_id):
    student = Student.get_by_id(student_id)
    if student:
        student.delete_student()
        return redirect('list-students')
    return redirect('list-students')


# ------------STUDENT STATISTICS------------------


@app.route('/student-statistics')
@login_required
@required_roles('Manager', 'Mentor', 'Student')
def statistics():
    """Return statistics.html with Student objects."""
    students = Student.list_students()
    if session['type'] == 'Student':
        students = [student for student in students if student.id == int(session['user'])]
    return render_template('statistics.html', user=user_session(session['user'], session['type']), students=students)


# ------------TEAMS----------------


@app.route('/list-teams')
@login_required
@required_roles('Mentor')
def list_teams():
    """Return viewteams.html with list of id teams and teams names."""
    teams = Team.list_teams()
    return render_template('viewteams.html', user=user_session(session['user'], session['type']), teams=teams)


@app.route('/list-teams/add', methods=["GET", 'POST'])
@login_required
@required_roles('Mentor')
def add_team():
    """
    Return team_form.html
    POST: Add team to database basing on data from request.form['name'] and redirect user to list-teams definition.
    """
    if request.method == 'POST':
        Team(request.form['name']).add_team()
        return redirect('list-teams')
    return render_template("team_form.html", user=user_session(session['user'], session['type']))


@app.route('/list-teams/edit/<team_id>', methods=["GET", 'POST'])
@login_required
@required_roles('Mentor')
def edit_team(team_id):
    """
    Return team_form.html with team basing on given team_id
    POST: Edit team with given values in request.form['name'] and redirect user to list-teams definition.
    :param team_id: team id in database
    """
    team = Team.get_by_id(team_id)
    if request.method == 'POST':
        team.name = request.form['name']
        team.edit_team()
        return redirect(url_for('list_teams'))
    return render_template('team_form.html', user=user_session(session['user'], session['type']), team=team)


@app.route('/list-teams/delete/<team_id>')
@login_required
@required_roles('Mentor')
def delete_team(team_id):
    """Delete from database team by given id in team_id"""
    team = Team.get_by_id(team_id)
    team.delete_team()
    return redirect(url_for('list_teams'))


# ------------ASSIGNMENTS----------------


@app.route('/list-assignments')
@login_required
@required_roles('Mentor', 'Student')
def list_assignments():
    """
    List all assignments
    :return: template
    """

    user = user_session(session['user'], session['type'])
    choose = None
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


@app.route('/list-assignments/add-assignment', methods=['GET', 'POST'])
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
            return redirect(url_for('list_assignments'))

    return render_template('addassignment.html', user=user_session(session['user'], session['type']))


@app.route('/list-assignments/grade-assignment', methods=['GET', 'POST'])
@login_required
@required_roles('Mentor')
def grade_assignment():
    """
    List user of assignment
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
        return "Not Implemented"


@app.route('/list-assignments/grade-assignment/<username>', methods=['GET', 'POST'])
@login_required
@required_roles('Mentor')
def grade_user_assignments(username):
    """
    Grade assignment
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
            return redirect(url_for('grade_assignment', assignmentID=assignment_id))
    return 'Not permited fool'


@app.route('/list-assignments/view-assignments/<int:assignments_id>', methods=['GET', 'POST'])
@login_required
@required_roles('Student')
def view_assignments(assignments_id):
    """
    Student list assignments
    :param assignments_id:
    :return:
    """
    assignment = Assignment.get_by_id(assignments_id)
    submit = Submition.get_submit(user_session(
        session['user'], session['type']).id, assignments_id)
    return render_template('stud_view_assiment.html', user=user_session(session['user'], session['type']),
                           assignment=assignment, submit=submit)


@app.route('/list-assignments/view-assignments/<int:assignments_id>/submit_edition', methods=["GET", "POST"])
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
        return redirect(url_for('view_assignments', assignments_id=assignments_id))

    return render_template('stud-submit.html', user=user_session(session['user'], session['type']),
                           assignment=assignment, submit=submit)


@app.route('/list-assignments/delete/<assignment_id>')
@login_required
@required_roles('Mentor')
def delete_assignment(assignment_id):
    assignment = Assignment.get_by_id(assignment_id)
    assignment.delete_assignment()
    return redirect(url_for('list_assignments'))


# ---------------ATTENDANCE-----------------


@app.route("/attendance", methods=['GET', 'POST'])
@login_required
@required_roles('Mentor')
def attendance():
    """
    GET: Return attendance.html with Students object.
    POST: Add or update attendance in database by given value in request.form. Redirect to attendance definition.
    """
    students = Student.list_students()
    date = datetime.datetime.now().strftime("%Y-%m-%d")
    students_checked = Attendance.get_attendance_day(date)
    if request.method == 'POST':
        if Attendance.already_checked(date):
            for student in students_checked:
                value = int(request.form[str(student[0])])
                Attendance.update_attendance_day(
                    int(student[0]), date, int(value))
        else:
            for student in students:
                value = int(request.form[str(student.id)])
                Attendance.add(student.id, value, date)
        return redirect(url_for('attendance'))
    if Attendance.already_checked(date):
        return render_template('attendance.html', user=user_session(session['user'], session['type']),
                               students_checked=students_checked, date=date)
    return render_template('attendance.html', user=user_session(session['user'], session['type']), students=students,
                           date=date)


# -------------OTHER STAFF--------------


@app.context_processor
def override_url_for():
    """Overrides url_for with additional values on end (cache prevent)"""
    return dict(url_for=dated_url_for)


def dated_url_for(endpoint, **values):
    """Add on end to static files a int value(time)  """
    if endpoint == 'static':
        filename = values.get('filename', None)
        if filename:
            file_path = os.path.join(app.root_path,
                                     endpoint, filename)
            values['q'] = int(os.stat(file_path).st_mtime)
    return url_for(endpoint, **values)


def user_session(id, class_name):
    """Return object with given class name in class_name and id"""
    if class_name == "Student":

        return Student.get_by_id(id)
    elif class_name == "Mentor":

        return Mentor.get_by_id(id)
    elif class_name == "Employee":

        return Employee.get_by_id(id, 'assistant')
    elif class_name == "Manager":

        return Manager.get_by_id(id)
    return None


if __name__ == '__main__':
    DatabaseController.createSqlDatabase()
    DatabaseController.sample_data()
    app.run(debug=True)

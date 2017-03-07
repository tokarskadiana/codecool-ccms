import os

from flask import Flask, render_template, request, redirect, url_for
from model.student import Student
from model.submit import Submition
from model.team import Team
from controller.database_controller import DatabaseController
from model.assignment import Assignment
from model.employee import Employee
from model.mentor import Mentor
from model.student import Student

app = Flask(__name__)

app.user = Mentor('kkk', 'mateusz', 'ostafil', '123123123', 'mateusz@ostafil.pl', 842, 5000)
print(app.user.__dict__)


@app.route('/')
def index():
    """
    handle main index page, display nav of curent user
    :return:
    """
    return render_template('index.html')


@app.route('/list-mentors', methods=['GET', 'POST'])
def list_mentors():
    """

    :return:
    """

    if request.method == 'GET':
        mentorsObjectList = Mentor.list_mentors()
        print(mentorsObjectList[0])
        return render_template('viewmentors.html', mentorsObjectList=mentorsObjectList)

    if request.method == 'POST':
        pass

    return render_template('viewmentors.html')


@app.route('/delete-mentor/<mentor_id>')
def delete_mentor():
    """

    :return:
    """
    if request.method == 'GET':
        mentorsObjectList = Mentor.list_mentors()
        print(mentorsObjectList[0])
        return render_template('viewmentors.html', mentorsObjectList=mentorsObjectList)

    return redirect(render_template('viewmentors.html'))


@app.route('/list-students', methods=['GET', 'POST'])
def list_students():
    """

    :return:
    """
    students = Student.list_students()
    return render_template('viewstudents.html', students=students)


@app.route('/list-students/add', methods=['GET', 'POST'])
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
                          team_id=request.form['team'])
        student.add_student()
        return redirect(url_for('list_students'))
    return render_template('student_form.html', teams=teams)


@app.route('/list-students/edit/<student_id>', methods=['GET', 'POST'])
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
                    team_id=request.form['team']).edit_student()
            return redirect('list-students')
        return render_template('edit_student_form.html', student=student, teams=teams)
    return redirect('list-students')


@app.route('/list-student/delete/<student_id>')
def delete(student_id):
    student = Student.get_by_id(student_id)
    if student:
        student.delete_student()
        return redirect('list-students')
    return redirect('list-students')


@app.route('/student-statistics')
def statistics():
    students = Student.list_students()
    return render_template('statistics.html', students=students)


@app.route('/list-teams')
def list_teams():
    teams = Team.list_teams()
    return render_template('viewteams.html', teams=teams)


@app.route('/list-teams/add', methods=["GET", 'POST'])
def add_team():
    if request.method == 'POST':
        Team(request.form['name']).add_team()
        return redirect('list-teams')
    return render_template("team_form.html")


@app.route('/list-teams/edit/<team_id>', methods=["GET", 'POST'])
def edit_team(team_id):
    team = Team.get_by_id(team_id)
    if request.method == 'POST':
        team.name = request.form['name']
        team.edit_team()
        return redirect(url_for('list_teams'))
    return render_template('team_form.html', team=team)


@app.route('/list-teams/delete/<team_id>')
def delete_team(team_id):
    team = Team.get_by_id(team_id)
    team.delete_team()
    return redirect(url_for('list_teams'))


@app.route('/list-assistants', methods=['GET', 'POST'])
def list_assistants():
    """

    :return:
    """

    if request.method == 'POST':
        pass

    return render_template('viewassistants.html')


@app.route('/list-assignments')
def list_assignments():
    """

    :return:
    """
    if isinstance(app.user, Mentor):
        assignListOfObjects = Assignment.get_list()
        return render_template('viewassignments.html', assignListOfObjects=assignListOfObjects)
    elif (isinstance(app.user, Student)):
        pass
    else:
        return render_template('404.html')


@app.route('/list-assignments/add-assignment', methods=['GET', 'POST'])
def add_assignment():
    if request.method == 'POST':
        if request.form['add_assignment']:
            title = request.form['title']
            description = request.form['description']
            due_to = request.form['due_to']
            type = request.form['type']
            Assignment.create(title, description, type, app.user.username, due_to)
            return redirect(url_for('list_assignments'))

    return render_template('addassignment.html')


@app.route('/list-assignments/grade-assignment', methods=['GET', 'POST'])
def grade_assignment():
    if request.method == 'POST':
        if request.form['assignmentID']:
            assigID = Assignment.get_by_id(request.form['assignmentID'])
            studentsDetails = Assignment.get_studentsOfAssigmnent(assigID.id)

            return render_template('grade_assignment.html', students=studentsDetails, assignment=assigID)
    elif request.method == "GET":
        assigID = Assignment.get_by_id(request.args['assignmentID'])
        studentsDetails = Assignment.get_studentsOfAssigmnent(assigID.id)
        return render_template('grade_assignment.html', students=studentsDetails, assignment=assigID)
    else:
        return "Not Implemented"


@app.route('/list-assignments/grade-assignment/<username>', methods=['GET', 'POST'])
def grade_user_assignments(username):
    if request.method == "POST":

        if request.form['grade_user'] == 'grade':
            assignment_id = request.form['assignment']
            student_id = request.form['id']
            assignment = Assignment.get_by_id(assignment_id)
            student = Student.get_by_id(student_id)
            student_submit = Submition.get_submit(student_id, assignment_id)
            return render_template('grade_user_assignments.html', student=student, assignment=assignment,
                                   student_submit=student_submit)
        elif request.form['grade_user'] == 'Save':
            submit_id = request.form['submit_id']
            new_grade = request.form['new_grade']
            assignment_id = request.form['assignment_id']
            print(new_grade)
            submit = Submition.get_by_id(submit_id)
            print(submit)
            submit.update_grade(new_grade)
            return redirect(url_for('grade_assignment', assignmentID=assignment_id))
    return 'Not permited fool'


@app.context_processor
def override_url_for():
    return dict(url_for=dated_url_for)


def dated_url_for(endpoint, **values):
    if endpoint == 'static':
        filename = values.get('filename', None)
        if filename:
            file_path = os.path.join(app.root_path,
                                     endpoint, filename)
            values['q'] = int(os.stat(file_path).st_mtime)
    return url_for(endpoint, **values)

# WTF IS THIS ?
# @app.route('/view-teams', methods=['GET', 'POST'])
# def list_teams():
#     """
#
#     :return:
#     """
#     if request.method == 'POST':
#         pass
#
#     return render_template('viewteams.html')


@app.route('/test', methods=['GET', 'POST'])
def test():
    if request.method == 'POST':
        users = request.form.getlist('users')
    return render_template('test.html')


def xxx():
    return 'lol'


if __name__ == '__main__':
    DatabaseController.createSqlDatabase()
    DatabaseController.sample_data()
    app.run(debug=True)

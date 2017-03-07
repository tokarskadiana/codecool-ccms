from flask import Flask, render_template, request, redirect, url_for
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
    if request.method == 'POST':
        pass

    return render_template('viewstudents.html')


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
            assigID = request.form['assignmentID']
            studentsObjectList = Student.list_students()
            return render_template('grade_assignment.html')

    return render_template('grade_assignment.html')


@app.route('/view-teams', methods=['GET', 'POST'])
def list_teams():
    """

    :return:
    """
    if request.method == 'POST':
        pass

    return render_template('viewteams.html')


if __name__ == '__main__':
    DatabaseController.createSqlDatabase()
    DatabaseController.sample_data()
    app.run(debug=True)

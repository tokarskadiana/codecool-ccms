from flask import Flask, render_template, request, redirect, url_for

from controller.database_controller import DatabaseController
from model.assignment import Assignment
from model.employee import Employee

app = Flask(__name__)

app.user = Employee('kkk','mateusz','ostafil','123123123','mateusz@ostafil.pl')


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
    if request.method == 'POST':
        pass


    return render_template('viewmentors.html')


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
    assignListOfObjects = Assignment.get_list()

    return render_template('viewassignments.html',assignListOfObjects = assignListOfObjects)

@app.route('/list-assignments/add-assignments', methods=['GET', 'POST'])
def add_assignments():

    return render_template('addassignment.html')

if __name__ == '__main__':
    DatabaseController.createSqlDatabase()
    DatabaseController.sample_data()
    app.run(debug=True)

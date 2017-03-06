from flask import Flask, render_template, request, redirect, url_for

from controller.database_controller import DatabaseController
from model.mentor import Mentor

app = Flask(__name__)

app.user = None


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


@app.route('/list-assignments', methods=['GET', 'POST'])
def list_assignments():
    """

    :return:
    """

    if request.method == 'POST':
        pass

    return render_template('viewassignments.html')


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

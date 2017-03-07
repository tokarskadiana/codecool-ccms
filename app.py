from flask import Flask, render_template, request, redirect, url_for
from model.employee import Employee
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
    assistants = Employee.list_employee()
    if request.method == 'POST':
        pass

    return render_template('viewassistants.html', assistants=assistants)


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


@app.route("/remove-assistant/<assistant_id>")
def remove_assistant(assistant_id):
    """ Removes assistant with selected id from the database """
    employee = Employee.get_assistant_by_id(assistant_id)
    employee.delete()
    return redirect(url_for('list_assistants'))

@app.route("/editassistant/<assistant_id>", methods=['GET', 'POST'])
def edit_assistant(assistant_id):
    """ Edits todo item with selected id in the database
    If the method was GET it should show todo item form.
    If the method was POST it shold update todo item in database.
    """
    assistant = Employee.get_assistant_by_id(assistant_id)
    if request.method == 'GET':
        return render_template('editassistant.html', assistant=assistant)
    elif request.method == 'POST':
        assistant.first_name =request.form['first-name']
        assistant.last_name = request.form['last-name']
        assistant.telephone = request.form['phone-number']
        assistant.mail = request.form['mail']
        assistant.salary = request.form['salary']
        assistant.username = assistant.get_username()
        assistant.save()
        return redirect(url_for('list_assistants'))

@app.route("/addassistant", methods=['GET', 'POST'])
def add_assistant():
    if request.method == 'POST':
        first_name = request.form['first-name']
        last_name = request.form['last-name']
        telephone = request.form['phone-number']
        email = request.form['email']
        salary = request.form['salary']
        password = request.form['password']
        employee = Employee(password, first_name, last_name, telephone, email, salary)
        employee.position = 'employee'
        employee.save()
        return redirect(url_for('list_assistants'))
    return render_template('addassistant.html')

if __name__ == '__main__':
    DatabaseController.createSqlDatabase()
    DatabaseController.sample_data()
    app.run(debug=True)

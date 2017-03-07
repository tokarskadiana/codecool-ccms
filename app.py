from flask import Flask, render_template, request, redirect, url_for
from model.student import Student
from model.team import Team
from controller.database_controller import DatabaseController

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
    if request.method == 'POST':
        pass

    return render_template('viewmentors.html')


@app.route('/list-students')
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


if __name__ == '__main__':
    DatabaseController.createSqlDatabase()
    DatabaseController.sample_data()
    app.run(debug=True)

import os
from flask import Flask, render_template, request, redirect, url_for
from controller.database_controller import DatabaseController
from model.student import Student
from model.submit import Submition
from model.team import Team
from model.assignment import Assignment
from model.attendance import Attendance
from model.employee import Employee
import datetime


app = Flask(__name__)

app.user = Employee(id=120,
                    password='kkk',
                    first_name='Mateusz',
                    last_name='Ostafil',
                    position='mentor',
                    telephone="222")


@app.route('/')
def index():
    """
    handle main index page, display nav of curent user
    :return:
    """
    return render_template('index.html', user=app.user)


# -----------------EMPLOYEE------------------


def add_employee(position):
    Employee(id=None,
             password=request.form['password'],
             first_name=request.form['first_name'],
             last_name=request.form['last_name'],
             position=position,
             telephone=request.form.get('phone_number', ''),
             mail=request.form.get('mail', ''),
             salary=request.form.get('salary', '')).add_employee()


def edit_employee(position, employee):
    Employee(id=employee.id,
             first_name=request.form['first_name'],
             password=request.form['password'],
             last_name=request.form['last_name'],
             position=position,
             telephone=request.form.get('phone_number', ''),
             mail=request.form.get('mail', ''),
             salary=request.form.get('salary', '')).edit_employee()


# ----------------MENTORS-----------------


@app.route('/list-mentors')
def list_mentors():
    """
    :return:
    """
    mentors_list = Employee.list_employee('mentor')
    add = 'add_mentor'
    edit = 'edit_mentor'
    delete = 'delete_mentor'
    return render_template('viewemployee.html', user=app.user, employee_list=mentors_list, employee='Mentor',
                           add=add, edit=edit, delete=delete)


@app.route('/list-mentors/add', methods=['GET', 'POST'])
def add_mentor():
    if request.method == 'POST':
        add_employee('mentor')
        return redirect(url_for('list_mentors'))
    return render_template('addemployee.html', user=app.user, list='list_mentors')


@app.route('/list-mentors/edit/<employee_id>', methods=['GET', 'POST'])
def edit_mentor(employee_id):
    mentor = Employee.get_by_id(employee_id)
    if request.method == 'POST':
        edit_employee('mentor', mentor)
        return redirect('list-mentors')
    return render_template('editemployee.html', user=app.user, employee=mentor, list='list_mentors')


@app.route('/delete-mentor/<employee_id>')
def delete_mentor(employee_id):
    """
    :return:
    """
    mentor = Employee.get_by_id(employee_id)
    mentor.delete_employee()
    return redirect('list-mentors')


# ----------------ASSISTANTS-----------------


@app.route('/list-assistants')
def list_assistants():
    """
    :return:
    """
    assistants_list = Employee.list_employee('assistant')
    add = 'add_assistant'
    edit = 'edit_assistant'
    delete = 'delete_assistant'
    return render_template('viewemployee.html', user=app.user, employee_list=assistants_list, employee='Assistant',
                           add=add, edit=edit, delete=delete)


@app.route('/list-assistants/add', methods=['GET', 'POST'])
def add_assistant():
    if request.method == 'POST':
        add_employee('assistant')
        return redirect(url_for('list_assistants'))
    return render_template('addemployee.html', user=app.user, employee='Assistant', list='list_assistants')


@app.route('/list-assistant/edit/<employee_id>', methods=['GET', 'POST'])
def edit_assistant(employee_id):
    assistant = Employee.get_by_id(employee_id)
    if request.method == 'POST':
        edit_employee('assistant', assistant)
        return redirect('list-assistants')
    return render_template('editemployee.html', user=app.user, employee=assistant, list='list_assistants')


@app.route('/delete-assistant/<employee_id>')
def delete_assistant(employee_id):
    """
    :return:
    """
    assistant = Employee.get_by_id(employee_id)
    assistant.delete_employee()
    return redirect('list-assistants')

# ----------------STUDENTS--------------


@app.route('/list-students', methods=['GET', 'POST'])
def list_students():
    """

    :return:
    """
    students = Student.list_students()
    return render_template('viewstudents.html', user=app.user, students=students)


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
    return render_template('student_form.html', user=app.user, teams=teams)


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
        return render_template('edit_student_form.html', user=app.user, student=student, teams=teams)
    return redirect('list-students')


@app.route('/list-student/delete/<student_id>')
def delete(student_id):
    student = Student.get_by_id(student_id)
    if student:
        student.delete_student()
        return redirect('list-students')
    return redirect('list-students')


# ------------STUDENT STATISTICS------------------


@app.route('/student-statistics')
def statistics():
    students = Student.list_students()
    return render_template('statistics.html', user=app.user, students=students)


# ------------TEAMS----------------


@app.route('/list-teams')
def list_teams():
    teams = Team.list_teams()
    return render_template('viewteams.html', user=app.user, teams=teams)


@app.route('/list-teams/add', methods=["GET", 'POST'])
def add_team():
    if request.method == 'POST':
        Team(request.form['name']).add_team()
        return redirect('list-teams')
    return render_template("team_form.html", user=app.user)


@app.route('/list-teams/edit/<team_id>', methods=["GET", 'POST'])
def edit_team(team_id):
    team = Team.get_by_id(team_id)
    if request.method == 'POST':
        team.name = request.form['name']
        team.edit_team()
        return redirect(url_for('list_teams'))
    return render_template('team_form.html', user=app.user, team=team)


@app.route('/list-teams/delete/<team_id>')
def delete_team(team_id):
    team = Team.get_by_id(team_id)
    team.delete_team()
    return redirect(url_for('list_teams'))


# ------------ASSIGNMENTS----------------


@app.route('/list-assignments')
def list_assignments():
    """

    :return:
    """
    if isinstance(app.user, Employee):
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
            Assignment.create(title, description, type,
                              app.user.username, due_to, app.user.id)
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


# -------------OTHER STAFF--------------


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


@app.route("/attendance", methods=['GET', 'POST'])
def attendance():
    students = Student.list_students()
    date = datetime.datetime.now().strftime("%Y-%m-%d")
    students_checked = Attendance.get_attendance_day(date)
    if request.method == 'POST':
        if Attendance.already_checked(date):
            for student in students_checked:
                value = int(request.form[str(student[0])])
                Attendance.update_attendance_day(int(student[0]), date, int(value))
        else:
            for student in students:
                value = int(request.form[str(student.id)])
                Attendance.add(student.id, value, date)
        return redirect(url_for('attendance'))
    if Attendance.already_checked(date):
        return render_template('attendance.html', user=app.user, students_checked=students_checked, date=date)
    return render_template('attendance.html', user=app.user, students=students, date=date)

if __name__ == '__main__':
    DatabaseController.createSqlDatabase()
    DatabaseController.sample_data()
    app.run(debug=True)

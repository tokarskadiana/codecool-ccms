from flask import Blueprint, session, render_template, redirect, url_for, flash, request
from controller.decorators import login_required, required_roles
from controller.user_session import user_session
import datetime
from model.attendance import Attendance
from model.student import Student


attendance_controller = Blueprint('attendance_controller', __name__,
                                  template_folder='templates')
# ---------------ATTENDANCE-----------------


@attendance_controller.route("/attendance", methods=['GET', 'POST'])
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
        return redirect(url_for('attendance_controller.attendance'))
    if Attendance.already_checked(date):
        return render_template('attendance.html', user=user_session(session['user'], session['type']),
                               students_checked=students_checked, date=date)
    return render_template('attendance.html', user=user_session(session['user'], session['type']), students=students,
                           date=date)

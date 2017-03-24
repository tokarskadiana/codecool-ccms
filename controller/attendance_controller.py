from flask import Blueprint, session, render_template, redirect, url_for, flash, request
from controller.decorators import login_required, required_roles
from controller.user_session import user_session
import datetime
from model.attendance import Attendance
from model.student import Student


attendance_controller = Blueprint('attendance_controller', __name__,
                                  template_folder='templates')


@attendance_controller.route("/attendance", methods=['GET', 'POST'])
@login_required
@required_roles('Mentor')
def attendance():
    """
    GET: Return attendance.html with Students object.
    POST: Add or update attendance in database by given value in request.form. Redirect to attendance definition.
    """
    students = Student.list_students()
    date = datetime.datetime.today().date()
    students_checked = Attendance.get_attendance_day(date)
    if request.method == 'POST':
        if Attendance.already_checked(date):
            for student in students_checked:
                status = bool(int(request.form[str(student[0])]))
                Attendance.update_attendance_day(int(student[0]), date, status)
            flash('Attendence was updated')
        else:
            for student in students:
                status = bool(request.form[str(student.id)])
                Attendance(date, status, student.id).add()
                flash('Attendence was checked')
        return redirect(url_for('attendance_controller.attendance'))
    return render_template('attendance.html', user=user_session(session['user'], session['type']), students=students,
                           date=date, students_checked=students_checked)

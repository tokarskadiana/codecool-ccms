from model.student import Student
from model.sql_alchemy_db import db


class Attendance(db.Model):
    '''
    Class representing attendance object.
    '''
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date)
    status = db.Column(db.Boolean)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'))

    def __init__(self, date, status, student_id):
        """
        Initialize Assignment object.
        :param date (str): date of checking attendance
        """
        self.date = date
        self.status = status
        self.student_id = student_id

    def add(self):
        """
        Add Attendance objc to list_of_attendance.
        """
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def already_checked(date):
        """
        Check if in given date was checked presence.
        :param date: date
        :return: boolean
        """
        checked_day = Attendance.query.filter_by(date=date).first()
        if checked_day:
            return True
        return False

    @staticmethod
    def get_attendance_day(date):
        """
        Get presence from given date.
        :param date: date
        :return: list of list
        """
        students_presence = Attendance.query.filter_by(date=date).join(Student).values(Attendance.student_id,
                                                                                       Attendance.status,
                                                                                       Student.first_name,
                                                                                       Student.last_name)
        students_presence = [list(student) for student in students_presence]
        if students_presence:
            for student in students_presence:
                student[0] = str(student[0])
        return students_presence

    @staticmethod
    def update_attendance_day(student_id, date, status):
        """
        Update presence day by given id and date.
        :param id: id
        :param _date: date
        :param value: 1 to presence or 0 for absent
        """
        attendance = Attendance.query.filter_by(date=date, student_id=student_id).first()
        attendance.status = status
        db.session.commit()

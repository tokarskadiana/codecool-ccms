from model.sqlRequest import SqlRequest
import datetime


class Attendance:
    def __init__(self, date, student_presence):
        """
        Initialize Assignment object.
        :param date (str): date of checking attendance
        """
        self.date = date
        self.student_presence = student_presence

    @staticmethod
    def add(id, value, date):
        """
        Add Attendance objc to list_of_attendance.
        """

        request = 'INSERT INTO attendance (student_id, "date", status) VALUES ("{}","{}","{}")'.format(
            id, date, value)
        SqlRequest.sql_request(request)

    @staticmethod
    def already_checked(date):
        """
        Check if in given date was checked presence.
        :param date: date
        :return: boolean
        """
        checked_day = SqlRequest.sql_request('SELECT * FROM attendance WHERE "date"=="{}" LIMIT 1'.format(date))
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
        students_presence = SqlRequest.sql_request(
            'SELECT student.ID, attendance.status, student.first_name, student.last_name FROM attendance LEFT JOIN \
            student ON attendance.student_id=student.ID WHERE attendance."date"="{}"'.format(date))
        students_presence = [list(student) for student in students_presence]
        if students_presence:
            for student in students_presence:
                student[0] = str(student[0])
        return students_presence

    @staticmethod
    def update_attendance_day(id, _date, value):
        """
        Update presence day by given id and date.
        :param id: id
        :param _date: date
        :param value: 1 to presence or 0 for absent
        """
        SqlRequest.sql_request('UPDATE attendance SET status="{}" WHERE student_id="{}" AND \
        "date"="{}"'.format(value, id, _date))

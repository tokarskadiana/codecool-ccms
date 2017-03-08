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

    def check_attendance(self, username, present):
        """
        Change value of presence.
        :param username(str): username of student
        :param present(int): change value of student presence (0 or 1)
        """
        if present == '0' or present == '1':
            self.student_presence[username] = present

    @staticmethod
    def list_attendance(username):
        """
        Return dict of overall presence of given username. day:value of present.
        :return (dict): example {'10.10.2015': 0, '11.10.2015': 1}
        """
        present_list = {}
        for days in Attendance.list_of_attendance:
            for student, present in days.student_presence.items():
                if username == student:
                    present_list[days.date] = present

        return present_list

    @staticmethod
    def add(id, value, date):
        """
        Add Attendance objc to list_of_attendance.
        """

        request = 'INSERT INTO attendance (student_id, "date", status) VALUES ("{}","{}","{}")'.format(
            id, date, value)
        SqlRequest.sql_request(request)

    @staticmethod
    def present_statistic():
        """
        Calculate overall present for each student.
        :return (dict): SAMPLE DICT {'patrycja': '100', 'przemek': '50'}
        """
        percent_of_presence = {}

        request = 'SELECT student_id, status FROM attendance'
        stats = SqlRequest.sql_request(request)
        if stats:
            for pers_stat in stats:
                request_s = 'SELECT first_name, last_name FROM student WHERE ID="{}"'.format(pers_stat[
                                                                                                 0])
                output = SqlRequest.sql_request(request_s)
                full_name = output[0][1] + ' ' + output[0][1]
                if full_name in percent_of_presence.keys():
                    percent_of_presence[full_name] += pers_stat[1]
                else:
                    percent_of_presence[full_name] = pers_stat[1]

            for person, value in percent_of_presence.items():
                percent_of_presence[person] = (value / len(stats)) * 100

        return percent_of_presence

    @staticmethod
    def already_checked(date):
        checked_day = SqlRequest.sql_request('SELECT * FROM attendance WHERE "date"=="{}" LIMIT 1'.format(date))
        if checked_day:
            return True
        return False

    @staticmethod
    def get_attendance_day(date):
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
        SqlRequest.sql_request('UPDATE attendance SET status="{}" WHERE student_id="{}" AND \
        "date"="{}"'.format(value, id, _date))

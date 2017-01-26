class Attendance:
    list_of_attendance = [] # [obcj]  : obcj " ", {" ": 0/1}

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


    def add(self):
        """
        Add Attendance objc to list_of_attendance.
        """
        Attendance.list_of_attendance.append(self)

    @staticmethod
    def present_statistic():
        """
        Calculate overall present for each student.
        :return (dict): SAMPLE DICT {'patrycja': '100', 'przemek': '50'}
        """
        percent_of_presence = {}

        for day_attendance in Attendance.list_of_attendance:
            for student, present in day_attendance.student_presence.items():
                if student in percent_of_presence.keys():
                    percent_of_presence[student] += int(present)
                else:
                    percent_of_presence[student] = int(present)
        for student, attendance in percent_of_presence.items():
            percent_of_presence[student] = str(int((attendance/len(Attendance.list_of_attendance))*100))
        return percent_of_presence

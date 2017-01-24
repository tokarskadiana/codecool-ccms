class Attendance:
    list_of_attendance = [] # {date:{},date:{}}

    def __init__(self, date, presence):
        self.date = date
        self.student_presence = presence

    def list_attendance(self):
        """

        :return:
        """
        pass

    def add(self):
        """

        :return:
        """
        self.date_presence = {self.date:self.student_presence}
        Attendance.list_of_attendance.append(self.date_presence)

    @staticmethod
    def present_statistic(list):
        """

        :param data:
        :return: SAMPLE DICT {'patrycja': '100', 'przemek': '50'}
        """
        percent_of_presence = {}

        for attendance_list, students in list.items():
                for student, attendance in students.items():
                    if student in percent_of_presence.keys():
                        print(student, attendance)
                        percent_of_presence[student] += students[student]
                    else:
                        percent_of_presence[student] = students[student]

        for student, attendance in percent_of_presence.items():
            percent_of_presence[student] = str(int((attendance/len(list))*100))

        return percent_of_presence

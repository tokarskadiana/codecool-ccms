class Attendance:
    list_of_attendance = []

    def __init__(self, date, presence):
        self.date = date
        self.student_presence = presence

    def list_attendance(self):
        pass

    def add(self):
        self.date_presence = [self.date, self.student_presence]
        Attendance.list_of_attendance.append(self.date_presence)

    @staticmethod
    def present_statistic(data):
        """

        :param data:
        :return: SAMPLE DICT {'patrycja': '100', 'przemek': '50'}
        """
        percent_of_presence = {}

        for attendance_list in data:
            for attendance in attendance_list[1::2]:
                for student in attendance:
                    if student in percent_of_presence.keys():
                        percent_of_presence[student] += attendance[student]
                    else:
                        percent_of_presence[student] = attendance[student]
        for student, attendance in percent_of_presence.items():
            percent_of_presence[student] = str(int((attendance/len(data))*100))
        return percent_of_presence


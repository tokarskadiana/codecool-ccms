from user import User


class Student(User):
    list_of_students = []

    @staticmethod
    def add_student(password, first_name, last_name, telephone='', mail=''):
        student = Student(password, first_name, last_name, telephone, mail)
        Student.list_of_students.append(student)

    def edit_student(self, **kwargs):
        for key, value in kwargs:
            if key:
                if key in self.__dict__.keys():
                    self.__dict__[key] = value

    @staticmethod
    def delete_student(username):
        for student in Student.list_of_students:
            if student.username == username:
                Student.list_of_students.remove(student)

    @classmethod
    def list_student(self):
        return Student.list_of_students

    def view_details(self):
        list_det = []
        list_det.append(self.username, self.first_name, self.last_name, self.telephone, self.mail)
        return list_det

from user import User

class Student(User):
    list_of_students = []

    @staticmethod
    def add_student(username, password, first_name, last_name, telephone='', mail=''):
        username = '{}.{}'.format(first_name, last_name)
        student = Student(username, password, first_name, last_name, telephone, mail)
        Student.list_of_students.append(student)

    def edit_student(self):
        pass

    @staticmethod
    def delete_student(username):
        for student in Student.list_of_students:
            if student.username == username:
                Student.list_of_students.remove(student)

    def list_student(self):
        return Student.list_of_students

    def view_details(self):
        pass

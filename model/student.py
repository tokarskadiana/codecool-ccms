from model.user import User


class Student(User):
    list_of_students = []

    @staticmethod
    def add_student(password, first_name, last_name, telephone='', mail=''):
        """
        Initialize Assignment object.
        :param password (str): password
        :param first_name (str): first name
        :param last_name (str): last name
        :param telephone (str): telephone
        :param mail (str): mail
        """
        student = Student(password, first_name, last_name, telephone, mail)
        Student.list_of_students.append(student)

    def edit_student(self, **kwargs):
        """
        Edit student attr.
        :param kwargs: name of attr and value of it
        """
        for key, value in kwargs.items():
            if key:
                if key in self.__dict__.keys():
                    self.__dict__[key] = value

    @staticmethod
    def delete_student(username):
        """
        Remove student from list_of_students by given username.
        :param username (str): value of username attr
        """
        for student in Student.list_of_students:
            if student.username == username:
                Student.list_of_students.remove(student)

    @staticmethod
    def list_student():
        """
        Returns static variable list_of_students.
        :return (list): list of students
        """
        return Student.list_of_students

    def view_details(self):
        """
        Returns list of personal data.
        :return (list): list of personal data
        """
        list_det = [self.first_name, self.last_name, self.username, self.telephone, self.mail]
        return list_det

    def get_username(self):
        return self.username

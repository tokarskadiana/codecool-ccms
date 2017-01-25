


class User:

    def __init__(self, password, first_name, last_name, telephone, mail):
        self.username = '{}.{}'.format(first_name, last_name)
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.telephone = telephone
        self.mail = mail


    @classmethod
    def log_in(cls, username=None, password=None):
        from mentor import Mentor
        from student import Student

        users = [Mentor.mentors_list,
                 Student.list_of_students]

        for list_of_users in users:
            for person in list_of_users:
                if username == person.username:
                    if password == person.password:
                        return person
        return False

    @classmethod
    def sign_out(cls):
        # save data to file
        cls.log_in()


class Employee(User):

    @classmethod
    def add_employee(cls):
        e = Employee(password, first_name, last_name, telephone, mail)



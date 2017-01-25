from student import *
from mentor import Mentor
from student import Student

class User:
    def __init__(self, password, first_name, last_name, telephone, mail):
        self.username = '{}.{}'.format(first_name, last_name)

        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.telephone = telephone
        self.mail = mail



    def log_in(self, username, password):
        users = [Mentor.mentors_list,
                 Student.list_of_students]

        if username in users:




        pass

    def sign_out(self):
        pass


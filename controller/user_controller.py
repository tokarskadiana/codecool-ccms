from model.mentor import Mentor
from model.student import Student
from model.manager import Manager
from model.employee import Employee
from controller.database_controller import DatabaseController
from model.sqlRequest import SqlRequest
from model.user import User
import sys


class UserController:

    def __init__(self, user):
        '''
        Constructor of user controller.

        Arguments:user object
        '''
        self.user = user

    @classmethod
    def log_in(cls, username, password):
        """
        This class method checking if username and password are correct for user
        :param username: (str) store user name
        :param password: (str) store user password
        :return: user object
        """
        request = 'SELECT password, first_name, last_name, telephone, mail, position FROM employee WHERE username="{}" AND password="{}"'.format(
            username, password)

        output = SqlRequest.sql_request(request)
        print(output)

        if output:
            if output[0][5] == 'mentor':
                return Mentor(output[0][1], output[0][1], output[0][2], output[0][3], output[0][4])
            elif output[0][5] == 'manager':
                return Manager(output[0][0], output[0][1], output[0][2], output[0][3], output[0][4])
            elif output[0][5] == 'employee':
                return Employee(output[0][0], output[0][1], output[0][2], output[0][3], output[0][4])

        request_s = 'SELECT password, first_name, last_name, telephone, mail FROM student WHERE password="{}" AND username="{}"' \
            .format(password, username)
        output_s = SqlRequest.sql_request(request_s)
        if output_s:
            return Student(output[0][0], output[0][1], output[0][2], output[0][3], output[0][4])
        return None

    @classmethod
    def sign_out(cls):
        """
        Saving data to file and exit the program
        """
        sys.exit()

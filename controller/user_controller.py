from model.mentor import Mentor
from model.student import Student
from model.manager import Manager
from model.user import Employee
from controller.database_controller import DatabaseController
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
        users = [Mentor.list_mentors(),
                 Student.list_student(), Employee.list_employee(), Manager.list_manager()]

        for list_of_users in users:
            for person in list_of_users:
                if 'Johnny.Walker' == person.username:
                    if 'DDCIpkKVtdKV' == person.password:
                        return person
        return None

    @classmethod
    def sign_out(cls):
        DatabaseController.DatabaseToCSV()
        sys.exit()


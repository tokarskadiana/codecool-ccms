from controller.employee_controller import EmployeeController
from model.mentor import Mentor
from model.user import Employee

class MenagerController(EmployeeController):

    def list_mentor(self):
        mentor_list = []
        for index, mentor in enumerate(Mentor.list_mentors()):
            mentor_list.append('{}. {}'.format(index + 1, mentor))
        return mentor_list

    def view_mentors_details(self, username):
        for person in mentor.Mentor.mentors_list:
            if person.username == username:
                mentor.Mentor.view_mentor_details(person, person.username)

    def edit_mentor(self, username, parameter, new_value):
        for mentor in Mentor.list_mentors():
            if mentor.get_username() == username:
                mentor.edit_mentor(parameter=new_value)
                return '{} was edited.'.format(mentor)
    def add_mentor(self, first_name, last_name, password):
        Mentor.add_mentor(password, first_name, last_name)
        return 'Mentor was added.'

    def add_assistant(self, first_name, last_name, password):
        Employee.create(first_name, last_name, password)
        return 'Assistant was added.'
    # +remove_mentor(Mentor_obj:obj):str
    @staticmethod
    def remove_mentor(username):
        for mentor in Mentor.list_mentors():
            if mentor.get_username() == username:
                mentor.delete_mentor(username)
                return '{} was deleted'.format(mentor)

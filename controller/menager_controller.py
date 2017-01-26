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

    @staticmethod
    def manager_session(user):
        session = MenagerController(user)
        while True:
            view.menager_menu()
            option = input('\nChoose the option:')
            if option == '1':
                list_mentors = session.list_mentor()
                view.print_mentors_list(list_mentors)
            elif option == '2':
                first_name = input('Enter first name:')
                last_name = input('Enter last name:')
                password = input('Enter password:')
                print(session.add_mentor(first_name, last_name, password))
            elif option == '3':
                first_name = input('Enter first name:')
                last_name = input('Enter last name:')
                password = input('Enter password:')
                print(session.add_assistant(first_name, last_name, password))
            elif option == '4':
                view.edit_menu()
                mentor = input('Enter user_name:')
                parameter = input('Enter what you want to edit:')
                new_value = input('Enter new value:')
                print(session.edit_mentor(mentor, parameter, new_value))
            elif option == '5':
                mentor = input('Enter mentors username you want to delete:')
                print(session.remove_mentor(mentor))
            elif option == '0':
                UserController.sign_out()
                return
            else:
                print('Enter valid option.')
                continue

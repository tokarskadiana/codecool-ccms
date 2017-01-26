from controller.employee_controller import EmployeeController
from controller.user_controller import UserController
from model.mentor import Mentor
from model.user import Employee
import view


class MenagerController(EmployeeController):

    def list_mentor(self):
        mentor_list = []
        for index, mentor in enumerate(Mentor.list_mentors()):
            mentor_list.append([index] + str(mentor).split())
        return mentor_list

    def view_mentors_details(self, username):
        for mentor in Mentor.list_mentors():
            if mentor.username == username:
                return mentor.view_mentor_details()

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
            view.View.menager_menu()
            option = input('\nChoose the option:')
            if option == '1':
                view.View.clear()
                list_mentors = session.list_mentor()
                view.View.print_mentors_list(list_mentors)
                mentor = input('\nEnter mentor username to see details or x to get back:')
                if mentor.lower() == 'x':
                    pass
                else:
                    view.View.clear()
                    view.View.show_user_details(session.view_mentors_details(mentor))
                    back = input('\nEnter some key to get back:')
            elif option == '2':
                view.View.clear()
                first_name = input('Enter first name:')
                last_name = input('Enter last name:')
                password = input('Enter password:')
                print(session.add_mentor(first_name, last_name, password))
                back = input('\nEnter some key to get back:')
            elif option == '3':
                view.View.clear()
                first_name = input('Enter first name:')
                last_name = input('Enter last name:')
                password = input('Enter password:')
                print(session.add_assistant(first_name, last_name, password))
                back = input('\nEnter some key to get back:')
            elif option == '4':
                view.View.clear()
                list_mentors = session.list_mentor()
                view.View.print_mentors_list(list_mentors)
                view.View.edit_menu()
                mentor = input('Enter user_name:')
                parameter = input('Enter what you want to edit:')
                new_value = input('Enter new value:')
                print(session.edit_mentor(mentor, parameter, new_value))
                back = input('\nEnter some key to get back:')
            elif option == '5':
                view.View.clear()
                list_mentors = session.list_mentor()
                view.View.print_mentors_list(list_mentors)
                mentor = input('Enter mentors username you want to delete:')
                print(session.remove_mentor(mentor))
                back = input('\nEnter some key to get back:')
            elif option == '0':
                UserController.sign_out()
                return
            else:
                print('Enter valid option.')
                continue

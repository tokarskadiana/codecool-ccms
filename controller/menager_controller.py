from controller.employee_controller import EmployeeController
from controller.user_controller import UserController
from model.mentor import Mentor
from model.user import Employee
import view

class MenagerController(EmployeeController):
    def list_mentor(self):
        """
        Returns list of mentors objc.
        :return (list): list of mentors objc
        """
        mentor_list = []
        for index, mentor in enumerate(Mentor.list_mentors()):
            mentor_list.append('{}. {}'.format(index + 1, mentor))
        return mentor_list

    def view_mentors_details(self, username):
        """
        Returns details of student objc by given username.
        :param username (str): username of objc
        :return (list): list of details
        """
        for person in mentor.Mentor.mentors_list:
            if person.username == username:
                mentor.Mentor.view_mentor_details(person, person.username)

    def edit_mentor(self, username, parameter, new_value):
        """
        Edit attr of mentor objc by given username.
        :param username (str): mentor username
        :param parameter (str): name of attr
        :param new_value (str): new value of attr
        :return (str): returns message
        """
        for mentor in Mentor.list_mentors():
            if mentor.get_username() == username:
                mentor.edit_mentor(parameter=new_value)
                return '{} was edited.'.format(mentor)

    def add_mentor(self, first_name, last_name, password):
        """
        Create mentor and add to mentor list in class.
        :param first_name (str): first name of mentor
        :param last_name (str): last name of mentor
        :param password (str): password of mentor
        :return (str): returns message
        """
        Mentor.add_mentor(password, first_name, last_name)
        return 'Mentor was added.'

    def add_assistant(self, first_name, last_name, password):
        """
        Add assistant to list of employee.
        :param first_name (str): first name of assistant
        :param last_name (str): last name of assistant
        :param password (str): password of assistant
        :return (str): returns message
        """
        Employee.create(first_name, last_name, password)
        return 'Assistant was added.'

    @staticmethod
    def remove_mentor(username):
        """
        Remove mentor from mentor list.
        :param username: returns
        :return: returns message
        """
        for mentor in Mentor.list_mentors():
            if mentor.get_username() == username:
                mentor.delete_mentor(username)
                return '{} was deleted'.format(mentor)

    @staticmethod
    def manager_session(user):
        """
        Start manager menu.
        :param user (objc): mentor objc
        """
        session = MenagerController(user)
        while True:
            view.View.menager_menu()
            option = input('\nChoose the option:')
            if option == '1':
                list_mentors = session.list_mentor()
                view.View.print_mentors_list(list_mentors)
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
                view.View.edit_menu()
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

from controller.employee_controller import EmployeeController
from controller.user_controller import UserController
from model.mentor import Mentor
from model.employee import Employee
import view


class MenagerController(EmployeeController):
    def list_mentor(self):
        """
        Returns list of mentors objc.
        :return (list): list of mentors objc
        """
        mentor_list = []
        for index, mentor in enumerate(Mentor.list_mentors()):
            mentor_list.append([index] + str(mentor).split())
        return mentor_list

    def view_mentors_details(self, mentor_index):
        """
        Returns details of student objc by given username.
        :param username (str): username of objc
        :return (list): list of details
        """
        return Mentor.list_mentors()[mentor_index].view_mentor_details()

    def edit_mentor(self, mentor_index, parameter, new_value):
        """
        Edit attr of mentor objc by given username.
        :param username (str): mentor username
        :param parameter (str): name of attr
        :param new_value (str): new value of attr
        :return (str): returns message
        """
        mentor = Mentor.list_mentors()[mentor_index]
        if parameter == 'mail':
            if mentor.edit_mentor(mail=new_value):
                return '{} was edited.'.format(mentor.get_username())
        if parameter == 'telephone':
            if mentor.edit_mentor(telephone=new_value):
                return '{} was edited.'.format(mentor.get_username())
        return 'You dont edit mentor. Try again.'

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
    def remove_mentor(mentor_index):
        """
        Remove mentor from mentor list.
        :param username: returns
        :return: returns message
        """
        mentor = Mentor.list_mentors()[mentor_index]
        if mentor.delete_mentor(mentor):
            return 'Mentor was deleted'
        return 'Mentor was\'t deleted'

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
                view.View.clear()
                list_mentors = session.list_mentor()
                view.View.print_user_list(list_mentors)
                if list_mentors:
                    mentor_index = input(
                        '\nFor more details give the number of person or else to get back: ')
                    try:
                        mentor_index = int(mentor_index)
                        if mentor_index in range(len(list_mentors)):
                            view.View.clear()
                            view.View.show_user_details(
                                session.view_mentors_details(mentor_index))
                            input('\nPress any key to back:')
                    except ValueError:
                        continue
                else:
                    print('There no any employeed mentor')
                    input('\nPress any key to back:')
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
                view.View.print_user_list(list_mentors)
                view.View.edit_menu()
                mentor_index = input('Enter mentor index:')
                try:
                    mentor_index = int(mentor_index)
                    if mentor_index in range(len(list_mentors)):
                        parameter = input('Enter what you want to edit:')
                        new_value = input('Enter new value:')
                        print(session.edit_mentor(
                            mentor_index, parameter, new_value))
                        back = input('\nEnter some key to get back:')
                    else:
                        continue
                except ValueError:
                    continue
            elif option == '5':
                view.View.clear()
                list_mentors = session.list_mentor()
                view.View.print_user_list(list_mentors)
                if list_mentors:
                    mentor_index = input(
                        'Enter mentor index which you want to remove:')
                try:
                    mentor_index = int(mentor_index)
                    if mentor_index in range(len(list_mentors)):
                        print(session.remove_mentor(mentor_index))
                        back = input('\nEnter some key to get back:')
                    else:
                        continue
                except ValueError:
                    continue
            elif option == '0':
                UserController.sign_out()
                return
            else:
                continue

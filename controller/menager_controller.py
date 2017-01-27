from controller.employee_controller import EmployeeController
from controller.user_controller import UserController
from model.mentor import Mentor
from model.user import Employee
import view


class MenagerController(EmployeeController):

    def list_mentor(self):
        """

        :return:
        """
        mentor_list = []
        for index, mentor in enumerate(Mentor.list_mentors()):
            mentor_list.append([index] + str(mentor).split())
        return mentor_list

    def view_mentors_details(self, mentor_index):
        return Mentor.list_mentors()[mentor_index].view_mentor_details()

    def edit_mentor(self, mentor_index, parameter, new_value):
        mentor = Mentor.list_mentors()[mentor_index]
        if parameter == 'mail':
            if mentor.edit_mentor(mail=new_value):
                return '{} was edited.'.format(mentor.get_username())
        if parameter == 'telephone':
            if mentor.edit_mentor(telephone=new_value):
                return '{} was edited.'.format(mentor.get_username())
        return 'You dont edit mentor. Try again.'

    def add_mentor(self, first_name, last_name, password):
        Mentor.add_mentor(password, first_name, last_name)
        return 'Mentor was added.'

    def add_assistant(self, first_name, last_name, password):
        Employee.create(first_name, last_name, password)
        return 'Assistant was added.'

    @staticmethod
    def remove_mentor(mentor_index):
        mentor = Mentor.list_mentors()[mentor_index]
        if mentor.delete_mentor(mentor):
            return 'Mentor was deleted'
        return 'Mentor was\'t deleted'

    @staticmethod
    def manager_session(user):
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
                        else:
                            print('Wrong number')
                            continue
                    except ValueError:
                        print('Enter a number')
                else:
                    print('There no any empoyed mentor')
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
                        print('Wrong number')
                        continue
                except ValueError:
                    print('Enter a number')
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
                        print('Wrong number')
                        continue
                except ValueError:
                    print('Enter a number')
            elif option == '0':
                UserController.sign_out()
                return
            else:
                print('Enter valid option.')
                continue

from tabulate import tabulate
from model.assignment import Assignment
import sys
import os
from controller.mentor_controller import MentorController


class View:

    @staticmethod
    def main_menu():
        View.clear()
        print('Welcome in CodeCool Management System')
        print('\nTo EXIT program press "0"\n')
        username = input('Enter your username:')
        if username == '0':
            sys.exit()
        password = input('Enter your password:')
        return username, password

    @staticmethod
    def student_menu():
        View.clear()
        print('''
        -----------MENU-----------
        1. List assignments
        2. Check grades
        3. Submit assignment
        0. Exit
        ''')

    @staticmethod
    def mentor_menu():
        View.clear()
        print('''
        -----------MENU-----------
        1. Check attendance
        2. Add assignment
        3. Grade assignment
        4. Add student
        5. Edit student
        6. Delete student
        7. View presence statistics
        0. Exit
        ''')

    @staticmethod
    def menager_menu():
        View.clear()
        print('''
        -----------MENU-----------
        1. List mentors
        2. Add mentor
        3. Add assistant
        4. Edit mentor
        5. Delete mentor
        0. Exit
        ''')

    @staticmethod
    def employee_menu():
        View.clear()
        print('''
        -----------MENU-----------
        1. List student
        0. Exit
        ''')

    @staticmethod
    def show_user_details(user):
        if user:
            headers = ['First name', 'Last name', 'User name', 'Phone Number', 'Mail']
            print(tabulate([list(user)], headers, tablefmt="fancy_grid"))
        else:
            print('There is ampty.')

    @staticmethod
    def print_assignment_grades(assignment_grades):
        if assignment_grades:
            headers = ['Assiment', 'Grade']
            print(tabulate(assignment_grades, headers,
                           tablefmt="fancy_grid", stralign="center"))
        else:
            print('There is ampty.')

    @staticmethod
    def print_assignments_list(assignments_list):
        if assignments_list:
            headers = ['Title', 'Due_date', 'description']
            print (tabulate(assignments_list, headers, tablefmt="fancy_grid"))
        else:
            print('There is ampty.')

    @staticmethod
    def print_user_list(user_list):
        if user_list:
            headers = ['Index', 'First name', 'Last name', 'User name']
            print (tabulate(user_list, headers, tablefmt="fancy_grid"))
        else:
            print('There is ampty.')

    @staticmethod
    def display_static_present(list_stat):
        if list_stat:
            for key, value in list_stat.items():
                print('{} {}'.format(key, value))
        else:
            print('No statistics yet.')

    @staticmethod
    def edit_menu():
        print('''
        You can edit following parameters:
            1. telephone
            2. mail
        ''')

    @staticmethod
    def print_two_demention_list(printed_list):
        for index, sub_list in enumerate(printed_list):
            print('{}. {}'.format(index, ' - '.join(sub_list)))

    @staticmethod
    def clear():
        """
        Clears screen for better display
        """
        os.system('cls' if os.name == 'nt' else 'clear')

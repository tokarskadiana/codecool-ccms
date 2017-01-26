from model.user import User
from model.user import Employee
from model.student import Student
from model.mentor import Mentor
from model.manager import Manager
from model.assignment import Assignment
from controller.student_controller import StudentController
from controller.user_controller import UserController
from controller.mentor_controller import MentorController
from controller.menager_controller import MenagerController
from controller.employee_controller import EmployeeController
from view import View as view





def mentor_session(user):
    session = MentorController(user)
    while True:
        view.mentor_menu()
        option = input('\nChoose the option:')
        if option == '1':
            pass
        elif option == '2':
            pass
        elif option == '3':
            pass
        elif option == '4':
            pass
        elif option == '5':
            pass
        elif option == '6':
            pass
        elif option == '7':
            pass
        elif option == '0':
            UserController.sign_out()
            return
        else:
            print('Enter valid option.')
            continue


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


def employee_session(user):
    session = EmployeeController(user)
    while True:
        view.employee_menu()
        option = input('\nChoose the option:')
        if option == '1':
            pass
        elif option == '0':
            UserController.sign_out()
            return
        else:
            print('Enter valid option.')
            continue


def date_base():
    Employee.create('dupa', 'Kati', 'K')
    Mentor.add_mentor('dupa', 'Marcin', 'Foo')
    Student.add_student('dupa', 'diana', 'd')
    Manager.add_manager('dupa', 'Jurek', 'K')
    Assignment.create('Dupa', 'dacv')

def main():
    date_base()
    log_in_input = view.main_menu()
    username = log_in_input[0]
    password = log_in_input[1]
    user = UserController.log_in(username, password)
    if type(user) == Student:
        StudentController.student_session(user)
    elif type(user) == Mentor:
        mentor_session(user)
    elif type(user) == Manager:
        manager_session(user)
    elif type(user) == Employee:
        employee_session(user)
    else:
        main()

main()

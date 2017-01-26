from model.user import User
from model.user import Employee
from model.student import Student
from model.mentor import Mentor
from model.manager import Manager
from model.attendance import Attendance
from controller.student_controller import StudentController
from controller.user_controller import UserController
from controller.mentor_controller import MentorController
from controller.menager_controller import MenagerController
from controller.employee_controller import EmployeeController
from controller.database_controller import DatabaseController
from view import View as view


def student_session(user):
    session = StudentController(user)
    while True:
        view.student_menu()
        option = input('\nChoose the option:')
        if option == '1':

        elif option == '2':
            pass
        elif option == '0':
            UserController.sign_out()
            return
        else:
            print('Enter valid option.')
            continue


def mentor_session(user):
    session = MentorController(user)
    while True:
        view.mentor_menu()
        option = input('\nChoose the option:')
        if option == '1':
            day = input('write day "day.month.year"')
            MentorController.check_attendence(day)

        elif option == '2':
            title = input('title: ')
            description = input('description')
            due_date = input('due_date')
            MentorController.add_assiment(title, description, due_date)

        elif option == '3':
            pass

        elif option == '4':


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
            pass
        elif option == '2':
            pass
        elif option == '3':
            pass
        elif option == '4':
            pass
        elif option == '5':
            pass
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
            student_list = session.list_students()
            view.show_full_name(student_list)
            user_index = int(input('For more details give the number of person: '))
            if user_index -1 > len(student_list):
                    raise ValueError
            view.show_details(student_list[user_index -1])
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

# X0ChACq,Wanda,Ward,86-(541)543-7895,wward0@utexas.edu


def main():
    DatabaseController.DatabaseFromCSV()

    log_in_input = view.main_menu()
    username = log_in_input[0]
    password = log_in_input[1]
    user = UserController.log_in(username, password)
    if type(user) == Student:
        student_session(user)
    elif type(user) == Mentor:
        mentor_session(user)
    elif type(user) == Manager:
        manager_session(user)
    elif type(user) == Employee:
        employee_session(user)
    else:
        print(type(user))
        main()

main()

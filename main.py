from model.user import User
from model.user import Employee
from model.student import Student
from model.mentor import Mentor
from model.manager import Manager
from model.assignment import Assignment
from model.attendance import Attendance
from controller.student_controller import StudentController
from controller.user_controller import UserController
from controller.mentor_controller import MentorController
from controller.menager_controller import MenagerController
from controller.employee_controller import EmployeeController
from controller.database_controller import DatabaseController
from view import View as view


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
            view.display_assigments()
            number = input('write number of ass: ')
            view.display_ass(number)



        elif option == '4':
            first_name = input('first name: ')
            last_name = input('last name: ')
            password = input('password: ')
            MentorController.add_student(first_name, last_name, password)

        elif option == '5':
            view.display_students(Student.list_of_students)
            number = input('number of student: ')
            telephone = input('telephone: ')
            mail = input('mail: ')
            MentorController.edit_student(number, telephone, mail)

        elif option == '6':
            view.display_students(Student.list_of_students)
            number = input('number of student: ')
            MentorController.remove_student(number)
        elif option == '7':
            view.display_static_present(MentorController.view_presence_statistic())
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


def main():
    DatabaseController.DatabaseFromCSV()

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
        EmployeeController.employee_session(user)
    else:
        print(type(user))
        main()

main()

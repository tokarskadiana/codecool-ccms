from model.user import User
from controller.student_controller import StudentController
from view import View as view


def student_session(user):
    session = StudentController(user)
    while True:
        view.student_menu()
        option = input('\nChoose the option:')
        if option == '1':
            pass
        elif option == '2':
            pass
        elif option == '0':
            User.sing_out()
            main()
        else:
            print('Enter valid option.')
            continue


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
            User.sing_out()
            main()
        else:
            print('Enter valid option.')
            continue

def menager_session(user):
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
            User.sing_out()
            main()
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
            User.sing_out()
            main()
        else:
            print('Enter valid option.')
            continue

def main():
    log_in_input = view.main_menu()
    username = log_in_input[0]
    password = log_in_input[1]
    user = User.log_in(username, password)
    if type(user) == Student:
        student_session(user)
    elif type(user) == Mentor:
        mentor_session(user)
    elif type(user) == Menager:
        menager_session(user)
    elif type(user) == Employee:
        employee_session(user)
    else:
        main()

main()

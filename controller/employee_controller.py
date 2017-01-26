from controller.user_controller import UserController
from model.student import Student
from view import View as view


class EmployeeController(UserController):

    @staticmethod
    def list_students():
        list_of_details = []
        for student in Student.list_student():
            list_of_details.append(student.view_details())

        return list_of_details

    @staticmethod
    def employee_session(user):
        session = EmployeeController(user)
        while True:
            view.employee_menu()
            option = input('\nChoose the option:')
            if option == '1':
                student_list = session.list_students()
                view.show_full_name(student_list)
                user_index = input('For more details give the number of person: ')
                try:
                    user_index = int(user_index)
                    if user_index -1 > len(student_list):
                        print('Wrong number')
                        continue
                    view.show_details(student_list[user_index -1])
                except ValueError:
                    print('Wrong number')

            elif option == '0':
                UserController.sign_out()
                return
            else:
                print('Enter valid option.')
                continue

from controller.user_controller import UserController
from model.student import Student
import view


class EmployeeController(UserController):

    def list_students(self):
        """
        Returns list of students.
        :return (list): list of students objc
        """
        list_student = []
        for index, student in enumerate(Student.list_student()):
            list_student.append([index]+str(student).split())
        return list_student

    def view_details(self, stud_index):
        for index, student in enumerate(Student.list_student()):
            if index == stud_index:
                return student.get_details()

    @staticmethod
    def employee_session(user):
        """
        Start employee menu.
        :param user (objc): employee objc
        """
        session = EmployeeController(user)
        while True:
            view.View.employee_menu()
            option = input('\nChoose the option:')
            if option == '1':
                view.View.clear()
                student_list = session.list_students()
                view.View.print_user_list(student_list)
                user_index = input('\nFor more details give the number of person or else to get back: ')
                try:
                    user_index = int(user_index)
                    if user_index in range(len(student_list)):
                        view.View.clear()
                        view.View.show_user_details(session.view_details(user_index))
                        input('\nPress any key to back:')
                    else:
                        print('Wrong number')
                        continue
                except ValueError:
                    print('Enter a number')

            elif option == '0':
                UserController.sign_out()
                return
            else:
                continue

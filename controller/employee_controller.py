from controller.user_controller import UserController
from model.student import Student
import view


class EmployeeController(UserController):

    def list_students(self):
        """
        Create list of student with detail data
        Returns list of students.
        :return (list): list of students objc
        """
        list_student = []
        if Student.list_student():
            for index, student in enumerate(Student.list_student()):
                list_student.append([index]+str(student).split())
        return list_student

    # def view_details(self, stud_index):
    #     for index, student in enumerate(Student.list_student()):
    #         if index == stud_index:
    #             return student.get_details()

    @staticmethod
    def employee_session(user):
        """
        Run employee menu and session
        :param user (objc): employee objc
        """
        session = EmployeeController(user)
        while True:
            view.View.employee_menu()
            option = input('\nChoose the option:')
            if option == '1':
                view.View.clear()
                view.View.show_students_name(Student.student_name())
                studentid = input('\nFor more details give the ID of person or else to get back: ')
                view.View.print_user_list(Student.list_for_employee(studentid))


                input('\nPress any key to back:')

            elif option == '0':
                UserController.sign_out()
            else:
                continue

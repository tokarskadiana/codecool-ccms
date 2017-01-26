from model import student
from model import attendance
from model.assignment import Assignment
from controller.employee_controller import EmployeeController
import view
from model.student import Student
from  .user_controller import UserController


class MentorController(EmployeeController):

    @staticmethod
    def add_assiment(title, description, due_date):
        Assignment.create(title, description, due_date)

    def grade_assignment(self, assiment_title, student_username, grade):
        for assiment in Assignment.get_list():
            if assiment.get_title() == assiment_title:
                assiment.grade_assigment(student_username, grade)
                return ('You grade assigment.')

    @staticmethod
    def check_attendence(day):
        atta = attendance.Attendance(day, {})
        for person in student.Student.list_of_students:
            print('{} {}'.format(person.first_name, person.last_name))
            ask = input('0 or 1')
            print('{} {}'.format(person.first_name, person.last_name))
            atta.check_attendance(person.username, int(ask))

    @staticmethod
    def add_student(first_name, last_name, password):
        student.Student.add_student(password, first_name, last_name)

    # +edit_student(Student_obj: obj, options_to_change: ** kwargs)
    @staticmethod
    def edit_student(number, telep, mai):
        for index, stu in enumerate(student.Student.list_of_students):
            if str(index) == number:
                stu.edit_student(telephone=telep, mail=mai)

    # +remove_student(Stud_obj:obj):str
    @staticmethod
    def remove_student(number):
        for index, stu in enumerate(student.Student.list_of_students):
            if str(index) == number:
                student.Student.delete_student(stu.username)

    # view_presence_statistic(days number:int);str
    @staticmethod
    def view_presence_statistic():
        return attendance.Attendance.present_statistic()

    @staticmethod
    def display_assignment(number):
        for index, ass in enumerate(Assignment.list_assignment):
            if str(index) == number:
                return ass.view_details()

    @staticmethod
    def mentor_session(user):
        session = MentorController(user)
        while True:
            view.View.mentor_menu()
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
                view.View.display_assigments()
                number = input('write number of ass: ')
                view.View.display_ass(number)
                title = input('title: ')
                u_name = input('username')
                grade = input('grade')
                print(session.grade_assignment(title, u_name, grade))

            elif option == '4':
                first_name = input('first name: ')
                last_name = input('last name: ')
                password = input('password: ')
                MentorController.add_student(first_name, last_name, password)

            elif option == '5':
                view.View.display_students(student.Student.list_of_students)
                number = input('number of student: ')
                telephone = input('telephone: ')
                mail = input('mail: ')
                MentorController.edit_student(number, telephone, mail)

            elif option == '6':
                view.View.display_students(Student.list_of_students)
                number = input('number of student: ')
                MentorController.remove_student(number)
            elif option == '7':
                view.View.display_static_present(MentorController.view_presence_statistic())
            elif option == '0':
                UserController.sign_out()
                return
            else:
                print('Enter valid option.')
                continue

from model import student
from model import attendance
from model.assignment import Assignment
from controller.employee_controller import EmployeeController
from controller.user_controller import UserController
import view
from model.student import Student
from .user_controller import UserController


class MentorController(EmployeeController):

    @staticmethod
    def add_assiment(title, description, due_date):
        """
        Add assignment object to the list of assignments
        :param title: store of title of assignment object
        :param description: store of description of assignment object
        :param due_date: store of due date of assignment object
        """
        Assignment.create(title, description, due_date)

    def grade_assignment(self, assiment_title, student_username, grade):
        """
        Grade student assignment submission
        :param assiment_title: (str) title of assignment
        :param student_username: (str) student user name
        :param grade: (str) grade
        :return: (str)
        """
        for assiment in Assignment.get_list():
            if assiment.get_title() == assiment_title:
                try:
                    if assiment.grade_assigment(student_username, grade):
                        return 'You grade assigment.'
                except:
                    return 'There is no student with given username'

    @staticmethod
    def check_attendence(day):
        """
        Check presence of students for given day
        :param day: (str) store date of given day
        """
        atta = attendance.Attendance(day, {})
        for person in student.Student.list_of_students:
            print('{} {}'.format(person.first_name, person.last_name))
            while True:
                ask = input('0 or 1')
                if ask == '0' or ask == '1':
                    break
            atta.check_attendance(person.username, ask)
        atta.add()

    @staticmethod
    def add_student(first_name, last_name, password):
        """
        Use student method to create student object
        :param first_name: store of first name of Student object
        :param last_name: store of last name of Student object
        :param password: store of password of Student object
        """
        student.Student.add_student(password, first_name, last_name)

    # +edit_student(Student_obj: obj, options_to_change: ** kwargs)
    @staticmethod
    def edit_student(number, telep, mai):
        """
        Edit student details to change/add phone number and e-mail
        :param number: store of number of Student object on the list
        :param telep: store of phone number of Student object
        :param mai: store of e-mail address of Student object
        """
        for index, stu in enumerate(student.Student.list_of_students):
            if str(index) == number:
                stu.edit_student(telephone=telep, mail=mai)

    # +remove_student(Stud_obj:obj):str
    @staticmethod
    def remove_student(number):
        """
        Remove student form a list of students
        :param number: store of number of Student object on the list
        """
        for index, stu in enumerate(student.Student.list_of_students):
            if str(index) == number:
                student.Student.delete_student(stu.username)

    # view_presence_statistic(days number:int);str
    @staticmethod
    def view_presence_statistic():
        """
        Calculate overall present for each student.
        :return (dict): SAMPLE DICT {'patrycja': '100', 'przemek': '50'}
        """
        return attendance.Attendance.present_statistic()

    @staticmethod
    def display_assignment(number):
        """
        Display assignment of given number form a list
        :param number: store number of assignment
        :return: False or assignment details
        """
        for index, ass in enumerate(Assignment.list_assignment):
            if str(index) == number:
                return ass.view_details()
        return False

    @staticmethod
    def mentor_session(user):
        """
        Run mentor menu session
        :param user: mentor user object
        """
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
                if view.View.display_ass(number):
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

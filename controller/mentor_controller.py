from model import student
from model import attendance
from model import assignment
from controller.employee_controller import EmployeeController


class MentorController(EmployeeController):

    @staticmethod
    def add_assiment(title, description, due_date):
        assignment.Assignment.create(title, description, due_date)

    @staticmethod
    def grade_assignment(assiment_title, student_username, grade):
        for assiment in Assignment.get_list():
            if assiment.get_title() == assiment_title:
                assiment.grade_assigment(student_username, grade)
                return ('You grade assigment.')

    @staticmethod
    def check_attendence(day):
        atta = attendance.Attendance(day, {})
        for person in student.Student.list_of_students:
            ask = input('0 or 1')
            print('{} {}'.format(person.first_name, person.last_name))
            atta.check_attendance(person.username, int(ask))
    # +add_student(first_name, last_name, password): str

    @staticmethod
    def add_student(first_name, last_name, password):
        student.Student.add_student(password, first_name, last_name)

    # +edit_student(Student_obj: obj, options_to_change: ** kwargs)
    @staticmethod
    def edit_student(person, first_name, last_name, telephone, mail):
        student.Student.edit_student(
            person, first_name='', last_name='', telephone='', mail='')

    # +remove_student(Stud_obj:obj):str
    @staticmethod
    def remove_student(person):
        for adept in student.Student.list_of_students:
            if person.username == adept.username:
                student.Student.delete_student(adept.username)

    # view_presence_statistic(days number:int);str
    @staticmethod
    def view_presence_statistic():
        attendance.Attendance.present_statistic()

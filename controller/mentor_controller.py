from model import student
from model import attendance
from model import assignment
from controller.employee_controller import EmployeeController


class MentorController(EmployeeController):

    @staticmethod
    def add_assiment(title, description, due_date):
        assignment.Assignment.create(title, description, due_date)

    @staticmethod
    def grade_assignment(number, student_number, grade):
        ass = assignment.Assignment.return_ass(number)

        ass.grade_assigment()




    @staticmethod
    def check_attendence(day):
        atta = attendance.Attendance(day, {})
        for person in student.Student.list_of_students:
            print('{} {}'.format(person.first_name, person.last_name))
            ask = input('0 or 1')
            atta.check_attendance(person.username, int(ask))
    # +add_student(first_name, last_name, password): str

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
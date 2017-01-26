from controller.user_controller import UserController
from model.student import Student


class EmployeeController(UserController):

    @staticmethod
    def list_students():
        list_of_details = []
        for student in Student.list_student():
            list_of_details.append(student.view_details())

        return list_of_details


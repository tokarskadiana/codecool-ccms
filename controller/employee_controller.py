from user_controller import UserController
from model import student


class EmployeeController(UserController):

    def list_students():
        list_of_details = []
        for person in student.Student.list_of_students:
             list_of_details.append(person.view_details())

    def view_students_details(self, username):
        """

        :param username: username of wanted student
        :return:
        """
        for person in student.Student.list_of_students:
            if  username == person.username:
                list_of_details = person.view_details() #list


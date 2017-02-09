from model.employee import Employee
from model.student import Student
from model.mentor import Mentor
from model.manager import Manager
from view import View
from controller.user_controller import UserController
from controller.database_controller import DatabaseController
from controller.student_controller import StudentController
from controller.mentor_controller import MentorController
from controller.menager_controller import MenagerController
from controller.employee_controller import EmployeeController


def main():
    DatabaseController.createSqlDatabase()
    DatabaseController.sample_data()

    log_in_input = View.main_menu()
    username = log_in_input[0]
    password = log_in_input[1]
    user = UserController.log_in(username, password)

    if type(user) == Student:
        StudentController.student_session(user)
    elif type(user) == Mentor:
        MentorController.mentor_session(user)
    elif type(user) == Manager:
        MenagerController.manager_session(user)
    elif type(user) == Employee:
        EmployeeController.employee_session(user)
    else:
        main()

main()

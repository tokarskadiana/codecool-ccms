from model.user import User
from model.user import Employee
from model.student import Student
from model.mentor import Mentor
from model.manager import Manager
from model.assignment import Assignment
from model.attendance import Attendance
from controller.student_controller import StudentController
from controller.user_controller import UserController
from controller.mentor_controller import MentorController
from controller.menager_controller import MenagerController
from controller.employee_controller import EmployeeController
from controller.database_controller import DatabaseController
from view import View as view



def main():
    DatabaseController.DatabaseFromCSV()

    log_in_input = view.main_menu()
    username = 'Johnny.Walker' #log_in_input[0]
    password = 'DDCIpkKVtdKV' #log_in_input[1]
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

from model.create_data import Database
from model.manager import Manager
from model.mentor import Mentor
from model.user import Employee
from model.student import Student
from model.assignment import Assignment
from model.attendance import Attendance

class DatabaseController:


    @staticmethod
    def DatabaseFromCSV():
        Manager.managers_list = Database.create_user_from_csv('manager1.csv',Manager)
        Mentor.mentors_list = Database.create_user_from_csv('mentors1.csv', Mentor)
        Employee.employee_list = Database.create_user_from_csv('employe1.csv', Employee)
        Student.list_of_students  = Database.create_user_from_csv('students1.csv', Student)
        Assignment.list_assignment = Database.create_assignment_from_csv('assigment1.csv')
        Attendance.list_of_attendance = Database.create_attendance_from_csv('attendance1.csv')

    @staticmethod
    def DatabaseToCSV():
        Database.save_user_to_csv('manager1.csv', Manager.managers_list)
        Database.save_user_to_csv('mentors1.csv', Mentor.mentors_list)
        Database.save_user_to_csv('employe1.csv', Employee.employee_list)
        Database.save_user_to_csv('students1.csv', Student.list_of_students)
        Database.save_assignment_to_csv('assigment1.csv', Assignment.list_assignment)
        Database.save_attendance_to_csv('attendance1.csv', Attendance.list_of_attendance)

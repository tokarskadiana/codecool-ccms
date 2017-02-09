from model.create_data import Database
from model.manager import Manager
from model.mentor import Mentor
from model.employee import Employee
from model.student import Student
from model.assignment import Assignment
from model.attendance import Attendance
import sqlite3


class DatabaseController:
    """Class which control database save/read"""

    @staticmethod
    def DatabaseFromCSV():
        """
        Initialize database for CCmS
        :return:
        """

        Manager.managers_list = Database.create_user_from_csv('manager1.csv', Manager)
        Mentor.mentors_list = Database.create_user_from_csv('mentors1.csv', Mentor)
        Employee.employee_list = Database.create_user_from_csv('employe1.csv', Employee)
        Student.list_of_students = Database.create_user_from_csv('students1.csv', Student)
        Assignment.list_assignment = Database.create_assignment_from_csv('assigment1.csv')
        Attendance.list_of_attendance = Database.create_attendance_from_csv('attendance1.csv')

    @staticmethod
    def createSqlDatabase():
        """

        :return:
        """
        sql_student = Database.readSqlTxt('student.txt')
        sql_assiment = Database.readSqlTxt('assiment.txt')
        sql_checkpoint = Database.readSqlTxt('checkpoint.txt')
        sql_employee = Database.readSqlTxt('employee.txt')
        sql_submition = Database.readSqlTxt('submition.txt')
        sql_attendance = Database.readSqlTxt('attendence.txt')
        sql_team = Database.readSqlTxt('team.txt')
        conn = sqlite3.connect('codecool.sqlite')
        cursor = conn.cursor()
        cursor.execute(sql_student)
        cursor.execute(sql_assiment)
        cursor.execute(sql_attendance)
        cursor.execute(sql_checkpoint)
        cursor.execute(sql_employee)
        cursor.execute(sql_submition)
        cursor.execute(sql_team)
        cursor.close()

    @staticmethod
    def sample_data():
        """

        :return:
        """
        sample_employee = Database.readSQLTxtLines('employee_sample.txt')
        sample_student = Database.readSQLTxtLines('student_sample.txt')
        samples = [sample_employee, sample_student]
        conn = sqlite3.connect('codecool.sqlite')
        cursor = conn.cursor()
        for sample_list in samples:
            for task in sample_list:
                print(task)
                cursor.execute(task)
        conn.commit()
        cursor.close()



    @staticmethod
    def DatabaseToCSV():
        """
        Save database to csv files
        :return:
        """
        Database.save_user_to_csv('manager1.csv', Manager.managers_list)
        Database.save_user_to_csv('mentors1.csv', Mentor.mentors_list)
        Database.save_user_to_csv('employe1.csv', Employee.employee_list)
        Database.save_user_to_csv('students1.csv', Student.list_of_students)
        Database.save_assignment_to_csv(
            'assigment1.csv', Assignment.list_assignment)
        Database.save_attendance_to_csv(
            'attendance1.csv', Attendance.list_of_attendance)


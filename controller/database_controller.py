from model.create_data import Database
from model.manager import Manager
from model.employee import Employee
from model.student import Student
from model.assignment import Assignment
from model.attendance import Attendance
import sqlite3


class DatabaseController:
    """Class which control database save/read"""

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
                cursor.execute(task)
        conn.commit()
        cursor.close()

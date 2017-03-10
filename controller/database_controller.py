from model.create_data import Database
import sqlite3


class DatabaseController:
    """Class which control database save/read"""

    @staticmethod
    def createSqlDatabase():
        """
        Creates tables in database using schemas.
        """
        tables = []
        filenames = ['student.txt', 'assiment.txt', 'employee.txt', 'submition.txt', 'attendence.txt', 'team.txt']
        for filename in filenames:
            tables.append(Database.readSqlTxt(filename))
        conn = sqlite3.connect('codecool.sqlite')
        cursor = conn.cursor()
        for table in tables:
            cursor.execute(table)
        cursor.close()

    @staticmethod
    def sample_data():
        """
        Add seeds to tables.
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

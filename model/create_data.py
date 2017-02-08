from model.user import User
from model.user import Employee
from model.mentor import Mentor
from model.student import Student
from model.manager import Manager
from model.assignment import Assignment
from model.submit import Submition
from model.attendance import Attendance

import csv


class Database(object):
    """
    This class represents Database connection/reading/saving
    """
    default_path = 'data_base/'  # default path to csv folder
    sql_path = 'sql_structure/'
    @classmethod
    def create_user_from_csv(cls, filename, user_type=User):
        """
        Class method  for reading csv file and create list of users objects
        :param filename: file name csv
        :user_type : type of User
        :return: List of Objects
        """
        file = cls.default_path + filename
        object_user_list = []
        with open(file, newline='') as csvfile:
            user_reader = csv.reader(csvfile, delimiter=',')

            for element in user_reader:
                temp_data = user_type(element[0], element[1], element[2], element[3], element[4])

                object_user_list.append(temp_data)

        return object_user_list

    @classmethod
    def readSqlTxt(cls, filename):
        """
        Class method  for reading csv file and create list of users objects
        :param filename: file name csv
        :user_type : type of User
        :return: List of Objects
        """
        file = cls.sql_path + filename
        with open(file, newline='') as fileSql:

            sql_output  = fileSql.read()

        return sql_output

    @classmethod
    def readSQLTxtLines(cls, filename):
        """

        :param filename:
        :return:
        """
        file = cls.sql_path + filename
        with open(file, newline='') as fileSql:

            sql_output  = fileSql.readlines()

        return sql_output



    def __str__(self, *args, **kwargs):
        return super().__str__(*args, **kwargs)

    @classmethod
    def save_user_to_csv(cls, filename, table):
        """
        Class method  for saving user to csv
        :param filename: file name csv
        :table : list of table
        :return: List of Objects
        """

        file = cls.default_path + filename
        with open(file, "w") as file:
            for record in table:
                row = ','.join(cls.user_data(record))
                file.write(row + "\n")

    @staticmethod
    def user_data(row):
        """
        Static method  which takes object and return list of its attributs
        :row - user object
        :return list of attr
        """
        coded = User.encodeBase64(row.password)
        return [coded, row.first_name, row.last_name, row.telephone, row.mail]

    @classmethod
    def create_assignment_from_csv(cls, filename):
        """
        Class method for reading assignment csv
        :param filename:
        :return: List of Objects
        """

        file = cls.default_path + filename
        object_assignment_list = []
        with open(file, newline='') as csvfile:
            assignment_reader = csv.reader(csvfile, delimiter=',')

            for element in assignment_reader:
                temp_data = cls.assignment_data_read(element)
                object_assignment_list.append(temp_data)

        return object_assignment_list

    @classmethod
    def save_assignment_to_csv(cls, filename, table):
        """
        Class method  which save assignment   to csv
        :param filename: file name csv
        :table : list of table
        :return: List of Objects
        """
        file = cls.default_path + filename

        with open(file, "w") as file:
            for record in table:
                row = ','.join(cls.assignment_data_save(record))
                file.write(row + "\n")

    @staticmethod
    def assignment_data_read(row, attr_number=3):

        """
        Convert csv strings to object
        :param row:  line of csv
        :param attr_number:  number of submit list attr
        :return: object
        """
        new_list = row[3:]
        submit_object_list = []
        for i in range(0, len(new_list), attr_number):
            submit_object_list.append(
                Submition(new_list[i], new_list[i + 1], new_list[i + 2]))

        return Assignment(row[0], row[1], row[2], submit_object_list)

    @staticmethod
    def assignment_data_save(row):
        """
        Convert assignment object to list
        :type row: object
        :return list
        """
        attendance_list = row.submit_list

        submit = [row.title, row.description, row.due_date]
        for index, item in enumerate(attendance_list):
            submit.append(item.student_username)
            submit.append(item.content)
            submit.append(item.grade)

        return submit

    @classmethod
    def create_attendance_from_csv(cls, filename):
        """
        Class method for reading Attendance csv
        :param filename:
        :return: List of Objects
        """
        file = cls.default_path + filename
        object_attendance_list = []
        with open(file, newline='') as csvfile:
            attendance_reader = csv.reader(csvfile, delimiter=',')

            for element in attendance_reader:
                temp_data = cls.attendance_data_read(element)
                object_attendance_list.append(temp_data)
                # Attendance.add(temp_data)
        return object_attendance_list

    @staticmethod
    def attendance_data_read(row, attr_number=2):
        """
        Convert attendance csv strings to object
        :param row: list
        :param attr_number: attendance attr
        :return: attendance object
        """
        new_list = row[1:]

        attendance_object_dict = {}
        for i in range(0, len(new_list), attr_number):
            attendance_object_dict[new_list[i]] = new_list[i + 1]

        return Attendance(row[0], attendance_object_dict)

    @classmethod
    def save_attendance_to_csv(cls, filename, table):
        """
        Class method  which save attendance   to csv
        :param filename: file name csv
        :table : list of table
        :return: List of Objects
        """
        file = cls.default_path + filename
        with open(file, "w") as file:
            for record in table:
                row = ','.join(cls.attendance_data_save(record))
                file.write(row + "\n")

    @staticmethod
    def attendance_data_save(row):

        """
        Convert attendance object to list
        :type row: object
        :return list
        """
        attendance_list = row.student_presence

        attendance = [row.date]
        for key, value in attendance_list.items():
            attendance.append(key)
            attendance.append(value)

        return attendance

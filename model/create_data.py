import sqlite3
from model.user import User
from model.employee import Employee
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
    sql_path = 'sql_structure/'

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
            sql_output = fileSql.read()

        return sql_output

    @classmethod
    def readSQLTxtLines(cls, filename):
        """
        Read line by line query from text file.
        :param filename (str): path for text file
        :return: data form text file
        """
        file = cls.sql_path + filename
        with open(file) as fileSql:
            sql_output = fileSql.readlines()

        return sql_output

    def __str__(self, *args, **kwargs):
        return super().__str__(*args, **kwargs)

    @staticmethod
    def user_data(row):
        """
        Static method  which takes object and return list of its attributs
        :row - user object
        :return list of attr
        """
        coded = User.encodeBase64(row.password)
        return [coded, row.first_name, row.last_name, row.telephone, row.mail]

from user import User
# from mentor import Mentor
from student import Student
from assignment import Assignment
from submit import Submition

import csv

class Database(object):

    default_path = '../data_base/'

    @classmethod
    def create_user_from_csv(cls,filename, user_type = User):
        """
        Static method for reading csv file and create list of users objects
        :param filename:
        :return: List of Objects
        """
        count_record = 0
        file = cls.default_path + filename
        object_user_list = []
        with open(file, newline='') as csvfile:

            user_reader = csv.reader(csvfile, delimiter=',')

            for element in user_reader:
                count_record += 1
                temp_data = user_type(element[0], element[1], element[2], element[3], element[4])
                object_user_list.append(temp_data)

        return object_user_list


    @classmethod
    def save_user_to_csv(cls,filename, user_type = User):
        """
        Static method for reading csv file and create list of users objects
        :param filename:
        :return: List of Objects
        """
        count_record = 0
        file = cls.default_path + filename
        object_user_list = []
        with open(file, newline='') as csvfile:

            user_reader = csv.reader(csvfile, delimiter=',')

            for element in user_reader:
                count_record += 1
                temp_data = user_type(element[0], element[1], element[2], element[3], element[4])
                object_user_list.append(temp_data)

        return object_user_list

    @classmethod
    def save_user_to_csv(cls,filename , table):
        """
        Writes list of lists into a csv file.

        Args:
            file_name (str): name of file to write to
            table: list of lists to write to a file

        Returns:
             None
        """
        file = cls.default_path + filename
        with open(file, "w") as file:
            for record in table:
                print(record)
                row = ','.join(cls.user_data(record))
                file.write(row + "\n")

    @classmethod
    def create_assignment_from_csv(cls,filename):
        """
        Static method for reading csv file and create list of users objects
        :param filename:
        :return: List of Objects
        """
        count_record = 0
        file = cls.default_path + filename
        object_assignment_list = []
        with open(file, newline='') as csvfile:

            assignment_reader = csv.reader(csvfile, delimiter=',')

            for element in assignment_reader:
                count_record += 1
                cls.assigment_data_read(element)
                # temp_data = Assignment(element[0], element[1], element[2], element[3], element[4])
                # object_assignment_list.append(temp_data)

        return object_assignment_list

    @staticmethod
    def user_data(row):

        return [row.password,row.first_name,row.last_name,row.telephone,row.mail]

    @staticmethod
    def assigment_data_read(row,attr_number = 3):
        # student_username
        # content
        # grade
        # Structure title, description, due_date, submit_list
        print(row)
        new_list = row[3:]
        submmit_object_list = []
        for i in range(0,len(new_list),attr_number):
            submmit_object_list.append(Submition(new_list[i],new_list[i+1],new_list[i+2]))
        print(submmit_object_list)
        return submmit_object_list




data = Database.create_assignment_from_csv('assigment.csv')
#
# data = Database.save_user_to_csv('students_test.csv',data)
# # print(data[0].__dict__)
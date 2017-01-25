from user import *
import csv

class Database(object):

    # default_path = '../data_base/'

    @classmethod
    def create_user_from_csv(cls,filename):
        """
        Static method for reading csv file and create list of users objects
        :param filename:
        :return: List of Objects
        """
        count_record = 0
        # file = cls.default_path + filename
        object_user_list = []
        with open(filename, newline='') as csvfile:

            user_reader = csv.reader(csvfile, delimiter=',')

            print(user_reader)
            for element in user_reader:
                count_record += 1

                user = User(element[0], element[1], element[2], element[3], element[4])
                object_user_list.append(user)

        return object_user_list

data = Database.create_user_from_csv('../data_base/students.csv')
print(data)
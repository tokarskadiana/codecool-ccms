from model.employee import Employee
from model.sqlRequest import SqlRequest


class Mentor(Employee):
    mentors_list = []

    @classmethod
    def add_mentor(cls, password, first_name, last_name, telephone='', mail='', salary=''):
        """
        Add mentor to mentors list.
        :param password (str): password of mentor
        :param first_name (str):  first name of manager
        :param last_name (str): last name of manager
        :param telephone (str): telephone of mentor
        :param mail (str): mail of mentor
        :param salary (int): salary of mentor
        """
        username = '{}.{}'.format(first_name, last_name)
        SqlRequest.sql_request(
            'INSERT OR IGNORE INTO  employee (first_name,last_name,password,username,position) VALUES ("{}","{}","{}","{}","{}")'.format(
                 first_name, last_name, password, username, 'mentor'))

    def edit_mentor(self, **kwargs):
        """
        Edit attr of mentor objc by given key words.
        :param kwargs (dict): attr of mentor objc and value to change
        :return (dict): all attr of mentor objc
        """
        username = self.username
        for key, value in kwargs.items():
            for dict_key, dict_value in self.__dict__.items():

                if key == dict_key:
                    query = 'UPDATE employee SET "{}"="{}" WHERE position = "mentor" and username = "{}"'.format(key,
                                                                                                                 value,
                                                                                                                 username)
                    # print(query)
                    msg = SqlRequest.sql_request(query)
                    return True
        return False

    def view_mentor_details(self):
        """
        Returns value of attr by given username.
        :param username (str): value of mentor objc
        :return (tuple): tuple of value of attr
        """
        return self.first_name, self.last_name, self.username, self.telephone, self.mail

    @staticmethod
    def delete_mentor(mentor):
        """
        Remove mentor from list of mentors by given username.
        :param username: username of objc
        :return (bool):
        """
        username = mentor.username
        query = 'DELETE FROM employee WHERE position = "mentor" and username = "{}"'.format(username)
        msg = SqlRequest.sql_request(query)
        # print(msg)
        Mentor.mentors_list.remove(mentor)
        if mentor not in Mentor.mentors_list:
            return True
        return False

    @staticmethod
    def add_salary(mentor, salary):
        """
        Remove mentor from list of mentors by given username.
        :param username: username of objc
        :return (bool):
        """
        username = mentor.username
        query = 'UPDATE employee SET salary={} WHERE position = "mentor" and username = "{}"'.format(salary, username)
        msg = SqlRequest.sql_request(query)

    @classmethod
    def list_mentors(cls):
        """
        Returns mentors list.
        :return (list): list of mentors objc
        """
        query = 'SELECT * FROM employee WHERE position = "mentor"'
        mentorSqlList = SqlRequest.sql_request(query)
        mentorObjectList = []
        for element in mentorSqlList:
            mentorObject = cls(element[3], element[1], element[2], element[4], element[5], element[0])
            mentorObjectList.append(mentorObject)
        return mentorObjectList

    def get_username(self):
        """
        Returns username of objc.
        :return (str): username of objc
        """
        return self.username

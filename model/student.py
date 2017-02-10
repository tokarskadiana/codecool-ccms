from model.user import User
from model.sqlRequest import SqlRequest


class Student(User):
    # list_of_students = []

    @classmethod
    def add_student(cls, password, first_name, last_name, telephone='', mail=''):
        """
        Initialize Assignment object.
        :param password (str): password
        :param first_name (str): first name
        :param last_name (str): last name
        :param telephone (str): telephone
        :param mail (str): mail
        """

        team_id = 1
        username = '{}.{}'.format(first_name, last_name)

        query = ('INSERT OR IGNORE INTO student (first_name,last_name,password,telephone,mail,username,team_id) VALUES ("{}","{}","{}","{}","{}","{}","{}");'.format(first_name, last_name, password, telephone, mail, username, team_id))

        SqlRequest.sql_request(query)




    @staticmethod
    def edit_student(index, mail, telephone, team):
        """
        Edit student attr.
        :param kwargs: name of attr and value of it
        """
        # for key, value in kwargs.items():
        #     if key:
        #         if key in self.__dict__.keys():
        #             self.__dict__[key] = value
        query = ('UPDATE student SET mail="{}", telephone="{}", team_id={} WHERE id={}'.format(mail, telephone, team, index))
        SqlRequest.sql_request(query)



    @staticmethod
    def delete_student(id):
        """
        Remove student from list_of_students by given username.
        :param username (str): value of username attr
        """

        query = ('DELETE FROM student WHERE id={}'.format(id))
        SqlRequest.sql_request(query)



    @staticmethod
    def list_student():
        """
        Returns static variable list_of_students.
        :return (list): list of students
        """
        list_of_students = []


        query = ('SELECT id, first_name,last_name, username, mail, telephone, team_id FROM student')

        data = SqlRequest.sql_request(query)

        # for row in data:
        #     list_of_students.append(Student(row[1], row[2], row[4], row[5], row[6]))

        # students = []
        # for student in list_of_students:
        #     students.append(Student.first_name, Student.last_name )

        return data



    def get_details(self):
        """
        Returns list of personal data.
        :return (list): list of personal data
        """
        list_det = [self.first_name, self.last_name, self.username, self.telephone, self.mail]
        return list_det

    def get_username(self):
        """
        Returns username of objc.
        :return (str): username of objc
        """
        return self.username

    def __str__(self):
        return '{} {} {}'.format(self.first_name, self.last_name, self.username)

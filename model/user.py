import base64

class User:
    """
    This class representing User class
    """
    line = 0
    def __init__(self, password, first_name, last_name, telephone, mail):
        """
        Constructs User object
        :param password: (str) store of password of User object
        :param first_name: (str) store of first name of User object
        :param last_name: (str) store of last name of User object
        :param telephone: (str) store of phone number of User object
        :param mail: (str) store of e-mail address of User object
        """
        self.username = '{}.{}'.format(first_name, last_name)
        self.password = self.decodeBase64(password)
        # self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.telephone = telephone
        self.mail = mail

    @staticmethod
    def encodeBase64(password):
        """
        Static method to encode user password
        :param password: (str) password
        :return: (str) encoded password
        """
        # print(password)
        encoded_pwd = base64.encodebytes(password.encode())
        # print(encoded_pwd)
        encoded_pwd = str(encoded_pwd)

        return encoded_pwd

    @staticmethod
    def decodeBase64(password):
        """
        Static method for decoding encoded password
        :param password: (str) encoded password
        :return: decoded password
        """
        print(password)
        passwd_striped = password.replace('\\n','')
        print(passwd_striped)
        passwd  = passwd_striped[2:]
        passwd = passwd[:-1]
        passwd = passwd.encode()
        # print(passwd)
        decoded_pwd = base64.standard_b64decode(passwd).decode()
        print(decoded_pwd)
        return decoded_pwd


    @classmethod
    def log_in(cls, username=None, password=None):
        """
        Check if given username and password are in data base.
        :param username (str): username
        :param password (str): password
        :return (objc): objc with given parameters
        """
        from mentor import Mentor
        from student import Student
        from manager import Manager

        users = [Mentor.mentors_list,
                 Student.list_of_students,
                 Employee.employee_list,
                 Manager.managers_list]

        for list_of_users in users:
            for person in list_of_users:
                if username == person.username:
                    if password == person.password:
                        return person
        return False



class Employee(User):
    """
    This class representing Employee class
    """
    employee_list = []

    @classmethod
    def create(cls, password, first_name, last_name, telephone='', mail=''):
        """
        Create new employee object
        def create(cls, password, first_name, last_name, telephone=None, mail=None):

        :param password (str):
        :param first_name (str):
        :param last_name (str):
        :param telephone (str):
        :param mail (str):
        """
        password_coded = cls.encodeBase64(password)
        empl = Employee(password_coded, first_name, last_name, telephone, mail)
        cls.employee_list.append(empl)

    @classmethod
    def add_employee(cls, password, first_name, last_name, telephone, mail):
        """
        Add new employee
        Add employee objc.
        :param password (str):
        :param first_name (str):
        :param last_name (str):
        :param telephone (str):
        :param mail (str):
        """
        e = Employee(password, first_name, last_name, telephone, mail)
        cls.employee_list.append(e)

    @classmethod
    def list_employee(cls):
        """
        Class method for return list of employers (assistants)
        :return: (list) list of employers
        """
        return cls.employee_list

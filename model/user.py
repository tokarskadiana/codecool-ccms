import base64


class User:
    """
    This class represent all users of this program
    """
    line = 0

    def __init__(self, password, first_name, last_name, telephone, mail):
        """
        Constructs User object
        :param password:
        :param first_name:
        :param last_name:
        :param telephone:
        :param mail:
        """
        self.username = '{}.{}'.format(first_name, last_name)
        self.password = self.decodeBase64(password)
        self.first_name = first_name
        self.last_name = last_name
        self.telephone = telephone
        self.mail = mail

    @staticmethod
    def encodeBase64(password):
        """
        Code given password.
        :param password (str): password
        :return:
        """
        encoded_pwd = base64.encodebytes(password.encode())
        encoded_pwd = str(encoded_pwd)

        return encoded_pwd

    @staticmethod
    def decodeBase64(password):
        """
        Decode given password.
        :param password: password to decode
        :return: decoded password
        """
        passwd_striped = password.replace('\\n', '')
        passwd = passwd_striped[2:]
        passwd_striped = password.replace('\\n', '')
        passwd = passwd_striped[2:]
        passwd = passwd[:-1]
        passwd = passwd.encode()
        decoded_pwd = base64.standard_b64decode(passwd).decode()
        return decoded_pwd


class Employee(User):
    employee_list = []

    @classmethod
    def create(cls, password, first_name, last_name, telephone='', mail=''):
        """
        Create employee objc.
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
        Return list of employee.
        :return (list): list of employee
        """
        return cls.employee_list

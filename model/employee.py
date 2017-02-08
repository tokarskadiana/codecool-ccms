from model.user import User


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

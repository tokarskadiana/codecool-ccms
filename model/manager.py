from model.employee import Employee
from model.sqlRequest import SqlRequest


class Manager(Employee):
    managers_list = []

    @classmethod
    def add_manager(cls, password, first_name, last_name, telephone='', mail=''):
        """
        Add manager objc to list.
        :param password (str): password of manager
        :param first_name (str): first name of manager
        :param last_name (str): last name of manager
        :param telephone (str): telephone of manager
        :param mail (str): mail of manager
        """
        password_coded = cls.encodeBase64(password)
        # print("JESTEM W MANAGERZE")
        # SqlRequest.sql_request(
        #     "INSERT OR IGNORE INTO  employee (first_name,last_name,password,tel,mail) VALUES (?,?,?,?,?)",
        #     (first_name, last_name, password_coded, telephone, mail))
        # print('POSZŁO')
        m = Manager(password_coded, first_name, last_name, telephone, mail)
        cls.managers_list.append(m)


    @classmethod
    def list_manager(cls):
        """
        Returns list of manager.
        :return (list): manager list
        """
        return cls.managers_list

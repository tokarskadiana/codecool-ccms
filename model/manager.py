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
        username = '{}.{}'.format(first_name, last_name)
        SqlRequest.sql_request('INSERT OR IGNORE INTO  employee (first_name,last_name,password,username,position) VALUES ("{}","{}","{}","{}","{}")'.format(first_name,last_name,password,username,'manager'))



    @classmethod
    def list_manager(cls):
        """
        Returns list of manager.
        :return (list): manager list
        """
        query = 'SELECT * FROM employee WHERE position = "manager"'
        managerSqlList = SqlRequest.sql_request(query)
        managerObjectList = []
        for element in managerSqlList:
            managerObject = cls(element[3],element[1],element[2])
            managerObjectList.append(managerObject)
        return managerObjectList

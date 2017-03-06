from model.user import User
from model.sqlRequest import SqlRequest

class Employee(User):
    """
    This class representing Employee class
    """
    employee_list = []

    def __init__(self, password, first_name, last_name, telephone="", mail="", id=None, salary=None):
        super().__init__(password, first_name, last_name, telephone, mail)
        self.id = id
        self.salary = salary




    @classmethod
    def add_employee(cls, password, first_name, last_name, telephone="", mail=""):
        """
        Add new employee
        Add employee objc.
        :param password (str):
        :param first_name (str):
        :param last_name (str):
        :param telephone (str):
        :param mail (str):
        """
        username = '{}.{}'.format(first_name, last_name)
        SqlRequest.sql_request('INSERT OR IGNORE INTO  employee (first_name,last_name,password,username,position) VALUES ("{}","{}","{}","{}","{}")'.format(first_name,last_name,password,username,'employee'))



    @classmethod
    def list_employee(cls):
        """
        Class method for return list of employers (assistants)
        :return: (list) list of employers
        """
        query = 'SELECT * FROM employee WHERE position = "employee"'
        employeeSqlList = SqlRequest.sql_request(query)
        employeeObjectList = []
        for element in employeeSqlList:
            employeeObject = cls(element[3],element[1],element[2])
            employeeObjectList.append(employeeObject)
        return employeeObjectList
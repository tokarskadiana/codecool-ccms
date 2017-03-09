from model.employee import Employee
from model.sqlRequest import SqlRequest


class Manager(Employee):

    @classmethod
    def get_by_id(cls, id):
        Employee.get_by_id(id, 'menager')

    @classmethod
    def list_managers(cls):
        """
        """
        return Employee.list_employee('menager')

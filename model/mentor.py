from model.employee import Employee
from model.sqlRequest import SqlRequest


class Mentor(Employee):

    @classmethod
    def get_by_id(cls, id):
        Employee.get_by_id(id, 'mentor')

    @classmethod
    def list_mentors(cls):
        """
        """
        return Employee.list_employee('mentor')

from model.employee import Employee
from model.sqlRequest import SqlRequest


class Mentor(Employee):

    @classmethod
    def get_by_id(cls, id):
        return super(Mentor, cls).get_by_id(id, 'mentor')

    @classmethod
    def list_mentors(cls):
        """
        """
        return super(Mentor, cls).list_employee('mentor')

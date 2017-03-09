from model.employee import Employee
from model.sqlRequest import SqlRequest


class Manager(Employee):

    @classmethod
    def get_by_id(cls, id):
        """

        :param id:
        :return:
        """
        return super(Manager, cls).get_by_id(id, 'manager')

    @classmethod
    def list_managers(cls):
        """
        """
        return super(Manager, cls).list_employee('manager')

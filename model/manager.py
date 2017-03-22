from model.employee import Employee
from model.sql_alchemy_db import db

class Manager(Employee):
    """
    Represents manager object.
    """
    __tablename__ = "employee"

    @classmethod
    def get_by_id(cls, id):
        """
        Get mentor by id from database.
        arguments: int(mentor id)
        return: obj(Mentor)
        """
        return super(Manager, cls).get_by_id(id)
    @classmethod
    def list_managers(cls):
        """
        Returns list of managers object from database.
        return: list(list of Manager objects)
        """
        return super(Manager, cls).list_employee('manager')

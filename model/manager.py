from model.employee import Employee


class Manager(Employee):
    """
    Represents manager object.
    """

    @classmethod
    def get_by_id(cls, id):
        """
        Get manager by id from database.
        arguments: int(manager id)
        return: obj(Manager)
        """
        return super(Manager, cls).get_by_id(id, 'manager')

    @classmethod
    def list_managers(cls):
        """
        Returns list of managers object from database.
        return: list(list of Manager objects)
        """
        return super(Manager, cls).list_employee('manager')

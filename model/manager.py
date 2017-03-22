from model.employee import Employee


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

    @classmethod
    def get_to_login(cls, username, password):
        """
        Return Manager object by given username and password.
        :param username (str): username
        :param password (str): password
        :return: object
        """
        return super(Manager, cls).get_to_login(username, password, 'manager')

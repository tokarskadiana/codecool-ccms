from model.employee import Employee


class Mentor(Employee):
    """
    Represents Mentor object.
    """
    __tablename__ = 'employee'

    @classmethod
    def get_by_id(cls, id):
        """
        Get mentor by id from database.
        arguments: int(mentor id)
        return: obj(Mentor)
        """
        return super(Mentor, cls).get_by_id(id)

    @classmethod
    def list_mentors(cls):
        """
        Returns list of mentors object from database.
        return: list(list of Mentor objects)
        """
        return super(Mentor, cls).list_employee('mentor')

    @classmethod
    def get_to_login(cls, username, password):
        """
        Return Mentor object by given username and password.
        :param username (str): username
        :param password (str): password
        :return: object
        """
        return super(Mentor, cls).get_to_login(username, password, 'mentor')

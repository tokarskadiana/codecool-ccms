from model.employee import Employee


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
        password_coded = cls.encodeBase64(password)
        m = Manager(password_coded, first_name, last_name, telephone, mail)
        cls.managers_list.append(m)

    @classmethod
    def list_manager(cls):
        """
        Returns list of manager.
        :return (list): manager list
        """
        return cls.managers_list

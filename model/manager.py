from model.user import Employee


class Manager(Employee):
    managers_list = []

    @classmethod
    def add_manager(cls, password, first_name, last_name, telephone=None, mail=None):
        password_coded = cls.encodeBase64(password)
        m = Manager(password_coded, first_name, last_name, telephone, mail)
        cls.managers_list.append(m)

    @classmethod
    def list_manager(cls):
        return cls.managers_list

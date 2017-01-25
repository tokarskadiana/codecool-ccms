from user import User


class Manager(User):
    managers_list = []

    @classmethod
    def add_manager(cls, password, first_name, last_name, telephone=None, mail=None):
        m = Manager(password, first_name, last_name, telephone, mail)
        cls.managers_list.append(m)


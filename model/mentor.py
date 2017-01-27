from model.user import Employee


class Mentor(Employee):
    mentors_list = []

    @classmethod
    def add_mentor(cls, password, first_name, last_name, telephone='', mail=''):
        password_coded = cls.encodeBase64(password)
        m = Mentor(password_coded, first_name, last_name, telephone, mail)
        cls.mentors_list.append(m)

    def edit_mentor(self, **kwargs):
        for key, value in kwargs.items():
            for dict_key, dict_value in self.__dict__.items():
                if key == dict_key:
                    self.__dict__[dict_key] = value
                    return True
        return False

    def view_mentor_details(self):
        return self.first_name, self.last_name, self.username, self.telephone, self.mail

    @staticmethod
    def delete_mentor(mentor):
        Mentor.mentors_list.remove(mentor)
        if mentor not in Mentor.mentors_list:
            return True
        return False

    @staticmethod
    def list_mentors():
        return Mentor.mentors_list

    def __str__(self):
        return ('{} {} {}'.format(self.first_name, self.last_name, self.username))

    def get_username(self):
        return self.username

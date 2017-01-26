from model.user import Employee


class Mentor(Employee):
    mentors_list = []

    @classmethod
    def add_mentor(cls, password, first_name, last_name, telephone=None, mail=None):
        password_coded = cls.encodeBase64(password)
        m = Mentor(password_coded, first_name, last_name, telephone, mail)
        cls.mentors_list.append(m)

    def edit_mentor(self, **kwargs):
        for key, value in kwargs.items():
            if key:
                if key in self.__dict__.keys():
                    self.__dict__[key] = value

        return self.__dict__.items()

    def view_mentor_details(self, username):
        for mentor in self.mentors_list:
            if username == mentor.username:
                return [self.username, self.first_name, self.last_name, self.telephone, self.mail]

    @staticmethod
    def delete_mentor(username):
        for mentor in Mentor.mentors_list:
            if username == mentor.username:
                Mentor.mentors_list.remove(mentor)

        return Mentor.mentors_list

    @staticmethod
    def list_mentors():
        return Mentor.mentors_list

    def __str__(self):
        return ('{} {}'.format(self.first_name, self.last_name))

    def get_username(self):
        return self.username

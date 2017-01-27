from model.user import Employee


class Mentor(Employee):
    mentors_list = []

    @classmethod
    def add_mentor(cls, password, first_name, last_name, telephone='', mail=''):
        """
        Add mentor to mentors list.
        :param password (str): password of mentor
        :param first_name (str):  first name of manager
        :param last_name (str): last name of manager
        :param telephone (str): telephone of mentor
        :param mail (str): mail of mentor
        """
        password_coded = cls.encodeBase64(password)
        m = Mentor(password_coded, first_name, last_name, telephone, mail)
        cls.mentors_list.append(m)

    def edit_mentor(self, **kwargs):
        """
        Edit attr of mentor objc by given key words.
        :param kwargs (dict): attr of mentor objc and value to change
        :return (dict): all attr of mentor objc
        """
        for key, value in kwargs.items():
            if key:
                if key in self.__dict__.keys():
                    self.__dict__[key] = value

        return self.__dict__.items()

    def view_mentor_details(self, username):
        """
        Returns value of attr by given username.
        :param username (str): value of mentor objc
        :return (list): list of value of attr
        """
        for mentor in self.mentors_list:
            if username == mentor.username:
                return [self.username, self.first_name, self.last_name, self.telephone, self.mail]

    @staticmethod
    def delete_mentor(username):
        """
        Remove mentor from list of mentors by given username.
        :param username: username of objc
        :return (list): list of mentors objc
        """
        for mentor in Mentor.mentors_list:
            if username == mentor.username:
                Mentor.mentors_list.remove(mentor)

        return Mentor.mentors_list

    @staticmethod
    def list_mentors():
        """
        Returns mentors list.
        :return (list): list of mentors objc
        """
        return Mentor.mentors_list

    def __str__(self):
        """
        Returns full name of objc.
        :return (str): full name
        """
        return ('{} {}'.format(self.first_name, self.last_name))

    def get_username(self):
        """
        Returns username of objc.
        :return (str): username of objc
        """
        return self.username

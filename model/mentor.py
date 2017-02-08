from model.employee import Employee


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
            for dict_key, dict_value in self.__dict__.items():
                if key == dict_key:
                    self.__dict__[dict_key] = value
                    return True
        return False

    def view_mentor_details(self):
        """
        Returns value of attr by given username.
        :param username (str): value of mentor objc
        :return (tuple): tuple of value of attr
        """
        return self.first_name, self.last_name, self.username, self.telephone, self.mail

    @staticmethod
    def delete_mentor(mentor):
        """
        Remove mentor from list of mentors by given username.
        :param username: username of objc
        :return (bool):
        """
        Mentor.mentors_list.remove(mentor)
        if mentor not in Mentor.mentors_list:
            return True
        return False

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
        return ('{} {} {}'.format(self.first_name, self.last_name, self.username))

    def get_username(self):
        """
        Returns username of objc.
        :return (str): username of objc
        """
        return self.username

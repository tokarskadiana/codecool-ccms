from user import User


class Mentor(User):
    mentors_list = []


    @classmethod
    def add_mentor(cls, password, first_name, last_name, telephone=None, mail=None):
        m = Mentor(password, first_name, last_name, telephone, mail)
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

    @classmethod
    def delete_mentor(cls, username):
        for mentor in Mentor.mentors_list:
            if username == mentor.username:
                Mentor.mentors_list.remove(mentor)

        return Mentor.mentors_list

    def list_mentors(self):
        return self.mentors_list



#
# Mentor.add_mentor('password', 'Marcin', 'Dupa', '123', '@@@')
# Mentor.add_mentor('password', 'dupa', 'Dupa', '345', '@@@')
# lista = Mentor.mentors_list
#
# print(lista)
# print(Mentor.mentors_list[0].first_name)
# Mentor.delete_mentor('dupa.Dupa')
# print(lista)
# Mentor.mentors_list[0].edit_mentor(first_name='Dupaaaaaaaaa')
#
# # Mentor.edit_mentor(Mentor.mentors_list[0], first_name='dupaaaaaaaaaaaaaaaaaaa')
# print(lista)
# print(Mentor.mentors_list[0].first_name)




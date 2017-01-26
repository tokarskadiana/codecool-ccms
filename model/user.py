import base64

class User:
    line = 0
    def __init__(self, password, first_name, last_name, telephone, mail):
        self.username = '{}.{}'.format(first_name, last_name)
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.telephone = telephone
        self.mail = mail

    # @staticmethod
    # def encodeBase64(password):
    #     # test = base64.standard_b64encode(password.encode('utf-8'))
    #     # print(test)
    #     # test2 = str(test)
    #     # print(test2).strip('\\')
    #     # test3 = bytes(test2.encode('utf-8'))
    #     # print(base64.standard_b64decode(test3))
    #     print(str(base64.standard_b64encode(password.encode('utf-8'))))
    #     return str(base64.standard_b64encode(password.encode('utf-8')))
    #
    # @staticmethod
    # def decodeBase64(password):
    #     User.line += 1
    #     print(User.line)
    #     passwd = password
    #     # print(passwd)
    #     # print(type(passwd))
    #     passwd_strip = passwd.strip('\\')
    #     passwd_strip = passwd_strip[2:]
    #     # print(passwd_strip)
    #
    #     striped_password = passwd_strip.encode('utf-8')
    #     # print(type(striped_password))
    #     # print(striped_password)
    #     # print(base64.standard_b64decode(password).decode('utf-8'))
    #     print(str(base64.standard_b64decode(striped_password)))
    #     return str(base64.standard_b64decode(striped_password))


    @classmethod
    def log_in(cls, username=None, password=None):
        from mentor import Mentor
        from student import Student
        from manager import Manager

        users = [Mentor.mentors_list,
                 Student.list_of_students,
                 Employee.employee_list,
                 Manager.managers_list]

        for list_of_users in users:
            for person in list_of_users:
                if username == person.username:
                    if password == person.password:
                        return person
        return False

    @classmethod
    def sign_out(cls):
        # save data to file
        cls.log_in()


class Employee(User):
    employee_list = []

    @classmethod
    def create(cls, password, first_name, last_name, telephone=None, mail=None):
        empl = Employee(password, first_name, last_name, telephone, mail)
        cls.employee_list.append(empl)

    @classmethod
    def add_employee(cls, password, first_name, last_name, telephone, mail):
        e = Employee(password, first_name, last_name, telephone, mail)
        cls.employee_list.append(e)

    @classmethod
    def list_employee(cls):
        return cls.employee_list

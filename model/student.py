from model.user import User
from model.sqlRequest import SqlRequest


class Student(User):

    def __init__(self, id, password, first_name, last_name, telephone="", mail="", team_id=""):
        super(Student, self).__init__(id, password, first_name,
                                      last_name, telephone, mail)
        self.team_id = team_id
        self.team_name = self.get_team_name(team_id)

    def get_team_name(self, team_id):
        query = 'SELECT * FROM team WHERE id={}'.format(team_id)
        for row in SqlRequest.sql_request(query):
            team_name = row[1]
        return team_name

    @classmethod
    def get_by_id(cls, id):
        query = 'SELECT * FROM student WHERE id={}'.format(id)
        student = SqlRequest.sql_request(query)
        if student:
            return cls(id=student[0][0],
                       password=student[0][3],
                       first_name=student[0][1],
                       last_name=student[0][2],
                       telephone=student[0][4],
                       mail=student[0][5],
                       team_id=student[0][7])
        return None

    def add_student(self):
        """
        Initialize Assignment object.
        :param password (str): password
        :param first_name (str): first name
        :param last_name (str): last name
        :param telephone (str): telephone
        :param mail (str): mail
        """
        username = '{}.{}'.format(self.first_name, self.last_name)
        query = (
            'INSERT OR IGNORE INTO student (first_name,last_name,password,telephone,mail,username,team_id) VALUES("{}","{}","{}","{}","{}","{}","{}");'.format(
                self.first_name, self.last_name, self.password, self.telephone, self.mail, username, self.team_id))
        SqlRequest.sql_request(query)

    def edit_student(self):
        """
        Edit student attr.
        :param kwargs: name of attr and value of it
        """
        username = '{}.{}'.format(self.first_name, self.last_name)
        query = ("""UPDATE student SET first_name="{}", last_name="{}", password="{}", telephone="{}", mail="{}",
        team_id={}, username="{}" WHERE id={};""".format(self.first_name, self.last_name, self.password,
                                                         self.telephone, self.mail, self.team_id, username, self.id))

        SqlRequest.sql_request(query)

    def delete_student(self):
        """
        Remove student from list_of_students by given username.
        :param username (str): value of username attr
        """

        query = ('DELETE FROM student WHERE id={}'.format(self.id))
        SqlRequest.sql_request(query)

    @classmethod
    def list_students(cls):
        """
        Returns static variable list_of_students.
        :return (list): list of students
        """
        list_of_students = []

        query = 'SELECT id, password, first_name,last_name, mail, telephone, team_id FROM student'

        data = SqlRequest.sql_request(query)
        for row in data:
            list_of_students.append(cls(id=row[0],
                                        password=row[1],
                                        first_name=row[2],
                                        last_name=row[3],
                                        telephone=row[5],
                                        mail=row[4],
                                        team_id=row[6]))

        return list_of_students

    def full_name(self):
        return '{} {}'.format(self.first_name, self.last_name)

    def student_average_grade(self):
        """
        Get average student grade
        :return:
        """
        get_id = 'SELECT * FROM student WHERE username="{}"'.format(
            self.username)
        student_id = SqlRequest.sql_request(get_id)
        for id in student_id:
            get_average_grade = 'SELECT AVG(grade) FROM submition WHERE student_id = "{}"'.format(
                id[0])
            student_average_grade = SqlRequest.sql_request(get_average_grade)
            return student_average_grade[0][0]

    def get_attandance(self):
        """
        Get average present for student
        :return(int): average present
        """
        query = 'SELECT id FROM student WHERE username="{}"'.format(
            self.get_username())
        data = SqlRequest.sql_request(query)
        query_att = 'SELECT SUM(status), COUNT(status) FROM attendance WHERE student_id="{}"'.format(
            data[0][0])
        data_att = SqlRequest.sql_request(query_att)
        if data_att[0][0]:
            stats = (data_att[0][0] / data_att[0][1]) * 100
            return stats
        return False


from model.user import User
from model.sqlRequest import SqlRequest


class Student(User):
    def __init__(self, id, password, first_name, last_name, telephone="", mail="", team_id=""):
        super(Student, self).__init__(id, password, first_name,
                                      last_name, telephone, mail)
        self.team_id = team_id
        self.team_name = self.get_team_name(team_id)

    def get_team_name(self, team_id):
        if team_id:
            query = 'SELECT * FROM team WHERE id={}'.format(team_id)
            team = SqlRequest.sql_request(query)
            if team:
                for row in team:
                    team_name = row[1]
                return team_name
        return ''

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
        query = (
            'INSERT OR IGNORE INTO student (first_name,last_name,password,telephone,mail,username,team_id) \
            VALUES("{}","{}","{}","{}","{}","{}","{}");'.format(self.first_name, self.last_name, self.password,
                                                                self.telephone, self.mail, self.username, self.team_id))
        SqlRequest.sql_request(query)

    def edit_student(self):
        """
        Edit student attr.
        :param kwargs: name of attr and value of it
        """
        query = ("""UPDATE student SET first_name="{}", last_name="{}", password="{}", telephone="{}", mail="{}",
        team_id="{}", username="{}" WHERE id={};""".format(self.first_name, self.last_name, self.password,
                                                           self.telephone, self.mail, self.team_id,
                                                           self.username, self.id))

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
                                        telephone=(row[5] if row[5] else '-----'),
                                        mail=(row[4] if row[4] else '-----'),
                                        team_id=row[6]))

        return list_of_students

    def grade_average(self):
        """
        Get average student grade
        :return:
        """
        query = 'SELECT AVG(grade) FROM submition WHERE student_id = "{}"'.format(self.id)
        grade_average = SqlRequest.sql_request(query)
        if grade_average[0][0]:
            return grade_average[0][0]
        return '-----'

    def presence_average(self):
        """
        Get average present for student
        :return(int): average present
        """
        query = 'SELECT SUM(status), COUNT(status) FROM attendance WHERE student_id="{}"'.format(self.id)
        presence_average = SqlRequest.sql_request(query)
        if presence_average[0][1]:
            stats = (presence_average[0][0] / presence_average[0][1]) * 100
            return stats
        return '-----'


from model.user import User
from model.sqlRequest import SqlRequest


class Student(User):
    """
    Represents Student object.
    """

    def __init__(self, id, password, first_name, last_name, telephone="", mail="", team_id=""):
        """
        Student constructor.
        arguments:  int(id)
                    str(password)
                    str(first_name)
                    str(last_name)
                    str(telephone)
                    str(mail)
                    int(team_id)
        """
        super(Student, self).__init__(id, password, first_name,
                                      last_name, telephone, mail)
        self.team_id = team_id
        self.team_name = self.get_team_name(team_id)

    def get_team_name(self, team_id):
        """
        Return team name by team id.
        arguments: int(team_id)
        return: str(team name)
        """
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
        """
        Rteurn team object by id from database.
        arguments: int(id)
        return: obj(Team)
        """
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
        Add student to database.
        """
        query = (
            'INSERT OR IGNORE INTO student (first_name,last_name,password,telephone,mail,username,team_id) \
            VALUES("{}","{}","{}","{}","{}","{}","{}");'.format(self.first_name, self.last_name, self.password,
                                                                self.telephone, self.mail, self.username, self.team_id))
        SqlRequest.sql_request(query)

    def edit_student(self):
        """
        Update student id database.
        """
        query = ("""UPDATE student SET first_name="{}", last_name="{}", password="{}", telephone="{}", mail="{}",
        team_id="{}", username="{}" WHERE id={};""".format(self.first_name, self.last_name, self.password,
                                                           self.telephone, self.mail, self.team_id,
                                                           self.username, self.id))
        SqlRequest.sql_request(query)

    def delete_student(self):
        """
        Remove student from database..
        """
        query = ('DELETE FROM student WHERE id={}'.format(self.id))
        SqlRequest.sql_request(query)

    @classmethod
    def list_students(cls):
        """
        Find all students in database.
        return: list(Student objects)
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
        Get student average grade
        return: float(average garde)
        """
        query = 'SELECT AVG(grade) FROM submition WHERE student_id = "{}"'.format(self.id)
        grade_average = SqlRequest.sql_request(query)
        if grade_average[0][0]:
            return grade_average[0][0]

    def presence_average(self):
        """
        Get average present for student
        return: float(average present)
        """
        query = 'SELECT SUM(status), COUNT(status) FROM attendance WHERE student_id="{}"'.format(self.id)
        presence_average = SqlRequest.sql_request(query)
        if presence_average[0][1]:
            stats = (presence_average[0][0] / presence_average[0][1]) * 100
            return stats

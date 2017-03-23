from model.user import User
from model.sql_alchemy_db import db


class Student(User, db.Model):
    __tablename__ = 'student'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    password = db.Column(db.String)
    telephone = db.Column(db.String)
    mail = db.Column(db.String)
    username = db.Column(db.String)
    team_id = db.Column(db.Integer, db.ForeignKey('team.id'))
    # username_chkp = db.relationship('Checkpoint', backref="student", lazy="dynamic")

    # team = db.relationship("Team",foreign_keys=[team_id])
    # attendance_id = db.relationship('Attandance', backref="student", lazy="dynamic")


    def __init__(self, id, password, first_name, last_name, telephone="", mail="", team_id="", student_cards=""):
        """
        Represents Student object.
        """

        super(Student, self).__init__(id, password, first_name,
                                      last_name, telephone, mail)
        self.team_id = team_id
        self.student_cards = student_cards
        self.team_name = self.get_team_name(team_id)

    def get_team_name(self, teamID):
        """
        Return team name by team id.
        arguments: int(team_id)
        return: str(team name)
        """
        # Does it really work? Gota check it out
        print('get_team_name')
        if teamID:
            print(self.query.filter_by(team_id=teamID).first())
            return self.query.filter_by(team_id=teamID).first()
            # team_name  = self.query.join(Student).join(Team).fliter(Student.team_id==Team.id).first() Gota figure it out
            #  query = 'SELECT * FROM team WHERE id={}'.format(team_id)
            #  team = SqlRequest.sql_request(query)
            #  if team:
            #      for row in team:
            #          team_name = row[1]
            #      return team_name
        return ''

    @classmethod
    def get_by_id(cls, id):
        """
        Rteurn team object by id from database.
        arguments: int(id)
        return: obj(Team)
        """
        return db.session.query(cls).get(id)

    def add_student(self):
        """
        Add student to database.
        """
        db.session.flush()
        db.session.add(self)
        db.session.commit()

    def delete_student(self):
        """
        Remove student from database..
        """
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def list_students(cls):
        """
        Find all students in database.
        return: list(Student objects)
        """
        return cls.query.all()

    def grade_average(self):
        """
        Get student average grade
        return: float(average garde)
        """
        query = 'SELECT AVG(grade) FROM submition WHERE student_id = "{}"'.format(self.id)
        grade_average = SqlRequest.sql_request(query)
        grade = grade_average[0][0]
        if grade:
            return grade
        elif grade == 0:
            return 0.0

    def presence_average(self):
        """
        Get average present for student
        return: float(average present)
        """
        query = 'SELECT SUM(status), COUNT(status) FROM attendance WHERE student_id="{}"'.format(self.id)
        presence_average = SqlRequest.sql_request(query)
        if presence_average[0][1]:
            if not presence_average[0][0]:
                stats = 0
            stats = (presence_average[0][0] / presence_average[0][1]) * 100
            return stats

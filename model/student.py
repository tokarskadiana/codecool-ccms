from model.user import User
from model.sql_alchemy_db import db
from sqlalchemy import func
from model.sqlRequest import SqlRequest
from model.submit import Submition


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
    checkpoints = db.relationship('Checkpoint', backref="student", lazy="dynamic")
    teams = db.relationship('Team', backref="student", lazy="joined")
    attendance = db.relationship('Attendance', backref="student", lazy="dynamic")

    def __init__(self, id, password, first_name, last_name, telephone="", mail="", team_id="", student_cards=""):
        """
        Represents Student object.
        """

        super(Student, self).__init__(id, password, first_name,
                                      last_name, telephone, mail)
        self.team_id = team_id
        self.student_cards = student_cards
        self.team_name = self.get_team_name()

    def get_team_name(self):
        """
        Return team name by team id.
        arguments: int(team_id)
        return: str(team name)
        """
        if self.team_id:
            team_name = self.teams
            return team_name.name

        return ''

    def get_checkpoints(self):
        return self.checkpoints.all()

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
        grade = db.session.query(func.avg(Submition.grade)).filter_by(student_id=self.id).scalar()
        if grade:
            return grade
        elif grade == 0:
            return 0.0

    def presence_average(self):
        """
        Get average present for student
        return: float(average present)
        """
        attendance = self.attendance.first()
        if attendance:
            attendance = attendance.__class__
            presence_average = db.session.query(func.avg(attendance.status),
                                                func.count(attendance.status)).filter_by(student_id=self.id).all()
            avg = presence_average[0][0]
            count = presence_average[0][1]
            if count:
                if not avg:
                    avg = 0
                stats = (presence_average[0][0] / presence_average[0][1]) * 100
                return stats

    @classmethod
    def get_to_login(cls, username, password):
        """
        Return Employee object by given username and password.
        :param username (str): username
        :param password (str): password
        :return: object
        """
        return cls.query.filter_by(username=username, password=password).first()

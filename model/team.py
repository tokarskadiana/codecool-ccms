from model.sqlRequest import SqlRequest
from model.student import Student
from model.sql_alchemy_db import db


class Team(db.Model):
    """
    Represents team object.
    """

    __tablename__ = 'team'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)


    def __init__(self, name, id=None):
        """
        Team object constructor.
        """
        self.name = name
        self.id = id

    def get_members(self):
        """
        Returns list of Student objects where team_id = id of current team.
        return: list(Student objects)
        """
        members = db.session.query(Student).filter(Student.team_id==self.id)
        if members:
            return members

    def add_team(self):
        """
        Add team to database.
        """
        db.session.flush()
        db.session.add(self)
        db.session.commit()
        # query = 'INSERT OR IGNORE INTO team (name) VALUES("{}");'.format(self.name)
        # SqlRequest.sql_request(query)

    def edit_team(self):
        """
        Update team in database.
        """
        db.session.commit()

    def delete_team(self):
        """
        Remove team from database.
        """
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def list_teams(cls):
        """
        Get all team objects from database.
        return: list(Team objects)
        """
        return cls.query.all()

    @classmethod
    def get_by_id(cls, id):
        """
        Get team by id from database.
        return: obj(Team object)
        """
        return db.session.query(cls).get(id)

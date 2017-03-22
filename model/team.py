from model.sqlRequest import SqlRequest
from model.student import Student
from model.sql_alchemy_db import db


class Team(db.Model):
    """
    Represents team object.
    """
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
        members = []
        query = 'SELECT * FROM student WHERE team_id={}'.format(self.id)
        students = SqlRequest.sql_request(query)
        if students:
            for student in students:
                members.append(Student(id=student[0],
                                       password=student[3],
                                       first_name=student[1],
                                       last_name=student[2],
                                       telephone=student[4],
                                       mail=student[5],
                                       team_id=student[7]))
            return members

    def add_team(self):
        """
        Add team to database.
        """
        query = 'INSERT OR IGNORE INTO team (name) VALUES("{}");'.format(self.name)
        SqlRequest.sql_request(query)

    def edit_team(self):
        """
        Update team in database.
        """
        query = 'UPDATE team SET name="{}" WHERE id={}'.format(self.name, self.id)
        SqlRequest.sql_request(query)

    def delete_team(self):
        """
        Remove team from database.
        """
        query = 'DELETE FROM team WHERE id={}'.format(self.id)
        SqlRequest.sql_request(query)

    @classmethod
    def list_teams(cls):
        """
        Get all team objects from database.
        return: list(Team objects)
        """
        teams_list = []
        query = 'SELECT * FROM team'
        teams = SqlRequest.sql_request(query)
        for row in teams:
            teams_list.append(cls(row[1], row[0]))
        return teams_list

    @classmethod
    def get_by_id(cls, id):
        """
        Get team by id from database.
        return: obj(Team object)
        """
        query = 'SELECT * FROM team WHERE id={}'.format(id)
        team = SqlRequest.sql_request(query)
        if team:
            return cls(id=team[0][0], name=team[0][1])

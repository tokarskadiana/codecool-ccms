from model.sqlRequest import SqlRequest


class Team:

    def __init__(self, name, id=None):
        self.name = name
        self.id = id

    def get_members(self):
        members = []
        query = 'SELECT first_name, last_name FROM student WHERE team_id={}'.format(self.id)
        students = SqlRequest.sql_request(query)
        if students:
            for student in students:
                members.append('{} {}'.format(student[0], student[1]))
            return members

    def add_team(self):
        query = 'INSERT OR IGNORE INTO team (name) VALUES("{}");'.format(self.name)
        SqlRequest.sql_request(query)

    def edit_team(self):
        query = 'UPDATE team SET name="{}" WHERE id={}'.format(self.name, self.id)
        SqlRequest.sql_request(query)

    def delete_team(self):
        query = 'DELETE FROM team WHERE id={}'.format(self.id)
        SqlRequest.sql_request(query)

    @classmethod
    def list_teams(cls):
        teams_list = []
        query = 'SELECT * FROM team'
        teams = SqlRequest.sql_request(query)
        for row in teams:
            teams_list.append(cls(row[1], row[0]))
        return teams_list

    @classmethod
    def get_by_id(cls, id):
        query = 'SELECT * FROM team WHERE id={}'.format(id)
        team = SqlRequest.sql_request(query)
        if team:
            return cls(id=team[0][0], name=team[0][1])

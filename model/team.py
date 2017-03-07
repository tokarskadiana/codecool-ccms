from model.sqlRequest import SqlRequest

class Team:

    def __init__(self, name, id=None):
        self.name = name
        self.id = id

    @classmethod
    def list_teams(cls):
        teams_list = []
        query = 'SELECT * FROM team'
        teams = SqlRequest.sql_request(query)
        for row in teams:
            teams_list.append(cls(row[1], row[0]))
        return teams_list

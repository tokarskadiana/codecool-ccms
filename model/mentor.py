from model.employee import Employee
from model.sqlRequest import SqlRequest


class Mentor(Employee):
    @classmethod
    def get_by_id(cls, id , pos ="mentor"):
        query = 'SELECT * FROM employee WHERE id={} AND position = "{}"'.format(id,pos)
        mentor = SqlRequest.sql_request(query)
        if mentor:
            return cls(id=mentor[0][0],
                       password=mentor[0][3],
                       first_name=mentor[0][1],
                       last_name=mentor[0][3],
                       position=mentor[0][8],
                       telephone=mentor[0][4],
                       mail=mentor[0][5],
                       salary=mentor[0][7])
        return None

    @classmethod
    def list_mentors(cls, position):
        """
        """
        mentors_list = []
        query = 'SELECT * FROM employee WHERE position="{}"'.format(position)
        mentors = SqlRequest.sql_request(query)
        for row in mentors:
            mentors_list.append(cls(id=row[0],
                                     password=row[3],
                                     first_name=row[1],
                                     last_name=row[2],
                                     position=row[8],
                                     telephone=(row[4] if row[4] else '-----'),
                                     mail=(row[5] if row[5] else '-----'),
                                     salary=(row[7] if row[7] else '-----')))
        return mentors_list
from model.employee import Employee
from model.sqlRequest import SqlRequest


class Mentor(Employee):

    @classmethod
    def get_by_id(cls, id):

        query = 'SELECT * FROM employee WHERE id={} AND position = "{}"'.format(id, 'mentor')
        employee = SqlRequest.sql_request(query)
        if employee:
            return cls(id=employee[0][0],
                       password=employee[0][3],
                       first_name=employee[0][1],
                       last_name=employee[0][2],
                       position=employee[0][8],
                       telephone=employee[0][4],
                       mail=employee[0][5],
                       salary=employee[0][7])
        return None

    @classmethod
    def list_mentors(cls):
        """
        """
        return super(Mentor, cls).list_employee('mentor')

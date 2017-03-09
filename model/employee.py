from model.user import User
from model.sqlRequest import SqlRequest


class Employee(User):
    """
    This class representing Employee class
    """

    def __init__(self, id, password, first_name, last_name, position, telephone="", mail="", salary=""):
        super().__init__(id, password, first_name, last_name, telephone, mail)
        self.position = position
        self.salary = salary

    def add_employee(self):
        """
        Add mentor to db.
        """
        SqlRequest.sql_request(
            'INSERT OR IGNORE INTO  employee (first_name,last_name,password,telephone,username,position,mail,salary)\
            VALUES ("{}","{}","{}","{}","{}", "{}", "{}", "{}")'.format(self.first_name,
                                                                        self.last_name,
                                                                        self.password,
                                                                        self.telephone,
                                                                        self.username,
                                                                        self.position,
                                                                        self.mail,
                                                                        self.salary))

    def edit_employee(self):
        query = ("""UPDATE employee SET first_name="{}", last_name="{}", password="{}", telephone="{}", mail="{}",
                username="{}", salary="{}" WHERE id={}""".format(self.first_name, self.last_name, self.password,
                                                                 self.telephone, self.mail, self.username, self.salary,
                                                                 self.id))
        SqlRequest.sql_request(query)

    def delete_employee(self):
        """
        Remove employee from db.
        """
        query = ('DELETE FROM employee WHERE id={}'.format(self.id))
        SqlRequest.sql_request(query)

    @classmethod
    def get_by_id(cls, id, position):
        query = 'SELECT * FROM employee WHERE id={} AND position = "{}"'.format(id, position)
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
    def list_employee(cls, position):
        """
        """
        employee_list = []
        query = 'SELECT * FROM employee WHERE position="{}"'.format(position)
        employees = SqlRequest.sql_request(query)
        for row in employees:
            employee_list.append(cls(id=row[0],
                                     password=row[3],
                                     first_name=row[1],
                                     last_name=row[2],
                                     position=row[8],
                                     telephone=(row[4] if row[4] else '-----'),
                                     mail=(row[5] if row[5] else '-----'),
                                     salary=(row[7] if row[7] else '-----')))
        return employee_list

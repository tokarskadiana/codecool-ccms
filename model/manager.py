from model.employee import Employee
from model.sqlRequest import SqlRequest


class Manager(Employee):
    managers_list = []

    @classmethod
    def add_manager(cls, password, first_name, last_name, telephone='', mail=''):
        """
        Add manager objc to list.
        :param password (str): password of manager
        :param first_name (str): first name of manager
        :param last_name (str): last name of manager
        :param telephone (str): telephone of manager
        :param mail (str): mail of manager
        """
        username = '{}.{}'.format(first_name, last_name)
        SqlRequest.sql_request(
            'INSERT OR IGNORE INTO  employee (first_name,last_name,password,username,position) VALUES ("{}","{}","{}","{}","{}")'.format(
                first_name, last_name, password, username, 'manager'))

    @classmethod
    def get_by_id(cls, id , pos ="manager"):
        query = 'SELECT * FROM employee WHERE id={} AND position = "{}"'.format(id,pos)
        manager = SqlRequest.sql_request(query)
        if manager:
            return cls(id=manager[0][0],
                       password=manager[0][3],
                       first_name=manager[0][1],
                       last_name=manager[0][3],
                       position=manager[0][8],
                       telephone=manager[0][4],
                       mail=manager[0][5],
                       salary=manager[0][7])
        return None

    @classmethod
    def list_managers(cls, position):
        """
        """
        mangagers = []
        query = 'SELECT * FROM employee WHERE position="{}"'.format(position)
        manager_list = SqlRequest.sql_request(query)
        for row in manager_list:
            mangagers.append(cls(id=row[0],
                                     password=row[3],
                                     first_name=row[1],
                                     last_name=row[2],
                                     position=row[8],
                                     telephone=(row[4] if row[4] else '-----'),
                                     mail=(row[5] if row[5] else '-----'),
                                     salary=(row[7] if row[7] else '-----')))
        return mangagers

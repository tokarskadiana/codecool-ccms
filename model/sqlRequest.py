import sqlite3
class SqlRequest:
    @staticmethod
    def sql_request(query):
        """
        Return list of tuples from given query.
        :param query:
        :return:
        """
        print(query)
        conn = sqlite3.connect('codecool.sqlite')
        cursor = conn.cursor()
        cursor.execute(query)
        conn.commit()
        data = cursor.fetchall()
        conn.close()
        return data
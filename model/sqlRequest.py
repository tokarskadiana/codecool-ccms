class SqlRequest:
    @staticmethod
    def sql_request(query):
        """
        Return list of tuples from given query.
        :param query:
        :return:
        """
        conn = sqlite3.connect('../codecool.sqlite')
        cursor = conn.cursor()
        cursor.execute(query)
        data = cursor.fetchall()
        conn.close()
        return data
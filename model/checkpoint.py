from model.sqlRequest import SqlRequest

class Checkpoint:

    def __init__(self, mentor_id, date, card, student_id):
        self.mentor_id = mentor_id
        self.date = date
        self.card = card
        self.student_id = student_id




    def add_checpoint(self):

        request = 'INSERT INTO checkpoint (studentid, "date", card, mentorid) VALUES ({},"{}",{}, {})'.format(self.student_id, self.date, self.card, self.mentor_id)
        SqlRequest.sql_request(request)
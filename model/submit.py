from model.sqlRequest import SqlRequest
import datetime


class Submition:
    '''
    Represent an submit of individual student_username
    '''

    def __init__(self, assignment_id, student_id, id=None, content=None, grade=None, update=None, mentor_id=None):
        '''
        Constructor of Submition object.
        '''
        self.assignment_id = assignment_id
        self.student_id = student_id
        self.mentor_id = mentor_id
        self.content = content
        self.grade = grade
        self.update = update
        self.id = id

    def set_id(self, id):
        self.id = id

    @classmethod
    def create(cls, assignment_id, student_id):
        '''
        Make new submition.

        Returns: instance of Submition class
        '''
        SqlRequest.sql_request(
            'INSERT INTO submition (assignment_id, student_id) VALUES("{}", "{}")'.format(assignment_id, student_id))
        submition = cls(assignment_id, student_id)
        submition_id = SqlRequest.sql_request('SELECT * FROM submition WHERE id = (SELECT MAX(id) FROM submition);')[0][
            0]
        submition.set_id(submition_id)

    def update_grade(self, new_grade):
        '''
        Changes a submition grage to new value.

        Returns: boolean
        '''
        SqlRequest.sql_request(
            'UPDATE submition SET grade={} WHERE id={}'.format(new_grade, self.id))

    @staticmethod
    def change_grade(mentor_id, id, new_grade):
        '''
        Changes a submition grage to new value.

        Returns: boolean
        '''
        SqlRequest.sql_request(
            'UPDATE submition SET grade="{}", mentor_id="{}" WHERE id="{}";'.format(new_grade, mentor_id, id))

    def change_content(self, new_content):
        '''
        Changes a content of submition.

        Returns: boolean
        '''
        date = datetime.datetime.now().date()
        SqlRequest.sql_request(
            'UPDATE submition SET content="{}", update_data="{}" WHERE id="{}";'.format(new_content, date, self.id))

    @classmethod
    def get_submit(cls, student_id, assignment_id):
        query = 'SELECT assignment_id,student_id,content,id,grade,update_data,mentor_id FROM submition WHERE student_id={} \
                AND assignment_id={}'.format(student_id, assignment_id)

        submit = SqlRequest.sql_request(query)
        if submit:
            return cls(assignment_id=submit[0][0],
                       student_id=submit[0][1],
                       content=submit[0][2],
                       id=submit[0][3],
                       grade=submit[0][4],
                       update=submit[0][5],
                       mentor_id=submit[0][6],
                       )
        return None

    @classmethod
    def get_by_id(cls, id):
        print(id)
        query = 'SELECT assignment_id,student_id,content,id,grade,update_data,mentor_id FROM submition WHERE id={}'.format(
            id)
        submit = SqlRequest.sql_request(query)
        print(submit)
        if submit:
            return cls(assignment_id=submit[0][0],
                       student_id=submit[0][1],
                       content=submit[0][2],
                       id=submit[0][3],
                       grade=submit[0][4],
                       update=submit[0][5],
                       mentor_id=submit[0][6],
                       )
        return None

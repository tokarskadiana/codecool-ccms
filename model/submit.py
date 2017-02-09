from model.sqlRequest import SqlRequest
import datetime

class Submition:
    '''
    Represent an submit of individual student_username
    '''
    def __init__(self, assignment_id, student_id):
        '''
        Constructor of Submition object.
        '''
        self.assignment_id = assignment_id
        self.student_id = student_id
        self.mentor_id = None
        # self.content = None
        self.grade = None
        self.update = None
        self.id = None

    def set_id(self, id):
        self.id = id

    @classmethod
    def create(cls, assignment_id, student_id):
        '''
        Make new submition.

        Returns: instance of Submition class
        '''
        SqlRequest.sql_request('INSERT INTO submition (assignment_id, student_id) VALUES("{}", "{}")'.format(assignment_id, student_id))
        submition = cls(assignment_id, student_id)
        submition_id = SqlRequest.sql_request('SELECT * FROM submition WHERE id = (SELECT MAX(id) FROM submition);')[0][0]
        submition.set_id(submition_id)

    def get_content(self):
        '''
        Returns a content for submition.

        Returns: str
        '''
        return self.content

    def get_grade(self):
        '''
        Returns submit grade.

        Returns:str
        '''
        return self.grade

    @staticmethod
    def change_grade(mentor_id, id, new_grade):
        '''
        Changes a submition grage to new value.

        Returns: boolean
        '''
        SqlRequest.sql_request('UPDATE submition SET grade="{}", mentor_id="{}" WHERE id="{}";'.format(new_grade, mentor_id, id))

    @staticmethod
    def change_content(id, new_content):
        '''
        Changes a content of submition.

        Returns: boolean
        '''
        date = datetime.datetime.now().date()
        SqlRequest.sql_request('UPDATE submition SET content="{}", update_data="{}" WHERE id="{}";'.format(new_content, date, id))

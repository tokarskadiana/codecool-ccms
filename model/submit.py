from model.sql_alchemy_db import db
from model.sqlRequest import SqlRequest
import datetime


class Submition(db.Model):
    '''
    Represent an submit of individual student for specific assignment
    '''
    __tablename__ = 'submition'
    id = db.Column(db.Integer, primary_key=True)
    assignment_id = (db.Integer, db.ForeignKey('assignment.id'))
    student_id = (db.Integer, db.ForeignKey('student.id'))
    content = db.Column(db.String)
    grade = db.Column(db.Integer)
    update_data = db.Column(db.String)
    mentor_id = (db.Integer, db.ForeignKey('mentor.id'))

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
        submition_id = SqlRequest.sql_request('SELECT * FROM submition WHERE id = (SELECT MAX(id) \
        FROM submition);')[0][0]
        submition.set_id(submition_id)

    def update_grade(self, new_grade):
        '''
        Changes a submition grage to new value.
        '''
        SqlRequest.sql_request(
            'UPDATE submition SET grade={} WHERE id={}'.format(new_grade, self.id))

    def change_content(self, new_content):
        '''
        Changes a content of submition.
        '''
        date = datetime.datetime.now().date()
        SqlRequest.sql_request(
            'UPDATE submition SET content="{}", update_data="{}" WHERE id="{}";'.format(new_content, date, self.id))

    @classmethod
    def get_submit(cls, student_id, assignment_id):
        """
        Get submit for student for specific assqgnment
        arguments:  int(student_id)
                    int(assignment_id)
        return: obj(Submit)
        """
        return cls.query.filter(cls.student_id==student_id,cls.assignment_id==assignment_id).first()

    @classmethod
    def get_by_id(cls, id):
        """
        Get submit object by id from database.
        arguments: int(id)
        return: obj(Submit)
        """
        return db.session.query(cls).get(id)

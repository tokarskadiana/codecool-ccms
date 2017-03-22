from model.student import Student
from model.submit import Submition
from model.sqlRequest import SqlRequest
import datetime
from model.sql_alchemy_db import db

class Assignment(db.Model):
    '''
    Class representing assignment object.
    '''

    __tablename__ = 'assigment'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    date = db.Column(db.Date)
    description = db.Column(db.String)
    due_date = db.Column(db.Date)
    mentor_id = db.Column(db.Integer, db.ForeignKey('mentor.id'))
    type = db.Column(db.String)

    def __init__(self, title, description, due_date, mentor_id, type, id=None, date=None):
        '''
        Constructor of an object.
        '''
        self.title = title
        self.description = description
        self.due_date = due_date
        self.type = type
        self.mentor_id = mentor_id
        self.id = id
        self.date = date

    def set_id(self, id):
        self.id = id

    def make_submit_list(self):
        '''
        Make a list of submitions for particular assigment instance for every students.

        Returns:list
        '''
        student_list = SqlRequest.sql_request('SELECT * FROM student')
        for student in student_list:
            Submition.create(self.id, student[0])

    @classmethod
    def create(cls, title, description, type, user_name, due_date, mentor_id):  # add user_name
        '''
        Make new assignment and add it to assigment list.

        Returns: boolean value
        '''
        date = datetime.datetime.now().date()

        # assignment = Assignment(title=title, description=description, due_date=due_date, type=type, mentor_id=mentor_id, date=date)
        assignment = cls(title, description, due_date, mentor_id, type)

        query = "INSERT OR IGNORE INTO assignment (title, description, date, due_date, type, mentor_id) \
                 VALUES ('{}', '{}', '{}', '{}', '{}', '{}');".format(
            assignment.title, assignment.description, date,
            assignment.due_date, assignment.type, assignment.mentor_id)
        SqlRequest.sql_request(query)

        # db.session.query(Assignment).filter_by(id=max(i))
        assignment_id = SqlRequest.sql_request(
                'SELECT * FROM assignment WHERE id = (SELECT MAX(id) FROM assignment);')[0][0]
        assignment.set_id(assignment_id)
        assignment.make_submit_list()

    @classmethod
    def get_list(cls):
        '''
        Contains the list with all available assigment.
        title, description, due_date, mentor_id, type, id=None):
        Returns:list
        '''
        # list_assignment = []
        # data = SqlRequest.sql_request(
        #     'SELECT id,title,description,due_date,mentor_id,type FROM assignment')
        # for item in data:
        #     assignment = cls(item[1], item[2], item[3],
        #                      item[4], item[5], item[0])
        #     assignment.set_id(item[0])
        #     list_assignment.append(assignment)
        return cls.query.all()

    def get_submition_content(self, user_name):

        submitions = db.session.query(Submition).filter_by(assignment_id=self.id).all()
        user_id = db.session.query(Student).filter_by(username=user_name).all()[0][0]

        # SqlRequest.sql_request(
        #     "SELECT * FROM submition WHERE assignment_id='{}'".format(self.id))
            # SqlRequest.sql_request(
            # "SELECT * FROM student WHERE username='{}'".format(user_name))[0][0]

        for submition in submitions:
            if submition[2] == user_id:
                return submition[3]
        return None

    def submit_assignment(self, user_name, content):
        '''
        Make able to submit assigment to students.

        Returns: bool
        '''
        submitions = db.session.query(Submition).filter_by(assignment_id=self.id).all()

            # SqlRequest.sql_request(
            # "SELECT * FROM submition WHERE assignment_id='{}'".format(self.id))

        user_id = db.session.query(Student).filter_by(username=user_name)[0][0]

            # SqlRequest.sql_request(
            # "SELECT * FROM student WHERE username='{}'".format(user_name))[0][0]

        for submition in submitions:
            if submition[2] == user_id:
                Submition.change_content(submition[0], content)
                return True
        return False

    @classmethod
    def get_by_id(cls, id):
        """
        Return Assignment object by given id.
        :param id: Assignment id in assignment table.
        :return: object if exist row in table otherwise return None
        """
        if db.session.query(cls).get(id):
            return db.session.query(cls).get(id)
        return None

    @classmethod
    def get_students_of_assigmnent(cls, id):
        """
        Get all student assigned to assigmnent given by id.
        :param id: assigment id
        :return: list of tuples
        """
        query = "SELECT student.ID, first_name,last_name,grade,content,update_data, (\
        student.first_name || '.' || student.last_name ) as username from submition LEFT JOIN \
        student ON student.ID = student_id WHERE assignment_id={}".format(id)
        return SqlRequest.sql_request(query)

    @classmethod
    def get_all_assigmnets(cls, id):
        """
        Get all student submission by given student id
        :param id: student id
        :return: list of objects
        """
        query = 'SELECT DISTINCT assignment.id,title,description,due_date,assignment.mentor_id,type FROM \
        assignment LEFT JOIN submition ON assignment_id = submition.assignment_id WHERE student_id ={}'.format(id)
        assignments = SqlRequest.sql_request(query)
        assignments_list = []
        if assignments:
            for assignment in assignments:
                assignments_list.append(cls(id=assignment[0],
                                            title=assignment[1],
                                            description=assignment[2],
                                            due_date=assignment[3],
                                            mentor_id=assignment[4],
                                            type=assignment[5],
                                            ))
            return assignments_list
        return None

    def delete_assignment(self):
        """
        Delete assignment form database.
        """
        db.session.delete(self)
        db.session.commit()

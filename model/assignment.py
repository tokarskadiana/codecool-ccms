from model.student import Student
from model.submit import Submition
from model.sql_alchemy_db import db
from datetime import date


class Assignment(db.Model):
    '''
    Class representing assignment object.
    '''

    __tablename__ = 'assignment'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    date = db.Column(db.String, default=date.today())
    description = db.Column(db.String)
    due_date = db.Column(db.String)
    mentor_id = db.Column(db.Integer)
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
        student_list = db.session.query(Student).all()
        for student in student_list:
            submit = Submition(assignment_id=self.id, student_id=student.id)
            submit.create()

    @classmethod
    def create(cls, title, description, type, user_name, due_date, mentor_id):  # add user_name
        '''
        Make new assignment and add it to assigment list.

        Returns: boolean value
        '''

        assignment = Assignment(title=title, description=description, due_date=due_date, type=type, mentor_id=mentor_id)
        db.session.flush()
        db.session.add(assignment)
        db.session.commit()

        test = Assignment.get_by_id(assignment.id)
        test.make_submit_list()

    @classmethod
    def get_list(cls):
        '''
        Contains the list with all available assigment.
        title, description, due_date, mentor_id, type, id=None):
        Returns:list
        '''

        return cls.query.all()

    def submit_assignment(self, user_name, content):
        '''
        Make able to submit assigment to students.

        Returns: bool
        '''
        submitions = db.session.query(Submition).filter_by(assignment_id=self.id).all()

        user = db.session.query(Student).filter_by(username=user_name)
        user_id = user.id

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

        query = db.session.query(Student.id, Student.first_name, Student.last_name, Submition.grade, Submition.content,
                                 Submition.update_data, Student.username).filter(
            Student.id == Submition.student_id).filter(Submition.assignment_id == id).all()

        return query

    @classmethod
    def get_all_assigmnets(cls, id):
        """
        Get all student submission by given student id
        :param id: student id
        :return: list of objects
        """
        assignments = db.session.query(cls).distinct(Assignment.id, Assignment.description, Assignment.due_date,
                                                     Assignment.mentor_id).join(Submition).filter_by(student_id=id)

        if assignments:
            return assignments
        return None

    def delete_assignment(self):
        """
        Delete assignment form database.
        """
        db.session.delete(self)
        db.session.commit()

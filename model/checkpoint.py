from model.sql_alchemy_db import db
from model.student import Student


class Checkpoint(db.Model):
    '''
    Class representing checkpoint object.
    '''
    __tablename__ = 'checkpoint'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    checkpoint_date = db.Column(db.String)
    card = db.Column(db.Integer)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'))
    mentor_id = db.Column(db.Integer)

    def __init__(self, id, name, checkpoint_date, student_id, mentor_id, card):
        self.student_id = student_id
        self.mentor_id = mentor_id
        self.checkpoint_date = checkpoint_date
        self.id = id
        self.name = name
        self.card = card

    @classmethod
    def add_checkpoint_students(cls, name, checkpoint_date, mentor_id, student_list, card=0):
        """
        Add checkpoint to students
        :return:
        """

        for student in student_list:
            cls(None, name, checkpoint_date, student.id, mentor_id, card).add_checkpoint()

    def add_checkpoint(self):
        """Add checkpoint to db"""
        db.session.flush()
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_list_distinct(cls):
        """
        Get all available checkpoints
        :return:
        """
        return db.session.query(cls.name, cls.checkpoint_date).distinct()

    def remove_chkp(self):
        db.session.flush()
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def remove_checkpoint(cls, name):
        """
        Remove checkpoint from db
        :param name:
        :return:
        """
        checkpoints = cls.get_details_checkpoint_by_name(name)
        for checkpoint in checkpoints:
            checkpoint.remove_chkp()

    @classmethod
    def get_details_checkpoint_by_name(cls, name):
        """
        Get details of checkpoint by its name
        :return: List of objects
        """
        return cls.query.filter(cls.name == name).all()

    @classmethod
    def grade_checkpoints(cls, grade_list, id_list):
        """
        Grade checkpoint
        :param grade_list:
        :param id_list:
        :return:
        """
        for i, grade in enumerate(grade_list):
            try:
                if int(grade) >= 0 and int(grade) <= 3:
                    chkp = cls.get_by_id(id_list[i])
                    chkp.card = int(grade)
                    chkp.add_checkpoint()
            except:
                print("Hackers aren't ya?")

    def get_checkpoint_username(self):
        """
        Get student name
        :return: List of objects
        """
        student = Student.get_by_id(self.student_id)
        if student:
            return student.username
        return None

    @classmethod
    def get_by_student_id(cls, student_id):
        """
        Get list of checkpoint objects by  student id
        """

        return cls.query.filter(cls.student_id == student_id).all()

    @classmethod
    def get_by_id(cls, id):
        """
        Return team object by id from database.
        arguments: int(id)
        return: obj(Team)
        """
        return db.session.query(cls).get(id)

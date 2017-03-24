from model.user import User
from model.sqlRequest import SqlRequest
from model.sql_alchemy_db import db


class Employee(db.Model, User):
    """
    This class representing Employee class
    """
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    telephone = db.Column(db.String)
    username = db.Column(db.String, nullable=False)
    position = db.Column(db.String, nullable=False)
    mail = db.Column(db.String)
    salary = db.Column(db.String)

    def __init__(self, password, first_name, last_name, position, telephone=None, mail=None, salary=None):
        self.username = '{}.{}'.format(first_name.lower(), last_name.lower())
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.telephone = telephone
        self.mail = mail
        self.position = position
        self.salary = salary

    def add_employee(self):
        """
        Add mentor to db.
        """
        db.session.add(self)
        db.session.commit()

    def edit_employee(self, password, first_name, last_name, telephone, mail, salary):
        """
        Update employee in database.
        """
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.telephone = telephone
        self.mail = mail
        self.salary = salary
        db.session.commit()

    def delete_employee(self):
        """
        Remove employee from db.
        """
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def get_by_id(cls, id, position=None):
        """
        Get Object by given id and position in database.
        :param id: id
        :param position: position
        :return: Object
        """
        return cls.query.get(id)

    @classmethod
    def list_employee(cls, position):
        """
        Return list of Employee objects by given position.
        :param position (str): position
        :return: list of objects
        """
        return cls.query.filter_by(position=position).all()

    @classmethod
    def get_to_login(cls, username, password, position='assistant'):
        """
        Return Employee object by given username and password.
        :param username (str): username
        :param password (str): password
        :return: object
        """
        return cls.query.filter_by(username=username, password=password, position=position).first()

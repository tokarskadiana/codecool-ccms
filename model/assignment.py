from model.student import Student
from model.submit import Submition
from model.sqlRequest import SqlRequest
import datetime


class Assignment:
    '''
    Class representing assignment object.
    '''

    def __init__(self, title, description, due_date, mentor_id, type):
        '''
        Constructor of an object.
        '''
        self.title = title
        self.description = description
        self.due_date = due_date
        self.type = type
        self.mentor_id = mentor_id
        self.id = None

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
    def create(cls, title, description, type, user_name, due_date='No due date'): # add user_name
        '''
        Make new assignment and add it to assigment list.

        Returns: boolean value
        '''
        query = "SELECT * FROM employee WHERE (position='mentor' AND user_name='{}');".format(user_name)
        mentor_id = SqlRequest.sql_request(query)[0][0]
        assignment = cls(title, description, due_date, mentor_id, type)
        date = datetime.datetime.now().date()
        query = "INSERT OR IGNORE INTO assignment (title, description, date, due_date, type, mentor_id) \
                 VALUES ('{}', '{}', '{}', '{}', '{}', '{}');".format(
                 assignment.title, assignment.description, date,
                 assignment.due_date, assignment.type, assignment.mentor_id)
        SqlRequest.sql_request(query)
        assignment_id = SqlRequest.sql_request('SELECT * FROM assignment WHERE id = (SELECT MAX(id) FROM assignment);')[0][0]
        assignment.set_id(assignment_id)
        assignment.make_submit_list()

    def __str__(self):
        '''
        Returns formated output of object.

        Returns:str
        '''
        return '{} {} {}'.format(self.title, self.due_date, self.description)

    def get_title(self):
        return self.title

    @classmethod
    def get_list(cls):
        '''
        Contains the list with all available assigment.

        Returns:list
        '''
        list_assignment = []
        data = SqlRequest.sql_request('SELECT * FROM assignment')
        for item in data:
            assignment = cls(item[1], item[2], item[3], item[4], item[5])
            assignment.set_id(item[0])
            list_assignment.append(assignment)
        return list_assignment

    def get_submition_content(self, user_name):
        submitions = SqlRequest.sql_request("SELECT * FROM submition WHERE assignment_id='{}'".format(self.id))
        user_id = SqlRequest.sql_request("SELECT * FROM student WHERE username='{}'".format(user_name))[0][0]
        for submition in submitions:
            if submition[2] == user_id:
                return submition[3]
        return None

    def submit_assignment(self, user_name, content):
        '''
        Make able to submit assigment to students.

        Returns: bool
        '''
        submitions = SqlRequest.sql_request("SELECT * FROM submition WHERE assignment_id='{}'".format(self.id))
        user_id = SqlRequest.sql_request("SELECT * FROM student WHERE username='{}'".format(user_name))[0][0]
        for submition in submitions:
            if submition[2] == user_id:
                Submition.change_content(submition[0], content)
                return True
        return False

    def grade_assigment(self, mentor_username, student_username, grade):
        '''
        Make able mentor to grade students assigment.

        Returns:bool/int
        '''
        submitions = SqlRequest.sql_request("SELECT * FROM submition WHERE assignment_id='{}'".format(self.id))
        student_id = SqlRequest.sql_request("SELECT * FROM student WHERE username='{}'".format(student_username))[0][0]
        mentor_id = SqlRequest.sql_request("SELECT * FROM employee WHERE user_name='{}'".format(mentor_username))[0][0]
        for submition in submitions:
            if submition[2] == student_id:
                Submition.change_grade(mentor_id, submition[0], grade)
                return True
        return False

    def view_details(self):
        '''
        View details of particular assigment.

        Returns:list
        '''
        details = []
        submitions = SqlRequest.sql_request("SELECT * FROM submition WHERE assignment_id='{}'".format(self.id))
        for submition in submitions:
            user_name = SqlRequest.sql_request('SELECT * FROM student WHERE id="{}"'.format(submition[2]))[0][6]
            details.append([self.title, user_name, submition[3], submition[4]])
        return details

    def list_assignment_grades(self, user_name):
        '''
        Find submittion by user name and return info about garade.

        Returns:list
        '''
        submitions = SqlRequest.sql_request("SELECT * FROM submition WHERE assignment_id='{}'".format(self.id))
        user_id = SqlRequest.sql_request("SELECT * FROM student WHERE username='{}'".format(user_name))[0][0]
        for submition in submitions:
            if submition[2] == user_id:
                return submition[4]
        return None

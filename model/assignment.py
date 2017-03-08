from model.student import Student
from model.submit import Submition
from model.sqlRequest import SqlRequest
import datetime


class Assignment:
    '''
    Class representing assignment object.
    '''

    def __init__(self, title, description, due_date, mentor_id, type, id=None):
        '''
        Constructor of an object.
        '''
        self.title = title
        self.description = description
        self.due_date = due_date
        self.type = type
        self.mentor_id = mentor_id
        self.id = id

    def set_id(self, id):
        self.id = id


    def make_submit_list(self):
        '''
        Make a list of submitions for particular assigment instance for every students.

        Returns:list
        '''
        student_list = SqlRequest.sql_request('SELECT * FROM student')
        for student in student_list:
            print(student[0])
            Submition.create(self.id, student[0])

    @classmethod
    def create(cls, title, description, type, user_name, due_date, mentor_id):  # add user_name
        '''
        Make new assignment and add it to assigment list.

        Returns: boolean value
        '''
        query = "SELECT * FROM employee WHERE (position='mentor' AND username='{}');".format(user_name)
        # mentor_id = SqlRequest.sql_request(query)[0][0]
        assignment = cls(title, description, due_date, mentor_id, type)
        date = datetime.datetime.now().date()
        query = "INSERT OR IGNORE INTO assignment (title, description, date, due_date, type, mentor_id) \
                 VALUES ('{}', '{}', '{}', '{}', '{}', '{}');".format(
            assignment.title, assignment.description, date,
            assignment.due_date, assignment.type, assignment.mentor_id)
        SqlRequest.sql_request(query)
        assignment_id = \
            SqlRequest.sql_request('SELECT * FROM assignment WHERE id = (SELECT MAX(id) FROM assignment);')[0][0]
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
        title, description, due_date, mentor_id, type, id=None):
        Returns:list
        '''
        list_assignment = []
        data = SqlRequest.sql_request('SELECT id,title,description,due_date,mentor_id,type FROM assignment')
        for item in data:
            assignment = cls(item[1], item[2], item[3], item[4], item[5], item[0])
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
        student = SqlRequest.sql_request("SELECT * FROM student WHERE username='{}'".format(student_username))
        mentor = SqlRequest.sql_request("SELECT * FROM employee WHERE username='{}'".format(mentor_username))
        if student and mentor:
            student_id = student[0][0]
            mentor_id = mentor[0][0]
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
            if not submition[3]:
                con = 'No content'
            else:
                con = str(submition[3])
            if not submition[4]:
                grade = 'No grade'
            else:
                grade = str(submition[4])
            details.append([self.title, user_name, con, grade])
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

    # title, description, due_date, mentor_id, type, id = None
    @classmethod
    def get_by_id(cls, id):
        query = 'SELECT id,title,"date",description,due_date,mentor_id,type FROM assignment WHERE id={}'.format(id)
        assignments = SqlRequest.sql_request(query)
        if assignments:
            return cls(id=assignments[0][0],
                       title=assignments[0][1],
                       description=assignments[0][3],
                       due_date=assignments[0][4],
                       mentor_id=assignments[0][5],
                       type=assignments[0][6],
                       )
        return None

    @classmethod
    def get_studentsOfAssigmnent(cls, id):
        query = "SELECT student.ID, first_name,last_name,grade,content,update_data, (student.first_name || '.' || student.last_name ) as username  \
                from submition LEFT JOIN student ON student.ID = student_id WHERE assignment_id={}".format(id)
        return SqlRequest.sql_request(query)

    @classmethod
    def get_all_assigmnets(cls,id):
        query = 'SELECT DISTINCT assignment.id,title,description,due_date,assignment.mentor_id,type FROM assignment LEFT JOIN submition ON assignment_id = submition.assignment_id WHERE student_id ={}'.format(
            id)

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

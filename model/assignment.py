from student import Student
from submit import Submition
# from create_data import Database


class Assignment:
    '''
    Class representing assignment object
    '''

    def __init__(self, title, description, due_date, submit_list):
        '''
        Constructor of an object
        '''
        self.title = title
        self.description = description
        self.due_date = due_date
        self.submit_list = self.make_submit_list(submit_list)

    def make_submit_list(self, submit_list):
        '''
        Make a list of submitions for particular assigment instance for every students

        Returns:list
        '''
        if not submit_list:
            if Student.list_student():
                for student in Student.list_student():
                    submit_list.append(Submition.create(student.name))
                return submit_list
        return submit_list

    @classmethod
    def create(cls, title, description, due_date='No due date', submit_list=[]):
        '''
        Make new assignment and add it to assigment list.

        Returns: str
        '''
        assignment = cls(title, description, due_date, submit_list)
        Data.save_to_csv(assignment)        # save to csv immediately
        return 'Assignment was added.'

    def __str__(self):
        '''
        Returns formated output of object

        Returns:str
        '''
        return '{}, {}, {}'.format(self.title, self.due_date, self.description)

    @classmethod
    def list_assignment(cls):
        '''
        Contains the list with all available assigment

        Returns:list
        '''
        return Data.create_from_csv('../data_base/assigment.csv')  # create list of assiments from csv

    def submit_assignment(self, user_name, content):
        '''
        Make able to submit assigment to students

        Returns:str
        '''
        if self.submit_list:
            for submition in self.submit_list:
                if submition.get_student_username() == user_name:
                    if submition.change_content(content):
                        return 'You submit assigment.'
                    return 'Assignment already submited. You cant submit assigment twice.'
                return 'There no student with such username.'
        return 'You cant submit this assignment.'

    def grade_assigment(self, user_name, grade):
        '''
        Make able mentor to grade students assigment

        Returns:str
        '''
        if self.submit_list:
            for submition in self.submit_list:
                if submition.get_student_username() == user_name:
                    if submition.change_grade(grade):
                        return 'You grade {} assigment.'.format(user_name)
                    return 'Assignment already graded. You cant grade assigment twice.'
                return 'There no student with such username.'
        return 'You cant grade this assignment.'

    def view_details(self):
        '''
        View details of particular assigment

        Returns:list
        '''
        details = []
        for submition in self.submit_list:
            details.append([submition.get_student_username(),
                            submition.get_content(), submition.get_grade()])

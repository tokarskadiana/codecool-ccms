from model.student import Student
from model.submit import Submition
# from create_data import Database


class Assignment:
    '''
    Class representing assignment object.
    '''
    list_assignment = []

    def __init__(self, title, description, due_date, submit_list):
        '''
        Constructor of an object.
        '''
        self.title = title
        self.description = description
        self.due_date = due_date
        self.submit_list = self.make_submit_list(submit_list)

    def make_submit_list(self, submit_list):
        '''
        Make a list of submitions for particular assigment instance for every students.

        Returns:list
        '''
        if not submit_list:
            if Student.list_student():
                for student in Student.list_student():

                    submit_list.append(Submition.create(student.get_username()))
                return submit_list
        return submit_list

    @classmethod
    def create(cls, title, description, due_date='No due date', submit_list=[]):
        '''
        Make new assignment and add it to assigment list.

        Returns: boolean value
        '''
        assigment = cls(title, description, due_date, submit_list)
        cls.list_assignment.append(
            cls(title, description, due_date, submit_list))
        if assigment in cls.list_assignment:
            return True
        return False

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
        return cls.list_assignment

    def get_submition_content(self, user_name):
        if self.submit_list:
            for submition in self.submit_list:
                if submition.get_student_username() == user_name:
                    return submition.get_content()

    def submit_assignment(self, user_name, content):
        '''
        Make able to submit assigment to students.

        Returns: bool
        '''
        if self.submit_list:
            for submition in self.submit_list:
                if submition.get_student_username() == user_name:
                    if submition.change_content(content):
                        return True
        return False

    def grade_assigment(self, user_name, grade):
        '''
        Make able mentor to grade students assigment.

        Returns:bool/int
        '''
        if self.submit_list:
            for submition in self.submit_list:
                if submition.get_student_username() == user_name:
                    if submition.change_grade(grade):
                        return True
                return False
        return False

    def view_details(self):
        '''
        View details of particular assigment.

        Returns:list
        '''
        details = []
        if self.submit_list:
            for submition in self.submit_list:
                details.append([self.title, submition.get_student_username(),
                                submition.get_content(), submition.get_grade()])
        if details:
            return details
        return None

    def list_assignment_grades(self, student_username):
        '''
        Find submittion by user name and return info about garade.

        Returns:list
        '''
        for submit in self.submit_list:
            if submit.get_student_username() == student_username:
                return [self.title, submit.get_grade()]
        return None

    @staticmethod
    def return_ass(number):
        """
        Return assignment objc by given index in list.
        :param number: index of objc
        :return: objc
        """
        for index, ass in enumerate(Assignment.list_assignment):
            if str(index) == number:
                return ass

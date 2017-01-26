class Submition:
    '''
    Represent an submit of individual student_username
    '''
    def __init__(self, student_username, content, grade):
        '''
        Constructor of Submition object.
        '''
        self.student_username = student_username
        self.content = content
        self.grade = grade

    @classmethod
    def create(cls, student_username, content='', grade=''):
        '''
        Make new submition.

        Returns: instance of Submition class
        '''
        return Submition(student_username, content, grade)

    def get_student_username(self):
        '''
        Returns a student username for submition.

        Returns: str
        '''
        return self.student_username

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

    def change_grade(self, new_grade):
        '''
        Changes a submition grage to new value.

        Returns: boolean
        '''
        if not self.grade:
            self.grade = new_grade
            return True
        return False

    def change_content(self, new_content):
        '''
        Changes a content of submition.

        Returns: boolean
        '''
        if not self.content:
            self.content = new_content
            return True
        return False

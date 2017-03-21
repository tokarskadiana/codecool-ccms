from model.sqlRequest import SqlRequest
from model.student import Student


class Checkpoint():
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
            cls.add_checkpoint(name, checkpoint_date, student.id, mentor_id, card)

    @classmethod
    def add_checkpoint(cls, name, checkpoint_date, student_id, mentor_id, card):
        """Add checkpoint to db"""
        SqlRequest.sql_request(
            "INSERT INTO checkpoint (name, checkpoint_date, student_id, mentor_id,card) VALUES ('{}', '{}', {}, {},{})".format(
                name, checkpoint_date, student_id, mentor_id, card))

    @classmethod
    def get_list_distinct(cls):
        """
        Get all available checkpoints
        :return:
        """
        query = "SELECT name,checkpoint_date FROM checkpoint GROUP BY name"
        return SqlRequest.sql_request(query)

    @classmethod
    def remove_checkpoint(cls, name):
        """
        Remove checkpoint from db
        :param name:
        :return:
        """
        SqlRequest.sql_request('DELETE  FROM checkpoint WHERE name="{}"'.format(name))

    @classmethod
    def get_details_checkpoint_by_name(cls, name):
        """
        Get details of checkpoint by its name
        :return: List of objects
        """
        query = "SELECT id, name, checkpoint_date, student_id, mentor_id, card FROM checkpoint WHERE name='{}'".format(
            name)
        checkpoints = SqlRequest.sql_request(query)
        chkp_objects = []
        if checkpoints:
            for chkp in checkpoints:
                temp_object = cls(chkp[0], chkp[1], chkp[2], chkp[3], chkp[4], chkp[5])
                chkp_objects.append(temp_object)
            return chkp_objects
        return None

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
                    query = "UPDATE checkpoint SET card={} WHERE id={}".format(int(grade), id_list[i])
                    SqlRequest.sql_request(query)
            except:
                print('Hackers arent ya?')

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
    def get_by_studedent_id(cls, student_id):
        """
        Get list of checkpoin objects by  student id
        """
        chkp_objects = []
        query = 'SELECT * FROM checkpoint WHERE student_id={}'.format(student_id)
        checkpoints = SqlRequest.sql_request(query)
        if checkpoints:
            for chkp in checkpoints:
                check = 'Not graded'
                if chkp[5] == 1:
                    check = 'Red'
                elif chkp[5] == 2:
                    check = 'Yellow'
                elif chkp[5] == 2:
                    check = 'Green'

                temp_object = cls(chkp[0], chkp[1], chkp[2], chkp[3], chkp[4], check)
                chkp_objects.append(temp_object)
            return chkp_objects
        return None

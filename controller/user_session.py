from model.manager import Manager
from model.mentor import Mentor
from model.student import Student
from model.employee import Employee


def user_session(id, class_name):
    """Return object with given class name in class_name and id"""
    if class_name == "Student":

        return Student.get_by_id(id)
    elif class_name == "Mentor":

        return Mentor.get_by_id(id)
    elif class_name == "Employee":

        return Employee.get_by_id(id, 'assistant')
    elif class_name == "Manager":

        return Manager.get_by_id(id)
    return None

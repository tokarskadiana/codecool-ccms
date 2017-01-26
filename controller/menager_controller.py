from controller.employee_controller import EmployeeController
from model import mentor


class MenagerController(EmployeeController):

    def list_mentor(self):
        mentor.Mentor.list_mentors()  # return list of mentors (obcj)

    def view_mentors_details(self, username):
        for person in mentor.Mentor.mentors_list:
            if person.username == username:
                mentor.Mentor.view_mentor_details(person, person.username)

    def edit_mentor(self):
        pass

    # +add_mentor(first_name:str, last_name:str, password:str):str
    @staticmethod
    def add_mentor(first_name, last_name, password):
        mentor.Mentor.add_mentor(password, first_name, last_name)

    # +remove_mentor(Mentor_obj:obj):str
    @staticmethod
    def remove_mentor(objc):
        for person in mentor.Mentor.mentors_list:
            if objc.username == person.username:
                # returns list of mentors ???
                mentor.Mentor.delete_mentor(objc.username)

from model import student
from model import attendance
from model.assignment import Assignment
from controller.employee_controller import EmployeeController
from controller.user_controller import UserController
import view
from model.student import Student
from .user_controller import UserController


class MentorController(EmployeeController):
    def list_assignment(self):
        assignment_list = []
        for assignment in Assignment.get_list():
            assignment_list.append(str(assignment).split())
        return assignment_list

    def add_assiment(self, title, description, type, due_date):
        """
        Add assignment object to the list of assignments
        :param title: store of title of assignment object
        :param description: store of description of assignment object
        :param due_date: store of due date of assignment object
        """
        if not due_date:
            due_date = 'No due date'
        user_name = self.user.get_username()
        Assignment.create(title, description, type, user_name, due_date)

    def grade_assignment(self, assiment_title, student_username, grade):
        """
        Grade student assignment submission
        :param assiment_title: (str) title of assignment
        :param student_username: (str) student user name
        :param grade: (str) grade
        :return: (str)
        """
        for assiment in Assignment.get_list():
            if assiment.get_title() == assiment_title:
                if assiment.grade_assigment(self.user.get_username(), student_username, grade):
                    return True
        return False

    @staticmethod
    def check_attendence(day):
        """
        Check presence of students for given day
        :param day: (str) store date of given day
        """
        "query = ('SELECT id, first_name,last_name, username, mail, telephone FROM student')"
        atta = attendance.Attendance(day, {})
        for person in student.Student.list_student():
            print('{} {}'.format(person[1], person[2]))
            while True:
                ask = input('0 or 1')
                if ask == '0' or ask == '1':
                    break
            atta.check_attendance(person[3], ask)
        atta.add()

    def add_student(self, first_name, last_name, password):
        """
        Use student method to create student object
        :param first_name: store of first name of Student object
        :param last_name: store of last name of Student object
        :param password: store of password of Student object
        """
        student.Student.add_student(password, first_name, last_name)

    def edit_student(self, number, telep, mai):
        """
        Edit student details to change/add phone number and e-mail
        :param number: store of number of Student object on the list
        :param telep: store of phone number of Student object
        :param mai: store of e-mail address of Student object
        """

        for index, stu in enumerate(student.Student.list_of_students):
            if str(index) == number:
                stu.edit_student(telephone=telep, mail=mai)

    # def remove_student(self, number):
    #
    #     """
    #     Remove student form a list of students
    #     :param number: store of number of Student object on the list
    #     """
    #     # for index, stu in enumerate(student.Student.list_of_students):
    #     #     if str(index) == number:
    #     #         student.Student.delete_student(stu.username)
    #     pass

    def view_presence_statistic(self):
        """
          Calculate overall present for each student.
          :return (dict): SAMPLE DICT {'patrycja': '100', 'przemek': '50'}
          """
        return attendance.Attendance.present_statistic()

    def view_details(self, number):
        for index, assignment in enumerate(Assignment.get_list()):
            if str(index) == number:
                return assignment.view_details()
        return None

    @staticmethod
    def mentor_session(user):
        """
        Run mentor menu session
        :param user: mentor user object
        """
        session = MentorController(user)
        while True:
            view.View.mentor_menu()
            option = input('\nChoose the option:')
            if option == '1':
                view.View.clear()
                day = input('write day "day.month.year"')
                MentorController.check_attendence(day)

            elif option == '2':
                view.View.clear()
                title = input('Enter assignment title: ')
                type = input('Enter type(group or individual): ')
                description = input('Enter assignment description: ')
                due_date = input('Enter assignment due date(or skip if there no due date):')
                session.add_assiment(title, description, type, due_date)
                print('Assignment was added.')
                input('\nEnter some key to get back:')

            elif option == '3':
                view.View.clear()
                assignment_list = session.list_assignment()
                view.View.print_two_demention_list(assignment_list)
                number = input('Enter index of assigment: ')
                details = session.view_details(number)
                if details:
                    view.View.print_two_demention_list(details)
                    title = details[0][0]
                    u_name = input('\nSelect username:')
                    grade = input('\nEnter grade:')
                    if session.grade_assignment(title, u_name, grade):
                        print('You grade assignment.')
                        input('\nEnter some key to get back:')
                    else:
                        print('Something went wrong. You didnt grade assignment.')
                        input('\nEnter some key to get back:')

            elif option == '4':
                view.View.clear()
                first_name = input('First name: ')
                last_name = input('Last name: ')
                password = input('Password: ')
                session.add_student(first_name, last_name, password)
                input('\nEnter some key to get back:')

            elif option == '5':
                view.View.clear()
                view.View.print_user_list(Student.list_student())
                team_list = user.list_teams()
                view.View.showTeams(team_list)
                number = input('Select ID of student: ')
                telephone = input('Telephone: ')
                mail = input('Mail: ')
                team = input('Select team ID: ')
                Student.edit_student(number, mail, telephone, team)
                input('\nEnter some key to get back:')

            elif option == '6':
                view.View.clear()
                view.View.print_user_list(Student.list_student())
                id = input('ID of student: ')
                Student.delete_student(id)
                input('\nEnter some key to get back:')

            elif option == '7':
                view.View.clear()
                view.View.display_static_present(session.view_presence_statistic())
                input('\nEnter some key to get back:')
            elif option == '8':
                view.View.clear()
                team_list = user.list_teams()
                view.View.showTeams(team_list)
                input('\nEnter some key to get back:')
            elif option == '9':
                view.View.clear()
                view.View.print_user_list(Student.list_student())
                input('\nEnter some key to get back:')
            elif option == '10':
                view.View.clear()
                user.list_teams()
                user.addOrRemoveTeam()

            elif option == '0':
                UserController.sign_out()
                return
            else:
                continue

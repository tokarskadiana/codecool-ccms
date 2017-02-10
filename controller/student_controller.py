from controller.user_controller import UserController
from model.assignment import Assignment
from view import View as view


class StudentController(UserController):
    """Class which controls user behaviour"""

    def list_assignment(self):
        assignment_list = []
        for assignment in Assignment.get_list():
            assignment_list.append(str(assignment).split())
        return assignment_list

    def list_assignment_title_content(self, username):
        info = []
        for assignment in Assignment.get_list():
            if assignment.get_submition_content(username):
                content = assignment.get_submition_content(username)
            else:
                content = 'You dont submit this assignment yet.'
            info.append([assignment.get_title(), content])
        return info

    def list_assignment_grades(self):
        '''
        Returns and prints out assignment grades for student_username

        Returns:str
        '''
        student_assignment_grade = []
        for assignment in Assignment.get_list():
            grade = assignment.list_assignment_grades(self.user.get_username())
            if grade:
                if not grade[1]:
                    grade[1] = '---'
                student_assignment_grade.append(grade)
        return student_assignment_grade

    def submit_assignment(self, assignment_title, content):
        '''
        Submit assignment as a student
        return: string
        '''
        for assignment in Assignment.get_list():
            if assignment.get_title() == assignment_title:
                submit = assignment.submit_assignment(
                    self.user.get_username(), content)
                if submit:
                    return 'Your submit was added.'
        return 'Something went wrong, your submit wasn\'t added.'

    @staticmethod
    def student_session(user):
        """
        Static method show menu of user
        :param user:
        :return: None
        """
        session = StudentController(user)
        while True:
            view.student_menu()
            option = input('\nChoose the option:')
            if option == '1':
                view.clear()
                view.print_assignments_list(session.list_assignment())
                input('\nPress any key to back')
            elif option == '2':
                view.clear()
                grades = session.list_assignment_grades()
                view.print_assignment_grades(grades)
                input('\nPress any key to back')
                continue
            elif option == '3':
                view.clear()
                assignments_list = session.list_assignment_title_content(
                    session.user.get_username())
                view.print_two_demention_list(assignments_list)
                assignment_title = input('\nEnter assignment title to submit:')
                content = input('Enter content of assignment:')
                print(session.submit_assignment(assignment_title, content))
                input('\nPress any key to back')

            elif option == '5':
                view.clear()
                data = user.get_attandance()
                if data:
                    view.show_student_presents(data)
                input('\nPress any key to back')
            elif option == '0':
                UserController.sign_out()
                return
            else:
                print('Enter valid option.')
                continue

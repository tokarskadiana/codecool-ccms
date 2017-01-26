from controller.user_controller import UserController
from model.assignment import Assignment
from view import View as view


class StudentController(UserController):

    def list_assignment_grades(self):
        '''
        Returns and prints out assignment grades for student_username

        Returns:str
        '''
        student_assignment_grade = []
        for assignment in Assignment.get_list():
            grade = assignment.list_assignment_grades(self.user.get_username())
            student_assignment_grade.append(grade)
        return student_assignment_grade

    def submit_assignment(self, assignment_title, content):
        '''
        Submit assignment as a student
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
        session = StudentController(user)
        while True:
            view.student_menu()
            option = input('\nChoose the option:')
            if option == '1':
                view.clear()
                grades = session.list_assignment_grades()
                print('Your assignments:'
                      '\n')
                view.print_assignment_grades(grades)
                input('\nPress any key to back')
                continue
            elif option == '2':
                view.clear()
                assignment_title = input('Enter assignment title to submit:')
                content = input('Enter content of assignment:')
                print(session.submit_assignment(assignment_title, content))
            elif option == '0':
                UserController.sign_out()
                return
            else:
                print('Enter valid option.')
                continue

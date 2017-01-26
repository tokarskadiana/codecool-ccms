from tabulate import tabulate


class View:

    @staticmethod
    def print_assignment_grades(list_assignment_grades):
        for item in list_assignment_grades:
            print(item)

    @staticmethod
    def student_menu():
        print('''
        -----------MENU-----------
        1. List your assignments
        2. Submit assignment
        0. Exit
        ''')

    @staticmethod
    def print_assignment_grades(assignment_grades):
        headers = ['Assiment', 'Grade']
        print(tabulate(assignment_grades, headers,
                       tablefmt="fancy_grid", stralign="center"))

    @staticmethod
    def main_menu():
        print('Welcome in CodeCool Management System')
        username = input('Enter your username:')
        password = input('Enter your password:')
        return username, password

    @staticmethod
    def mentor_menu():
        print('''
        -----------MENU-----------
        1. Check attendance
        2. Add assignment
        3. Grade assignment
        4. Add student
        5. Edit student
        6. Delete student
        7. View presense statistics
        0. Exit
        ''')

    @staticmethod
    def menager_menu():
        print('''
        -----------MENU-----------
        1. List mentors
        2. Add mentor
        3. Add assistant
        4. Edit mentor
        5. Delete mentor
        0. Exit
        ''')

    @staticmethod
    def employee_menu():
        print('''
        -----------MENU-----------
        1. List student
        0. Exit
        ''')

    @staticmethod
    def print_mentors_list(mentors_list):
        for mentor in mentors_list:
            print (mentor)

    @staticmethod
    def edit_menu():
        print('''
        You can edit following parameters:
            - telephone
            - mail
        ''')

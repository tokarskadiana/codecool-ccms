from model.assignment import Assignment

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
        7. View presence statistics
        0. Exit
        ''')

    @staticmethod
    def display_assigments():
        for index, ass in enumerate(sorted((Assignment.list_assignment))):
            print('{} {} {}'.format(index, ass.title, ass.due_date))

    @staticmethod
    def display_ass(number):
        for index, ass in enumerate(sorted(Assignment.list_assignment)):
            if str(index) == number:
                details = ass.view_details()
                for index, student_subb in enumerate(details):
                    print('{} {} {} {}'.format(index, student_subb[0], student_subb[1], student_subb[2]))

    @staticmethod
    def display_students():
        

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
    def show_full_name(user_list):
        n = 0
        for user in user_list:
            n += 1
            print('{}. {} {}'.format(n , user[0], user[1]))



    @staticmethod
    def show_details(user):
        print('{} {} phone number:{}, e-mail: {}'.format(user[0], user[1], user[3], user[4]))


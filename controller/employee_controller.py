from flask import Blueprint, session, render_template, redirect, url_for, flash, request
from controller.decorators import login_required, required_roles
from controller.user_session import user_session
from model.manager import Manager
from model.mentor import Mentor
from model.employee import Employee

employee_controller = Blueprint('employee_controller', __name__,
                                template_folder='templates')


# -----------------EMPLOYEE------------------


def save_employee(position, save, obj=None):
    employee = Employee(password=request.form['password'],
                        first_name=request.form['first_name'],
                        last_name=request.form['last_name'],
                        position=position,
                        telephone=request.form.get('phone_number', ''),
                        mail=request.form.get('mail', ''),
                        salary=request.form.get('salary', ''))
    if save == 'add':
        employee.add_employee()
    elif save == 'edit':
        obj.edit_employee(password=request.form['password'],
                          first_name=request.form['first_name'],
                          last_name=request.form['last_name'],
                          telephone=request.form.get('phone_number', ''),
                          mail=request.form.get('mail', ''),
                          salary=request.form.get('salary', ''))


# ----------------MENTORS-----------------


@employee_controller.route('/list-mentors')
@login_required
@required_roles('Manager')
def list_mentors():
    """
    GET to generate a list of mentors
    """
    mentors_list = Mentor.list_mentors()
    add = 'employee_controller.add_mentor'
    edit = 'employee_controller.edit_mentor'
    delete = 'employee_controller.delete_mentor'
    return render_template('viewemployee.html', user=user_session(session['user'], session['type']),
                           employee_list=mentors_list, employee='Mentor',
                           add=add, edit=edit, delete=delete)


@employee_controller.route('/list-mentors/add', methods=['GET', 'POST'])
@login_required
@required_roles('Manager')
def add_mentor():
    """
    GET: returns add mentor formula
    POST: returns list of mentors with new mentor added

    """

    if request.method == 'POST':
        save_employee('mentor', 'add')
        return redirect(url_for('employee_controller.list_mentors'))
    return render_template('addemployee.html', user=user_session(session['user'], session['type']),
                           list='employee_controller.list_mentors')


@employee_controller.route('/list-mentors/edit/<employee_id>', methods=['GET', 'POST'])
@login_required
@required_roles('Manager')
def edit_mentor(employee_id):
    """
    Edit mentor formula to edit mentor details
    :param employee_id: int
    GET return edit mentor formula
    POST return list of mentors with edited mentor changes saved
    """
    mentor = Mentor.get_by_id(employee_id)
    if request.method == 'POST':
        save_employee('mentor', 'edit', mentor)
        return redirect(url_for('employee_controller.list_mentors'))
    return render_template('editemployee.html', user=user_session(session['user'], session['type']), employee=mentor,
                           list='employee_controller.list_mentors')


@employee_controller.route('/delete-mentor/<employee_id>')
@login_required
@required_roles('Manager')
def delete_mentor(employee_id):
    """
    Remove mentor from list(data base)
    :param employee_id: int
    GET return list of mentors without removed mentor
    """
    mentor = Mentor.get_by_id(employee_id)
    mentor.delete_employee()
    return redirect(url_for('employee_controller.list_mentors'))


# ----------------ASSISTANTS-----------------


@employee_controller.route('/list-assistants')
@login_required
@required_roles('Manager')
def list_assistants():
    """
    GET to generate a list of assistants
    """
    assistants_list = Employee.list_employee('assistant')
    add = 'employee_controller.add_assistant'
    edit = 'employee_controller.edit_assistant'
    delete = 'employee_controller.delete_assistant'
    return render_template('viewemployee.html', user=user_session(session['user'], session['type']),
                           employee_list=assistants_list, employee='Assistant',
                           add=add, edit=edit, delete=delete)


@employee_controller.route('/list-assistants/add', methods=['GET', 'POST'])
@login_required
@required_roles('Manager')
def add_assistant():
    """
    GET: returns add assistant formula
    POST: returns list of assistant with new assistant added
    """
    if request.method == 'POST':
        save_employee('assistant', 'add')
        return redirect(url_for('employee_controller.list_assistants'))
    return render_template('addemployee.html', user=user_session(session['user'], session['type']),
                           employee='Assistant', list='employee_controller.list_assistants')


@employee_controller.route('/list-assistant/edit/<employee_id>', methods=['GET', 'POST'])
@login_required
@required_roles('Manager')
def edit_assistant(employee_id):
    """
    Edit assistant formula to edit assistant details
    :param employee_id: int
    GET return edit assistants formula
    POST return list of assistants with edited assistant changes saved
    """
    assistant = Employee.get_by_id(employee_id, 'assistant')
    if request.method == 'POST':
        save_employee('assistant', 'edit', assistant)
        return redirect(url_for('employee_controller.list_assistants'))
    return render_template('editemployee.html', user=user_session(session['user'], session['type']), employee=assistant,
                           list='employee_controller.list_assistants')


@employee_controller.route('/delete-assistant/<employee_id>')
@login_required
@required_roles('Manager')
def delete_assistant(employee_id):
    """
    Remove assistant from list(data base)
    :param employee_id: int
    GET return list of assistants without removed assistant
    """
    assistant = Employee.get_by_id(employee_id, 'assistant')
    assistant.delete_employee()
    return redirect(url_for('employee_controller.list_assistants'))

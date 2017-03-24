from app import app
from model.sql_alchemy_db import db
from flask import Flask, render_template
from controller.database_controller import DatabaseController
from controller.login import authorization
from controller.index import main_page
from controller.employee_controller import employee_controller
from controller.student_controller import student_controller
from controller.team_controller import team_controller
from controller.assignment_controller import assignment_controller
from controller.attendance_controller import attendance_controller
from controller.checkpoint_controller import checkpoint_controller
from controller.helpers import page_not_found, override_url_for


app.register_blueprint(authorization)
app.register_blueprint(employee_controller)
app.register_blueprint(student_controller)
app.register_blueprint(team_controller)
app.register_blueprint(assignment_controller)
app.register_blueprint(attendance_controller)
app.register_blueprint(checkpoint_controller)
app.register_blueprint(main_page)


if __name__ == '__main__':
    db.create_all()
    DatabaseController.sample_data()
    app.run(debug=True)

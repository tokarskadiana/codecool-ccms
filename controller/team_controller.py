from flask import Blueprint, session, render_template, redirect, url_for, flash, request
from controller.decorators import login_required, required_roles
from controller.user_session import user_session
from model.team import Team

team_controller = Blueprint('team_controller', __name__,
                            template_folder='templates')


# ------------TEAMS----------------


@team_controller.route('/list-teams')
@login_required
@required_roles('Mentor')
def list_teams():
    """Return viewteams.html with list of id teams and teams names."""
    teams = Team.list_teams()
    return render_template('viewteams.html', user=user_session(session['user'], session['type']), teams=teams)


@team_controller.route('/list-teams/add', methods=["GET", 'POST'])
@login_required
@required_roles('Mentor')
def add_team():
    """
    Return team_form.html
    POST: Add team to database basing on data from request.form['name'] and redirect user to list-teams definition.
    """
    if request.method == 'POST':
        Team(request.form['name']).add_team()
        flash('Team was added')
        return redirect('list-teams')
    return render_template("team_form.html", user=user_session(session['user'], session['type']))


@team_controller.route('/list-teams/edit/<team_id>', methods=["GET", 'POST'])
@login_required
@required_roles('Mentor')
def edit_team(team_id):
    """
    Return team_form.html with team basing on given team_id
    POST: Edit team with given values in request.form['name'] and redirect user to list-teams definition.
    :param team_id: team id in database
    """
    team = Team.get_by_id(team_id)
    if request.method == 'POST':
        team.name = request.form['name']
        team.edit_team()
        flash('Team was edited')
        return redirect(url_for('team_controller.list_teams'))
    return render_template('team_form.html', user=user_session(session['user'], session['type']), team=team)


@team_controller.route('/list-teams/delete/<team_id>')
@login_required
@required_roles('Mentor')
def delete_team(team_id):
    """Delete from database team by given id in team_id"""
    team = Team.get_by_id(team_id)
    team.delete_team()
    flash('Team was deleted')
    return redirect(url_for('team_controller.list_teams'))

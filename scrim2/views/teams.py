from flask import Blueprint, render_template, g, redirect, url_for
from flask.ext.login import login_required
from scrim2.extensions import db

teams_bp = Blueprint('teams_bp', __name__)

@teams_bp.route('/team/<id>')
@login_required
def team(id):
    return render_template('/teams/team.html')

@teams_bp.route('/teams', methods=['GET', 'POST'])
@teams_bp.route('/teams/page/<int:page>', methods=['GET', 'POST'])
@login_required
def teams_all(page=1):
    return render_template('teams/teams.html')

@teams_bp.route('/team/new', methods=['GET', 'POST'])
@login_required
def team_new():
    return render_template('/teams/team_new.html')

@teams_bp.route('/team/edit/<team_id>', methods=['GET', 'POST'])
@login_required
def team_edit(team_id):
    return render_template('/teams/team_edit.html')

@teams_bp.route('/team/delete/<team_id>')
@login_required
def team_delete(team_id):
    return 'OK'

"""
promote, demote, kick
"""

from flask import Blueprint, render_template, url_for, g, redirect
from flask.ext.login import login_required
from scrim2.extensions import db

profile_bp = Blueprint('profile_bp', __name__)

@profile_bp.route('/profile')
@login_required
def my_profile(steam_id):
    return redirect(url_for('profile', steam_id=g.user.steam_id))

@profile_bp.route('/profile/<steam_id>')
def profile(steam_id):
    return render_template('/profile/profile.html')

@profile_bp.route('/profile/<steam_id>/edit', methods=['GET', 'POST'])
def profile_edit(steam_id):
    return render_template('/profile/profile_edit.html')

from flask import Blueprint, render_template, url_for, g, redirect
from flask.ext.login import login_required
from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound
from scrim2.models import User
from scrim2.extensions import db

profile_bp = Blueprint('profile_bp', __name__)

@profile_bp.route('/profile')
@login_required
def my_profile():
    return redirect(url_for('profile_bp.profile', steam_id=g.user.steam_id))

@profile_bp.route('/profile/<steam_id>')
def profile(steam_id):
    try:
        u = User.query.filter_by(steam_id=steam_id).one()
        return render_template('/profile/profile.html',
                u=u)
    except NoResultFound:
        return "no", 404

@profile_bp.route('/profile/<steam_id>/edit', methods=['GET', 'POST'])
def profile_edit(steam_id):
    return render_template('/profile/profile_edit.html')

from flask import Blueprint, render_template, url_for, g, redirect
from flask.ext.login import login_required
from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound
from scrim2.models import User
from scrim2.extensions import db, rds
from scrim2.forms import EditUserForm

profile_bp = Blueprint('profile_bp', __name__)

@profile_bp.route('/profile')
@login_required
def my_profile():
    return redirect(url_for('profile_bp.profile', steam_id=g.user.steam_id))

@profile_bp.route('/profile/<steam_id>')
@login_required
def profile(steam_id):
    try:
        u = User.query.filter_by(steam_id=steam_id).one()
        status = rds.get(u.id)
        return render_template('/profile/profile.html',
                u=u,
                status=status)
    except NoResultFound:
        return "no", 404

@profile_bp.route('/profile/edit', methods=['GET', 'POST'])
@login_required
def profile_edit():

    form = EditUserForm()

    if form.validate_on_submit():
        g.user.skill_level = form.skill_level.data
        g.user.main_class = form.main_class.data
        db.session.add(g.user)
        db.session.commit()
        # flash()
        return redirect(url_for('profile_bp.my_profile'))
    else:
        form.main_class.data = g.user.main_class
        form.skill_level.data = g.user.skill_level
        return render_template('/profile/profile_edit.html', form=form)


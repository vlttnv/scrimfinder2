from flask import Blueprint, render_template, json, g, current_app, redirect, url_for
from flask.ext.login import login_required
from scrim2.extensions import db, rds
import redis

live_bp = Blueprint('live_bp', __name__)

@live_bp.route('/live')
@login_required
def live():
    import string
    import random

    token = ''.join(random.choice(string.ascii_uppercase) for i in range(80))
    rds.set(str(g.user.id)+":token", token)

    return render_template('/live/live.html',
            token=token)

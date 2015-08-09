from flask import Blueprint, render_template, json, g, current_app, redirect, url_for
from flask.ext.login import login_required
from scrim2.extensions import db

live_bp = Blueprint('live_bp', __name__)

@live_bp.route('/live')
@login_required
def live():
    return render_template('/live/live.html')

from flask import Blueprint, render_template, json, g, current_app, redirect, url_for, session
from datetime import datetime as dt
from scrim2.extensions import oid, db, lm
from scrim2.models import User
from sqlalchemy.orm.exc import NoResultFound
from flask.ext.login import login_user, logout_user, current_user
import requests, re


home_bp = Blueprint('home_bp', __name__)

@home_bp.route('/')
def index():
    if current_user.is_authenticated():
        return redirect(url_for('live_bp.live'))
    return render_template('/home/index.html')

@home_bp.route('/login')
@oid.loginhandler
def login():
    """Log in via Steam OpenID

    """

    if g.user is not None:
        return redirect(oid.get_next_url())
    else:
        return oid.try_login('http://steamcommunity.com/openid')

@oid.after_login
def after_login(resp):
    """
    """
    steam_id_regex = re.compile('steamcommunity.com/openid/id/(.*?)$')
    steam_id = steam_id_regex.search(resp.identity_url).group(1)

    try:
        g.user = User.query.filter_by(steam_id=steam_id).one()
        user_info = get_user_info(g.user.steam_id)
        login_user(g.user)
        return redirect(oid.get_next_url())
    except NoResultFound:
        print "CREATIN USER"
        g.user = User()
        steam_data             = get_user_info(steam_id)
        g.user.steam_id        = steam_id
        g.user.nickname        = steam_data['personaname']
        g.user.avatar_url      = steam_data['avatar']
        g.user.avatar_url_full = steam_data['avatarfull']
        g.user.join_date       = dt.utcnow()
        db.session.add(g.user)
        db.session.commit()
        login_user(g.user)
        return redirect(url_for('home_bp.index'))

@home_bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home_bp.index'))

def get_user_info(steam_id):
    """
    Return player summaries of the user that has the steam_id.

    Example:
    {
        u'steamid': u'steamid',
        u'personaname': u'personaname',
        ...
    }

    See: https://developer.valvesoftware.com/wiki/Steam_Web_API#GetPlayerSummaries_.28v0002.29
    """

    api = 'http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?'
    params = {
        'key': current_app.config['STEAM_API_KEY'],
        'steamids': steam_id,
        'format': json
    }
    user_info = requests.get(url=api, params=params)
    user_info_json = user_info.json()

    return user_info_json['response']['players'][0] or {}







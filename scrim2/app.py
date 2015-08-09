from flask import Flask, g, session, url_for, redirect
from .views.home import home_bp
from .views.live import live_bp
from .views.profile import profile_bp
from .views.teams import teams_bp
from scrim2.extensions import db, lm, oid
from scrim2.models import User

def create_app():
    scrim2_app = Flask(__name__, instance_relative_config=True)

    scrim2_app.config.from_object('config')
    scrim2_app.config.from_pyfile('config.py')

    config_blueprints(scrim2_app)
    config_extensions(scrim2_app)
    config_befores(scrim2_app)
    lm_decorators()

    return scrim2_app

def config_blueprints(the_app):
    the_app.register_blueprint(home_bp)
    the_app.register_blueprint(live_bp)
    the_app.register_blueprint(profile_bp)
    the_app.register_blueprint(teams_bp)

def config_extensions(the_app):
    db.init_app(the_app)
    lm.init_app(the_app)
    oid.init_app(the_app)

def config_befores(the_app):
    @the_app.before_request
    def before_request():
        """
        A handler before every request. TODO: More.
        """

        if 'user_id' in session:
            g.user = User.query.filter_by(id=session['user_id']).first()
        else:
            g.user = None

def lm_decorators():
    @lm.user_loader
    def load_user(id):
        return User.query.get(int(id))

    @lm.unauthorized_handler
    def unauthorized():
        # TODO: flash
        return redirect(url_for('home_bp.index'))

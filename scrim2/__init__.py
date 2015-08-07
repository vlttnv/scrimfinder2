from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from .views.home import home_bp
from tornado.wsgi import WSGIContainer
from tornado.web import Application, FallbackHandler
from tornado.websocket import WebSocketHandler

# Configure
scrim2_app = Flask(__name__, instance_relative_config=True)
scrim2_app.config.from_object('config')
scrim2_app.config.from_pyfile('config.py')

scrim2_app.register_blueprint(home_bp)

# Init
db = SQLAlchemy(scrim2_app)
container = WSGIContainer(scrim2_app)
server = Application([
    (r'.*', FallbackHandler, dict(fallback=container))
    ], debug=True)

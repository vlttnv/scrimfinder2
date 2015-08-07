from flask import Flask
from .views.home import home_bp
from tornado.wsgi import WSGIContainer
from tornado.web import Application, FallbackHandler
from tornado.websocket import WebSocketHandler

scrim2_app = Flask(__name__)
scrim2_app.register_blueprint(home_bp)

container = WSGIContainer(scrim2_app)
server = Application([
    (r'.*', FallbackHandler, dict(fallback=container))
    ], debug=True)

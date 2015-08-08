from scrim2 import create_app
from tornado.web import Application, FallbackHandler
from tornado.websocket import WebSocketHandler
from tornado.ioloop import IOLoop
from tornado.wsgi import WSGIContainer
from scrim2.extensions import db
import sys, os.path
from migrate.versioning import api
from config import SQLALCHEMY_DATABASE_URI
from config import SQLALCHEMY_MIGRATE_REPO

scrim2_app = create_app()



if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(1)
    elif sys.argv[1] == 'run':
        container = WSGIContainer(scrim2_app)
        server = Application([
            (r'.*', FallbackHandler, dict(fallback=container))
            ], debug=True)
        server.listen(8080)
        IOLoop.instance().start()
    elif sys.argv[1] == 'db':
        with scrim2_app.app_context():
            db.create_all()
        if not os.path.exists(SQLALCHEMY_MIGRATE_REPO):
            api.create(SQLALCHEMY_MIGRATE_REPO, 'database repository')
            api.version_control(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
        else:
             api.version_control(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO, api.version(SQLALCHEMY_MIGRATE_REPO))


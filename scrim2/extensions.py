from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.openid import OpenID
from flask.ext.login import LoginManager

db = SQLAlchemy()
lm = LoginManager()
oid = OpenID()

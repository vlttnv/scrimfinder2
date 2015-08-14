from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.openid import OpenID
from flask.ext.login import LoginManager
from flask.ext.redis import FlaskRedis


db  = SQLAlchemy()
lm  = LoginManager()
oid = OpenID()
rds = FlaskRedis()

from scrim2.extensions import db

class User(db.Model):
    id                      = db.Column(db.Integer,
            primary_key=True,
            autoincrement=True)
    steam_id                = db.Column(db.String(40), unique=True)
    nickname                = db.Column(db.String(80))
    avatar_url              = db.Column(db.String(80))
    avatar_url_full         = db.Column(db.String(80))
    join_date               = db.Column(db.DateTime)

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self.id)

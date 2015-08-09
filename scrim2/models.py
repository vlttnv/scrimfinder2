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
    is_merc                 = db.Column(db.Integer)
    last_updated            = db.Column(db.String(45))
    skill_level             = db.Column(db.String(80))

    # Relationship
    memberships             = db.relationship('Membership',
            backref='member',
            lazy='dynamic')
    livescrims              = db.relationship('Livescrim',
            backref='creator',
            lazy='dynamic')

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self.id)

class Team(db.Model):
    id                      = db.Column(db.Integer,
            primary_key=True)
    name                    = db.Column(db.String(45))
    skill_level             = db.Column(db.String(45))
    time_zone               = db.Column(db.String(45))
    team_type               = db.Column(db.String(45))

    # Memberships
    livescrims              = db.relationship('Livescrim',
            backref='creator_team',
            lazy='dynamic')


class Membership(db.Model):
    id                      = db.Column(db.Integer,
            primary_key=True)
    team_id                 = db.Column(db.Integer,
            db.ForeignKey('team.id')) #FK
    user_id                 = db.Column(db.Integer,
            db.ForeignKey('user.id')) #FK
    role                    = db.Column(db.String(45))

class Livescrim(db.Model):
    id                      = db.Column(db.Integer,
            primary_key=True)
    user_id                 = db.Column(db.Integer,
            db.ForeignKey('user.id'))
    team_id                 = db.Column(db.Integer,
            db.ForeignKey('team.id'))
    comment                 = db.Column(db.Text)
    server                  = db.Column(db.String(45))
    livescrim_type          = db.Column(db.String(45))
    region                  = db.Column(db.String(45))
